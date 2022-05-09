import imp
import math
from tiffile import TiffFile
from vedo.applications import *
from vedo.picture import Picture
from os.path import exists
import cv2
import aicsimageio.readers.bioformats_reader as bioreader
from aicsimageio.types import PhysicalPixelSizes
from aicsimageio.writers import OmeTiffWriter
import typing
import numpy as np
from vedo import Plotter
from scipy import ndimage
from skimage import measure
import mcubes
from tiffChannel import *     
from vedo import * 
import vedo

def channelSelect(channels, id: int):
    return channels[id]

def channelSave(chn: TiffChannel, filename: str):
    chn.save(filename)

def channelInvert(chn: TiffChannel):    
    chn.data = 255 - chn.data
    return chn

def channelCrop(chn: TiffChannel, p1, p2):
    chn.data = chn.data[:, p1[1]:p2[1], p1[0]:p2[0]]
    return chn

def channelRotate(chn: TiffChannel, degrees: float, inter: str="bicubic"):
    interpolations = {
        "nearest": cv2.INTER_NEAREST,
        "bilinear": cv2.INTER_LINEAR,
        "bicubic": cv2.INTER_CUBIC,
        "area": cv2.INTER_AREA,
        "lanczos4": cv2.INTER_LANCZOS4
    }
    
    if inter not in interpolations.keys():
        print("[DAMAKER] Error: rotate() -> interpolation algorithm unkown.")
        return
    
    # create a rotation matric
    w, h = (chn.shape[2], chn.shape[1])
    img_center = (chn.shape[2]/2, chn.shape[1]/2)
    rot = cv2.getRotationMatrix2D(img_center, degrees, 1)
    
    # calculate the new size of a frame
    rad = math.radians(degrees)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    # re-center the frame
    rot[0, 2] += ((b_w / 2) - img_center[0])
    rot[1, 2] += ((b_h / 2) - img_center[1])
    
    # new stack of frame with the correct size
    new_data = np.zeros(shape=(chn.shape[0], b_h, b_w), dtype=np.int32)
    
    # apply rotation
    for i in range(chn.shape[0]):
        new_data[i] = cv2.warpAffine(chn.data[i], rot, (b_w, b_h), flags=interpolations[inter])
    
    chn.data = new_data
    return chn

def channelRotateType(chn: TiffChannel, rotType):
    if rotType == cv2.ROTATE_180:
        new_data = np.zeros(shape=chn.shape, dtype=np.int32)
    else:
        new_data = np.zeros(shape=(chn.shape[0], chn.shape[2], chn.shape[1]), dtype=np.int32)
    
    for i in range(chn.shape[0]):
        new_data[i] = cv2.rotate(chn.data[i], rotType)
    chn.data = new_data
    return chn

def channelRotate90(chn: TiffChannel):
    channelRotateType(chn, cv2.ROTATE_90_CLOCKWISE)
    return chn

def channelRotate180(chn: TiffChannel):
    channelRotateType(chn, cv2.ROTATE_180)
    return chn

