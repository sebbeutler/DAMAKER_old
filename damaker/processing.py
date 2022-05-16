import os
import subprocess
import math
import cv2
import numpy as np

import vedo
from vedo import Mesh
from vedo.applications import *

import SimpleITK as sitk

from aicsimageio.types import PhysicalPixelSizes
from scipy import ndimage

from py4j.java_gateway import JavaGateway
from py4j.java_collections import JavaArray

from .utils import StrFilePath, plotArray, plotChannel
from .Channel import Channel, Channels

def channelSelect(input: Channels, id: int):
    """
        Category: Channel filter
        Desc: Choose a specific channels
    """
    channels = []
    for channel in input:
        if channel.id == id:
            channels.append(channel)
    return channels

def channelInvert(input: Channel):
    input.data = 255 - input.data
    return input

def channelCrop(input: Channel, p1, p2):
    input.data = input.data[:, p1[1]:p2[1], p1[0]:p2[0]]
    return input

def channelRotate(input: Channel, degrees: float, inter: str="bicubic"):   
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
    w, h = (input.shape[2], input.shape[1])
    img_center = (input.shape[2]/2, input.shape[1]/2)
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
    new_data = np.zeros(shape=(input.shape[0], b_h, b_w), dtype=np.int32)
    
    # apply rotation
    for i in range(input.shape[0]):
        new_data[i] = cv2.warpAffine(input.data[i], rot, (b_w, b_h), flags=interpolations[inter])
    
    input.data = new_data
    return input

def channelRotateType(input: Channel, rotType):
    if rotType == cv2.ROTATE_180:
        new_data = np.zeros(shape=input.shape, dtype=np.int32)
    else:
        new_data = np.zeros(shape=(input.shape[0], input.shape[2], input.shape[1]), dtype=np.int32)
    
    for i in range(input.shape[0]):
        new_data[i] = cv2.rotate(input.data[i], rotType)
    input.data = new_data
    return input

def channelRotate90(input: Channel):
    print(input)
    channelRotateType(input, cv2.ROTATE_90_CLOCKWISE)
    return input

def channelRotate180(input: Channel):
    channelRotateType(input, cv2.ROTATE_180)
    return input

