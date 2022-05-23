import enum
import os
import subprocess
import math
from time import time
import cv2
import numpy as np
import time

import vedo
from vedo import Mesh
from vedo.applications import *

import SimpleITK as sitk

from aicsimageio.types import PhysicalPixelSizes
from scipy import ndimage

from py4j.java_gateway import JavaGateway
from py4j.java_collections import JavaArray

from damaker.pipeline import BatchParameters

from .utils import StrFilePath, StrFolderPath, channelsSave, plotArray, plotChannel, NamedArray
from .Channel import Channel, Channels, SingleChannel

def channelSelect(input: Channels, id: int=1) -> Channels:
    """
        Name: Channel Filter
        Category: Operations
        Desc: Choose a specific channel among the inputs.
    """
    channels = []
    for channel in input:
        if channel.id == id:
            channels.append(channel)
    if len(channels) == 0:
        print(f"channelSelect: no channels with id={id}")
    return channels

def channelInvert(input: Channel) -> Channel:
    """
        Name: Invert colors
        Category: Operations
        Desc: Every black pixels become white and vice versa.
    """
    input.data = 255 - input.data
    return input

def channelCrop(input: Channel, p1, p2) -> Channel:
    input.data = input.data[:, p1[1]:p2[1], p1[0]:p2[0]]
    return input

class cv_Interpolation(enum.Enum):
    nearest = cv2.INTER_NEAREST
    bilinear = cv2.INTER_LINEAR
    bicubic = cv2.INTER_CUBIC
    area = cv2.INTER_AREA
    lanczos4 = cv2.INTER_LANCZOS4

def channelRotate(input: Channel, degrees: float, inter: cv_Interpolation=cv_Interpolation.bilinear) -> Channel:    
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
        new_data[i] = cv2.warpAffine(input.data[i], rot, (b_w, b_h), flags=inter.value)
    
    input.data = new_data
    return input

def channelRotateType(input: Channel, rotType) -> Channel:
    if rotType == cv2.ROTATE_180:
        new_data = np.zeros(shape=input.shape, dtype=np.int32)
    else:
        new_data = np.zeros(shape=(input.shape[0], input.shape[2], input.shape[1]), dtype=np.int32)
    
    for i in range(input.shape[0]):
        new_data[i] = cv2.rotate(input.data[i], rotType)
    input.data = new_data
    return input

def channelRotate90(input: Channel) -> Channel:
    channelRotateType(input, cv2.ROTATE_90_CLOCKWISE)
    return input

def channelRotate180(input: Channel) -> Channel:
    channelRotateType(input, cv2.ROTATE_180)
    return input