def channelRotate270(chn: TiffChannel):
    channelRotateType(chn, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return chn
    
def channelFlipHorizontally(chn: TiffChannel):
    for i in range(chn.shape[0]):
        chn.data[i] = cv2.flip(chn.data[i], 1)
    return chn

def channelFlipVertically(chn: TiffChannel):
    for i in range(chn.shape[0]):
        chn.data[i] = cv2.flip(chn.data[i], 0)
    return chn

def pixelIntensity(chn: TiffChannel, frameId: int=-1):
    if frameId < 0:
        data = chn.data
    else:
        data = chn.data[frameId]    
    
    px_intensity = np.zeros(shape=(256), dtype=np.int32)
    
    for px in data:
        px_intensity[px] += 1
    
    return px_intensity

def zProjectionMax(tiff: TiffChannel):
    return tiff.data.max(0)

def zProjectionMean(tiff: TiffChannel):
    return tiff.data.mean(0)

def zProjectionMin(tiff: TiffChannel):
    return tiff.data.min(0)


# TODO: Verify types of the channels to be TiffChannel
def operatorAND(chn: TiffChannel, channels, threshold: int=1):
    result = chn.copy()
    for channel in channels:
        result.data = np.where(channel.data >= threshold, result.data, 0)
    return result

def operatorOR(chn: TiffChannel, channels):
    datas = [chn.data]
    for channel in channels:
        datas.append(channel.data)
    return chn.clone(np.maximum.reduce(datas))

def operatorADD(chn1: TiffChannel, channels):
    result = chn1.copy()
    result.data = result.data.astype(np.uint16)
    for channel in channels:
        result.data += channel.data
    result.data = result.data.clip(0, 255)
    result.data = result.data.astype(np.uint8)
    return result

def operatorSUB(chn1: TiffChannel, channels):
    result = chn1.copy()
    result.data = result.data.astype(np.int16)
    for channel in channels:
        result.data -= channel.data
    result.data = result.data.clip(0, 255)
    result.data = result.data.astype(np.uint8)
    return result

def changeBrightnessAndContrast(chn: TiffChannel, brightness: int, contrast: int):
    def contrastFactor(c):
        return (259*(c + 255)) / (255*(259 - c))

    factor = contrastFactor(contrast)
    
    data = chn.data.astype(np.float16)
    
    data += brightness
    data = factor*(data - 128) + 128
 
    chn.data = data.clip(0, 255).astype(np.uint8)
    return chn

def averageChannels(channels):
    data = []
    for chn in channels:
        data.append(chn.data)
    
    data = np.array(data, dtype=np.uint32)
    data = data.mean(0)
    
    return TiffChannel("average", data, channels[0].px_sizes)

def thresholdChannel(chn: TiffChannel, tmin:int=0, tmax:int=255, replace=True):
    if not replace:
        chn = chn.copy()
    chn.data[chn.data < tmin] = 0
    chn.data[chn.data > tmax] = 0
    return chn

def thresholdChannelLevel(chn: TiffChannel, nb_sample, level, replace=True, tmax=255):
    return thresholdChannel(chn, level/nb_sample * 255, tmax, replace)

def resliceTop(chn: TiffChannel):        
    Z, Y, X = chn.shape
    
    reslice = np.swapaxes(chn.data, 0, 1) # (Z, Y, X) -> (Y, Z, X)
    
    new_Z = Z * chn.px_sizes.Z / chn.px_sizes.Y
    new_Z = int(new_Z)
    
    result = np.zeros((Y, new_Z, X))
    
    for i in range(Y):
        result[i, :, :] =  cv2.resize(reslice[i], (X, new_Z), interpolation=cv2.INTER_CUBIC)
    
    return TiffChannel("reslicedTop_" + chn.name, result, PhysicalPixelSizes(chn.px_sizes.X, chn.px_sizes.X, chn.px_sizes.Y))


def resliceLeft(chn: TiffChannel):
    Z, Y, X = chn.shape
    
    reslice = np.swapaxes(chn.data, 0, 2) # (Z, Y, X) -> (X, Y, Z)
    reslice = np.swapaxes(reslice, 1, 2) # (X, Y, Z) -> (X, Z, Y)
    
    new_Z = Z * chn.px_sizes.Z / chn.px_sizes.X
    new_Z = int(new_Z)
    
    result = np.zeros((X, new_Z, Y))
    
    for i in range(X):
        result[i, :, :] =  cv2.resize(reslice[i], (Y, new_Z), interpolation=cv2.INTER_CUBIC)
    
    return TiffChannel("reslicedTop_" + chn.name, result, PhysicalPixelSizes(chn.px_sizes.X, chn.px_sizes.X, chn.px_sizes.Y))

def reverseChannel(chn: TiffChannel):
    chn.data = chn.data[::-1]
    return chn

def sliceVolume(data, s_z, s_y, s_x, threshold=0):
    return np.count_nonzero(data[data >= threshold]) * s_z * s_y * s_x

def channelTotalVolume(chn: TiffChannel, min_size=0):
    l, n = ndimage.label(chn.data, np.ones((3, 3, 3)))
    
    f = ndimage.find_objects(l)
    
    count = []
    
    for i in range(len(f)):
        count.append(np.count_nonzero(l[f[i]] == i+1))
    count = np.array(count)
    
    return count[count >= min_size].sum() * chn.px_sizes.Z * chn.px_sizes.Y * chn.px_sizes.X

def channelVolumeArray(chn: TiffChannel):
    z, y, x = chn.shape
    
    volumes = []
    
    for i in range(z):
        volumes.append(sliceVolume(chn.data[i], chn.px_sizes.Z, chn.px_sizes.Y, chn.px_sizes.X))
    
    return volumes

def channelAxisQuantification(chn: TiffChannel):
    axisFront = channelVolumeArray(chn)
    axisTop = channelVolumeArray(resliceTop(chn))
    axisLeft = channelVolumeArray(resliceLeft(chn))
    
    return [axisFront, axisTop, axisLeft]

def meshCompareDistance(mesh1, mesh2, largest_region=False):
    colors = []
    for i in np.linspace(-80, 80):
        c = colorMap(i, name='seismic', vmin=-80, vmax=80)
        if abs(i) < 5:
            c = 'white'
        colors.append([i, c])

    lut = buildLUT(
        colors,
        vmin=-80,
        vmax=80,
        interpolate=True)
    
    if largest_region:
        obj1 = Mesh(mesh1).rotateY(90).extractLargestRegion()
        obj2 = Mesh(mesh2).rotateY(90).extractLargestRegion() 
    else:
        obj1 = Mesh(mesh1).rotateY(90)
        obj2 = Mesh(mesh2).rotateY(90)
    
    obj1.distanceTo(obj2, signed=True)
    obj1.cmap(input_array="Distance", cname=lut)
    obj1.addScalarBar(title='Distance')
    
    vedo.show(obj1, new=True)
    
    return obj1.pointdata["Distance"]

def meshCompareDistance_fiji(mesh1, mesh2):
    colors = []
    for i in np.linspace(-80, 80):
        c = colorMap(i, name='seismic', vmin=-80, vmax=80)
        if abs(i) < 5:
            c = 'white'
        colors.append([i, c])

    lut = buildLUT(
        colors,
        vmin=-80,
        vmax=80,
        interpolate=True)
     
    obj1 = Mesh(mesh1).mirror("z")
    obj2 = Mesh(mesh2).mirror("z")
    
    obj1.distanceTo(obj2, signed=True)
    obj1.cmap(input_array="Distance", cname=lut)
    obj1.addScalarBar(title='Distance')
    
    obj1.show()
    
    return obj1.pointdata["Distance"]

def channelFromBinary(chn: TiffChannel):
    chn.data[chn.data > 0] = 255