def channelRotate270(input: Channel):
    channelRotateType(input, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return input
    
def channelFlipHorizontally(input: Channel):
    for i in range(input.shape[0]):
        input.data[i] = cv2.flip(input.data[i], 1)
    return input

def channelFlipVertically(input: Channel):
    for i in range(input.shape[0]):
        input.data[i] = cv2.flip(input.data[i], 0)
    return input

def pixelIntensity(input: Channel, frameId: int=-1):
    if frameId < 0:
        data = input.data
    else:
        data = input.data[frameId]    
    
    px_intensity = np.zeros(shape=(256), dtype=np.int32)
    
    for px in data:
        px_intensity[px] += 1
    
    return px_intensity

def zProjectionMax(Input: Channel):
    return Input.data.max(0)

def zProjectionMean(Input: Channel):
    return Input.data.mean(0)

def zProjectionMin(Input: Channel):
    return Input.data.min(0)


# TODO: Verify types of the channels to be Channel
def operatorAND(input: Channels, threshold: int=1):
    result = input[0].copy()
    for channel in input:
        result.data = np.where(channel.data >= threshold, result.data, 0)
    return result

def operatorOR(input: Channels):
    datas = input.data
    for channel in input:
        datas.append(channel.data)
    return input[0].clone(np.maximum.reduce(datas))

def operatorADD(input: Channels):
    result = input[0].copy()
    result.data = result.data.astype(np.uint16)
    for channel in input:
        result.data += channel.data
    result.data = result.data.clip(0, 255)
    result.data = result.data.astype(np.uint8)
    return result

def operatorSUB(input: Channels):
    result = input[0].copy()
    result.data = result.data.astype(np.int16)
    for channel in input:
        result.data -= channel.data
    result.data = result.data.clip(0, 255)
    result.data = result.data.astype(np.uint8)
    return result

def changeBrightnessAndContrast(input: Channel, brightness: int, contrast: int):
    def contrastFactor(c):
        return (259*(c + 255)) / (255*(259 - c))

    factor = contrastFactor(contrast)
    
    data = input.data.astype(np.float16)
    
    data += brightness
    data = factor*(data - 128) + 128
 
    input.data = data.clip(0, 255).astype(np.uint8)
    return input

def averageChannels(input: Channels):
    data = []
    if len(input) == 0:
        return
    
    shape = input[0].shape
    for chn in input:
        if shape != chn.shape:
            print("[DAMAKER] averageChannels(input: Channels): channels must be the same size")
            return
        data.append(chn.data)
    
    data = np.array(data, dtype=np.uint32)
    data = data.mean(0)
    
    res: Channel = input[0].clone(data)
    res.name = "Average"
    res.id = 0
    
    return res

def clipChannel(input: Channel, tmin: int=0, tmax: int=255, replace: bool=False):
    if not replace:
        chn = chn.copy()
    chn.data[chn.data < tmin] = 0
    chn.data[chn.data > tmax] = 0
    return chn

def thresholdChannels(input: Channels, level: int=1, replace: bool=False):
    res = []
    for channel in input:
        res.append(clipChannel(input, level/len(input) * 255, 255, replace))
    return res

def resliceTop(input: Channel):        
    Z, Y, X = input.shape
    
    reslice = np.swapaxes(input.data, 0, 1) # (Z, Y, X) -> (Y, Z, X)
    
    new_Z = Z * input.px_sizes.Z / input.px_sizes.Y
    new_Z = int(new_Z)
    
    result = np.zeros((Y, new_Z, X))
    
    for i in range(Y):
        result[i, :, :] =  cv2.resize(reslice[i], (X, new_Z), interpolation=cv2.INTER_CUBIC)
    
    return Channel("reslicedTop_" + input.name, result, PhysicalPixelSizes(input.px_sizes.X, input.px_sizes.X, input.px_sizes.Y))


def resliceLeft(input: Channel):
    Z, Y, X = input.shape
    
    reslice = np.swapaxes(input.data, 0, 2) # (Z, Y, X) -> (X, Y, Z)
    reslice = np.swapaxes(reslice, 1, 2) # (X, Y, Z) -> (X, Z, Y)
    
    new_Z = Z * input.px_sizes.Z / input.px_sizes.X
    new_Z = int(new_Z)
    
    result = np.zeros((X, new_Z, Y))
    
    for i in range(X):
        result[i, :, :] =  cv2.resize(reslice[i], (Y, new_Z), interpolation=cv2.INTER_CUBIC)
    
    return Channel("reslicedTop_" + input.name, result, PhysicalPixelSizes(input.px_sizes.X, input.px_sizes.X, input.px_sizes.Y))

def channelReverse(input: Channel):
    input.data = input.data[::-1]
    return input

def sliceVolume(data, s_z, s_y, s_x, threshold=0):
    return np.count_nonzero(data[data >= threshold]) * s_z * s_y * s_x

def channelTotalVolume(input: Channel, min_size=0):
    l, n = ndimage.label(input.data, np.ones((3, 3, 3)))
    
    f = ndimage.find_objects(l)
    
    count = []
    
    for i in range(len(f)):
        count.append(np.count_nonzero(l[f[i]] == i+1))
    count = np.array(count)
    
    return count[count >= min_size].sum() * input.px_sizes.Z * input.px_sizes.Y * input.px_sizes.X

def channelVolumeArray(input: Channel):
    z, y, x = input.shape
    
    volumes = []
    
    for i in range(z):
        volumes.append(sliceVolume(input.data[i], input.px_sizes.Z, input.px_sizes.Y, input.px_sizes.X))
    
    return volumes

def channelAxisQuantification(input: Channel):
    axisFront = channelVolumeArray(input)
    axisTop = channelVolumeArray(resliceTop(input))
    axisLeft = channelVolumeArray(resliceLeft(input))
    
    return [axisFront, axisTop, axisLeft]

def meshCompareDistance(mesh1, mesh2, largest_region=False):
    colors = []
    for i in np.linspace(-80, 80):
        c = vedo.colorMap(i, name='seismic', vmin=-80, vmax=80)
        if abs(i) < 5:
            c = 'white'
        colors.append([i, c])

    lut = vedo.buildLUT(
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
        c = vedo.colorMap(i, name='seismic', vmin=-80, vmax=80)
        if abs(i) < 5:
            c = 'white'
        colors.append([i, c])

    lut = vedo.buildLUT(
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

def channelFromBinary(input: Channel):
    input.data[input.data > 0] = 255
    return input


def wekaSegmentation(input: Channel, classifier: StrFilePath, jar_path: StrFilePath):
    process = subprocess.Popen("java -Xms200M -Xmx8G -jar " + jar_path)
    gateway = JavaGateway()

    z, y, x = input.shape
    arr = bytes(input.data.flatten().tolist())
    img = gateway.entry_point.numpyToImagePlus(arr, x, y, z)
    segmented = gateway.entry_point.runSegmentation(img, os.path.abspath(classifier))
        
    res = []
    for frame in segmented:
        res += frame
    input.data = np.array(res).reshape(z, y, x)
    channelFromBinary(input)
    gateway.shutdown()
    process.kill()
    
    return input

def resampleChannel(input: Channel, sizeX: int, sizeY: int, sizeZ: int, px_sizeX: int, px_sizeY: int, px_sizeZ: int):
    arr = sitk.GetImageFromArray(input.data.astype(np.float32))
    arr.SetSpacing(tuple(reversed(input.px_sizes)))
    
    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetOutputSpacing((px_sizeX, px_sizeY, px_sizeZ))
    flt.SetSize((sizeX, sizeY, sizeZ))
    
    input.data = sitk.GetArrayFromImage(flt.Execute(arr))
    input.px_sizes = PhysicalPixelSizes(px_sizeZ, px_sizeY, px_sizeX)
    return input

def resampleLike(input: Channel, ref: Channel):
    arr = sitk.GetImageFromArray(input.data.astype(np.float32))
    arr.SetSpacing(tuple(reversed(input.px_sizes)))
    
    ref_arr = sitk.GetImageFromArray(ref.data.astype(np.float32))
    ref_arr.SetSpacing(tuple(reversed(ref.px_sizes)))
    
    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetReferenceImage(ref_arr)
    
    input.data = sitk.GetArrayFromImage(flt.Execute(arr))
    return input

def resampleMean(input: Channels):
    shapes = []
    px_sizes = []
    for channel in input:
        shapes.append(channel.shape)
        px_sizes.append(tuple(channel.px_sizes))
    
    shape = np.array(shapes).mean(0)
    px_size = np.array(px_sizes).mean(0)
    
    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetOutputSpacing(px_size[2], px_size[1], px_size[0])
    flt.SetSize(shape[2], shape[1], shape[0])

    for chn in input:
        resampleChannel(chn, shape[2], shape[1], shape[0], px_size[2], px_size[1], px_size[0])
    
    return input

def registration(input: Channel, reference: Channel, nb_iteration: int):
    def resample(image, transform):
        reference_image = image
        interpolator = sitk.sitkLinear
        default_value = 0.0
        return sitk.Resample(image, reference_image, transform, interpolator, default_value)

    def plotSITKImage(img):
        plotChannel(Channel("", sitk.GetArrayFromImage(img)))

    ref = sitk.GetImageFromArray(reference.data.astype(np.float32))
    ref.SetSpacing(tuple(reversed(reference.px_sizes)))

    mov = sitk.GetImageFromArray(input.data.astype(np.float32))
    mov.SetSpacing(tuple(reversed(input.px_sizes)))

    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetOutputSpacing(ref.GetSpacing())
    flt.SetSize((
        int(reference.px_sizes.X / input.px_sizes.X * input.shape[2]),
        int(reference.px_sizes.Y / input.px_sizes.Y * input.shape[1]),
        int(reference.px_sizes.Z / input.px_sizes.Z * input.shape[0])
        ))

    ref = flt.Execute(ref)
    mov = flt.Execute(mov)

    initial_transform = sitk.CenteredTransformInitializer(
        ref,
        mov,
        sitk.Euler3DTransform(),
        sitk.CenteredTransformInitializerFilter.GEOMETRY
    )

    mov_res = sitk.Resample(
        mov,
        ref,
        initial_transform,
        sitk.sitkLinear,
        0.0,
        mov.GetPixelID()
    )

    registration_method = sitk.ImageRegistrationMethod()

    # Similarity metric settings.
    registration_method.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)
    registration_method.SetMetricSamplingStrategy(registration_method.REGULAR)
    registration_method.SetMetricSamplingPercentage(0.01)

    registration_method.SetInterpolator(sitk.sitkLinear)

    # Optimizer settings.
    registration_method.SetOptimizerAsGradientDescent(
        learningRate=1.0,
        numberOfIterations=nb_iteration,
        convergenceMinimumValue=1e-7,
        convergenceWindowSize=10,
    )
    registration_method.SetOptimizerScalesFromPhysicalShift()

    # Setup for the multi-resolution framework.
    registration_method.SetShrinkFactorsPerLevel(shrinkFactors=[4, 2, 1])
    registration_method.SetSmoothingSigmasPerLevel(smoothingSigmas=[2, 1, 0])
    registration_method.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()

    # Don't optimize in-place, we would possibly like to run this cell multiple times.
    registration_method.SetInitialTransform(initial_transform, inPlace=False)

    final_transform = registration_method.Execute(
        ref, mov
    )

    print(f'Final metric value: {registration_method.GetMetricValue()}')
    print(
        f'Optimizer stopping condition, {registration_method.GetOptimizerStopConditionDescription()}'
    )

    mov_res: sitk.Image = sitk.Resample(
        mov,
        ref,
        final_transform,
        sitk.sitkLinear,
        0.0,
        mov.GetPixelID(),
    )

    # reference.data = sitk.GetArrayFromImage(ref)
    input.data = sitk.GetArrayFromImage(mov_res)
    input.data = input.data.astype(np.uint8)
    
    res_px = mov_res.GetSpacing()
    input.px_sizes = PhysicalPixelSizes(res_px[2], res_px[1], res_px[0])
    
    print(f'registration complete: {input}')
    return input