def channelRotate270(input: Channel) -> Channel:
    channelRotateType(input, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return input
    
def channelFlipHorizontally(input: Channel) -> Channel:
    for i in range(input.shape[0]):
        input.data[i] = cv2.flip(input.data[i], 1)
    return input

def channelFlipVertically(input: Channel) -> Channel:
    for i in range(input.shape[0]):
        input.data[i] = cv2.flip(input.data[i], 0)
    return input

def pixelIntensity(input: Channel, frameId: int=-1) -> Channel:
    if frameId < 0:
        data = input.data
    else:
        data = input.data[frameId]    
    
    px_intensity = np.zeros(shape=(256), dtype=np.int32)
    
    for px in data:
        px_intensity[px] += 1
    
    return px_intensity

def zProjectionMax(input: Channel) -> Channel:
    return input.data.max(0)

def zProjectionMean(input: Channel) -> Channel:
    return input.data.mean(0)

def zProjectionMin(input: Channel) -> Channel:
    return input.data.min(0)


# TODO: Verify types of the channels to be Channel
def operatorAND(input: Channels, threshold: int=1) -> Channel:
    result = input[0].copy()
    for channel in input:
        result.data = np.where(channel.data >= threshold, result.data, 0)
    return result

def operatorOR(input: Channels) -> Channel:
    datas = input.data
    for channel in input:
        datas.append(channel.data)
    return input[0].clone(np.maximum.reduce(datas))

def operatorADD(input: Channels) -> Channel:
    result = input[0].copy()
    result.data = result.data.astype(np.uint16)
    for channel in input:
        result.data += channel.data
    result.data = result.data.clip(0, 255)
    result.data = result.data.astype(np.uint8)
    return result

def operatorSUB(input1: Channel, input2: Channel) -> Channel:
    result = input1.copy()
    result.data = result.data.astype(np.int16)
    result.data -= input2.data
    result.data = result.data.clip(0, 255)
    result.data = result.data.astype(np.uint8)
    return result

def changeBrightnessAndContrast(input: Channel, brightness: int, contrast: int) -> Channel:
    def contrastFactor(c):
        return (259*(c + 255)) / (255*(259 - c))

    factor = contrastFactor(contrast)
    
    data = input.data.astype(np.float16)
    
    data += brightness
    data = factor*(data - 128) + 128
 
    input.data = data.clip(0, 255).astype(np.uint8)
    return input

avg_counter = 0
def averageChannels(input: Channels) -> Channel:
    global avg_counter
    avg_counter += 1
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
    res.name = "Average_" + str(avg_counter)
    
    return res

def clipChannel(input: Channel, tmin: int=0, tmax: int=255, replace: bool=False) -> Channel:
    if not replace:
        input = input.copy()
    input.data[input.data < tmin] = 0
    input.data[input.data > tmax] = 0
    return input

def consensusSelection(input: Channels, amount: int=1) -> Channel:
    return clipChannel(averageChannels(input), amount/len(input) * 255, 255)
  
def resliceTop(input: Channel) -> Channel:      
    input = input.copy()  
    Z, Y, X = input.shape
    
    reslice = np.swapaxes(input.data, 0, 1) # (Z, Y, X) -> (Y, Z, X)
    reslice = reslice.astype(np.float64)
    
    new_Z = Z * input.px_sizes.Z / input.px_sizes.Y
    new_Z = int(new_Z)
    
    result = np.zeros((Y, new_Z, X))
    
    for i in range(Y):
        result[i, :, :] =  cv2.resize(reslice[i], (X, new_Z), interpolation=cv2.INTER_CUBIC)
    
    input.name = "reslicedTop_" + input.name
    input.data = result.astype(np.uint8)
    
    return input


def resliceLeft(input: Channel) -> Channel:
    input = input.copy()
    Z, Y, X = input.shape
    
    reslice = np.swapaxes(input.data, 0, 2) # (Z, Y, X) -> (X, Y, Z)
    reslice = np.swapaxes(reslice, 1, 2) # (X, Y, Z) -> (X, Z, Y)
    reslice = reslice.astype(np.float64)
    
    new_Z = Z * input.px_sizes.Z / input.px_sizes.X
    new_Z = int(new_Z)
    
    result = np.zeros((X, new_Z, Y))
    
    for i in range(X):
        result[i, :, :] =  cv2.resize(reslice[i], (Y, new_Z), interpolation=cv2.INTER_CUBIC)
        
    input.name = "reslicedLeft_" + input.name
    input.data = result.astype(np.uint8)
    
    return input

def channelReverse(input: Channel) -> Channel:
    input.data = input.data[::-1]
    return input

def sliceVolume(data, s_z, s_y, s_x, threshold=0):
    return np.count_nonzero(data[data >= threshold]) * s_z * s_y * s_x

def channelTotalVolume(input: Channel, minObjSize: int=0) -> NamedArray:
    l, n = ndimage.label(input.data, np.ones((3, 3, 3)))
    
    f = ndimage.find_objects(l)
    
    count = []
    
    for i in range(len(f)):
        count.append(np.count_nonzero(l[f[i]] == i+1))
    count = np.array(count)
    
    res = NamedArray()
    res.name = input.name
    res.data = count[count >= minObjSize].sum() * input.px_sizes.Z * input.px_sizes.Y * input.px_sizes.X
    res.data = [res.data]
    
    return res

def channelVolumeArray(input: Channel) -> NamedArray:
    z, y, x = input.shape
    
    volumes = []
    
    for i in range(z):
        volumes.append(sliceVolume(input.data[i], input.px_sizes.Z, input.px_sizes.Y, input.px_sizes.X))
    
    res = NamedArray()
    res.name = "AxisQuantif_" + input.name
    res.data = volumes
    return res

def channelAxisQuantification(input: Channel) -> NamedArray:
    axisFront = channelVolumeArray(input)
    axisTop = channelVolumeArray(resliceTop(input))
    axisLeft = channelVolumeArray(resliceLeft(input))
    
    return [axisFront, axisTop, axisLeft]

def meshCompareDistance(mesh1: Mesh, mesh2: Mesh, largest_region: bool=False) -> NamedArray:
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
        obj1 = mesh1.rotateY(90).extractLargestRegion()
        obj2 = mesh2.rotateY(90).extractLargestRegion() 
    else:
        obj1 = mesh1.rotateY(90)
        obj2 = mesh2.rotateY(90)
    
    obj1.distanceTo(obj2, signed=True)
    obj1.cmap(input_array="Distance", cname=lut)
    obj1.addScalarBar(title='Distance')
    
    vedo.show(obj1, new=True)
    
    return obj1.pointdata["Distance"]

def _meshCompareDistance_fiji(mesh1, mesh2):
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

def channelFromBinary(input: Channel) -> Channel:
    input.data[input.data > 0] = 255
    return input

_jar_path = 'C:/Users/PC/source/DAMAKER/damaker/weka/bin/weka_segmentation_gateway.jar'
def segmentation(input: Channel, classifier: StrFilePath) -> Channel:
    input = input.copy()
    # process = subprocess.Pope
    # n("java -Xms200M -Xmx8G -jar " + _jar_path)
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
    
    input.name = classifier.split("/")[-1].split(".")[0] + "_" + input.name
    
    gateway.shutdown()
    
    return input

def segmentationMultiClassifier(input: Channel, classifiers: BatchParameters, outputDir: StrFolderPath):
    classifiers.load()
    print(classifiers.fileList)
    for file in classifiers.fileList:
        segmentation(input, classifiers.folder + "/" + file).save(outputDir)

def resampleChannel(input: Channel, sizeX: int, sizeY: int, sizeZ: int, px_sizeX: int, px_sizeY: int, px_sizeZ: int) -> Channel:
    arr = sitk.GetImageFromArray(input.data.astype(np.float32))
    arr.SetSpacing(tuple(reversed(input.px_sizes)))
    
    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetOutputSpacing((px_sizeX, px_sizeY, px_sizeZ))
    flt.SetSize((sizeX, sizeY, sizeZ))
    
    input.data = sitk.GetArrayFromImage(flt.Execute(arr))
    input.px_sizes = PhysicalPixelSizes(px_sizeZ, px_sizeY, px_sizeX)
    return input

def resampleLike(input: Channel, ref: Channel) -> Channel:
    arr = sitk.GetImageFromArray(input.data.astype(np.float32))
    arr.SetSpacing(tuple(reversed(input.px_sizes)))
    
    ref_arr = sitk.GetImageFromArray(ref.data.astype(np.float32))
    ref_arr.SetSpacing(tuple(reversed(ref.px_sizes)))
    
    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetReferenceImage(ref_arr)
    
    input.data = sitk.GetArrayFromImage(flt.Execute(arr))
    return input

def resampleMean(input: Channels) -> Channel:
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

def _channelToImage(chn):
    ret = sitk.GetImageFromArray(chn.data.astype(np.float32))
    ret.SetSpacing(tuple(reversed(chn.px_sizes)))
    return ret

def _imageToChannel(img, chn=None):
    if chn == None:
        chn = Channel("reg")      
    chn.data = sitk.GetArrayFromImage(img)
    chn.data = chn.data.astype(np.uint8)
    res_px = img.GetSpacing()
    chn.px_sizes = PhysicalPixelSizes(res_px[2], res_px[1], res_px[0])
    return chn
        
def registration(input: Channel, reference: SingleChannel, nb_iteration: int=200, retTransform=None) -> Channel:            
    def resample(image, transform):
        reference_image = image
        interpolator = sitk.sitkLinear
        default_value = 0.0
        return sitk.Resample(image, reference_image, transform, interpolator, default_value)

    def _plotImage(img):
        plotChannel(Channel("", sitk.GetArrayFromImage(img)))

    ref = _channelToImage(reference)

    mov =  _channelToImage(input)
    
    flt = sitk.ResampleImageFilter()
    flt.SetReferenceImage(ref)
    mov = flt.Execute(mov)

    initial_transform = sitk.CenteredTransformInitializer(
        ref,
        mov,
        sitk.Euler3DTransform(),
        sitk.CenteredTransformInitializerFilter.GEOMETRY
    )

    registration_method = sitk.ImageRegistrationMethod()

    # Similarity metric settings.
    registration_method.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)
    registration_method.SetMetricSamplingStrategy(registration_method.RANDOM)
    registration_method.SetMetricSamplingPercentage(0.01)
    registration_method.SetInterpolator(sitk.sitkLinear)
    
    # registration_method.SetOptimizerAsExhaustive(numberOfSteps=[0,1,1,0,0,0], stepLength = np.pi)
    # registration_method.SetOptimizerScales([1,1,1,1,1,1])

    # Optimizer settings.
    registration_method.SetOptimizerAsGradientDescent(
        learningRate=1.0,
        numberOfIterations=nb_iteration,
        convergenceMinimumValue=1e-6,
        convergenceWindowSize=10,
    )
    registration_method.SetOptimizerScalesFromPhysicalShift()

    # Setup for the multi-resolution framework.
    registration_method.SetShrinkFactorsPerLevel(shrinkFactors=[4, 2, 1])
    registration_method.SetSmoothingSigmasPerLevel(smoothingSigmas=[2, 1, 0])
    registration_method.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()

    registration_method.SetInitialTransform(initial_transform, inPlace=False)
    # registration_method.SetInitialTransform(initial_transform, inPlace=True)

    final_transform = registration_method.Execute(
        ref, mov
    )
    

    print(f'Final metric value: {registration_method.GetMetricValue()}')
    print(
        f'Optimizer stopping condition, {registration_method.GetOptimizerStopConditionDescription()}'
    )
    
    if retTransform == True:
        return final_transform

    mov_res: sitk.Image = sitk.Resample(
        mov,
        ref,
        final_transform,
        sitk.sitkLinear,
        0.0,
        mov.GetPixelID(),
    )
    
    # reference.data = sitk.GetArrayFromImage(ref)
    input = _imageToChannel(mov_res, input)
    
    print(f'registration complete: {input}')
    return input

def registrationMultiChannel(input: BatchParameters, reference: SingleChannel, refChannel: int=1, nb_iteration: int=200, outputPath: StrFolderPath="") -> None:
    input.load()
    ref = _channelToImage(reference[0])
    
    while not input.finished():
        channels = input.next()
        final_transform = None
        for chn in channels:
            if chn.id == refChannel:
                final_transform = registration(chn, reference[0], retTransform=True)
                break
        if final_transform == None:
            print("No suitable channel found")
            continue
        
        final = []
        for chn in channels:
            mov = sitk.GetImageFromArray(chn.data.astype(np.float32))
            mov.SetSpacing(tuple(reversed(chn.px_sizes)))
            mov_res: sitk.Image = sitk.Resample(
                mov,
                ref,
                final_transform,
                sitk.sitkLinear,
                0.0,
                mov.GetPixelID(),
            )
            
            final.append(_imageToChannel(mov_res, chn))
        channelsSave(final, outputPath)