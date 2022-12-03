import enum
import math
import os

import cv2
import numpy as np
import pandas as pd
import SimpleITK as sitk
import vedo
from scipy import ndimage
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from vedo import Mesh

import damaker
import damaker.utils as utils

from .dmktypes import *
from .ImageStack import *


def _foo() -> None:
    """
        Name: Foo
        Category: Bar
        Desc: .
    """
    return None

# TODO: Uses ?
def channelSelect(input: ImageStack, id: int=1) -> ImageStack:
    """
        Name: Select channel by id
        Category: Import
        Desc: Choose a specific channel among the inputs.
    """
    channels = []
    for channel in input:
        if channel.id == id:
            channels.append(channel)
    if len(channels) == 0:
        print(f"channelSelect: no channels with id={id}")
    return channels

@damaker.operation(alias='Invert colors')
def channelInvert(input: ImageStack) -> ImageStack:
    """
        Name: Invert colors
        Category: Transform
        Desc: Every black pixels become white and vice versa.
    """
    if input.format == np.uint8:
        input.data = 255 - input.data
    else:
        raise damaker.FormatMismatchException()

    return input

# def channelCrop(input: ImageStack, x1: int, y1: int, x2: int, y2: int) -> ImageStack:
#     """
#         Name: Crop
#         Category: Transform
#     """
#     input.data = input.data[:, y1:y2, x1:x2]
#     return input

def channelCrop(input: ImageStack, target: utils.Rect) -> ImageStack:
    """
        Name: Crop
        Category: Transform
    """
    input.data = input.data[:, target.pos.y:target.size.y, target.pos.x:target.size.x]
    return input

class cv_Interpolation(enum.Enum):
    nearest = cv2.INTER_NEAREST
    bilinear = cv2.INTER_LINEAR
    bicubic = cv2.INTER_CUBIC
    area = cv2.INTER_AREA
    lanczos4 = cv2.INTER_LANCZOS4

@damaker.operation(alias='Rotate angle', ndim=3)
def channelRotate(input: ImageStack, degrees: float, inter: cv_Interpolation=cv_Interpolation.bilinear) -> ImageStack:
    """
        Name: Rotation angle
        Category: Transform
    """
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

    input.data = new_data.astype(np.uint8)
    return input

class RotationTypes(enum.Enum):
    clockwise_90 =  cv2.ROTATE_90_CLOCKWISE
    counter_clockwise_90 = cv2.ROTATE_90_COUNTERCLOCKWISE
    rotate_180 = cv2.ROTATE_180

@damaker.operation(alias='Rotation', ndim=3)
def channelRotateType(input: ImageStack, rotType: RotationTypes=RotationTypes.clockwise_90) -> ImageStack:
    """
        Name: Rotation
        Category: Transform
    """
    if rotType.value == cv2.ROTATE_180:
        new_data = np.zeros(shape=input.shape, dtype=np.int32)
    else:
        new_data = np.zeros(shape=(input.shape[0], input.shape[2], input.shape[1]), dtype=np.int32)

    for i in range(input.shape[0]):
        new_data[i] = cv2.rotate(input.data[i], rotType.value)
    input.data = new_data.astype(np.uint8)

    return input

class FlipTypes(enum.Enum):
    vertically = 0
    horizontally = 1

@damaker.operation(alias='Flip', ndim=3)
def channelFlip(input: ImageStack, flipType: FlipTypes=FlipTypes.horizontally) -> ImageStack:
    """
        Name: Flip
        Category: Transform
    """
    for i in range(input.shape[0]):
        input.data[i] = cv2.flip(input.data[i], flipType.value)
    return input

# TODO: Test this shit
@damaker.operation(alias='Flip', ndim=[2,3])
def pixelIntensity(input: ImageStack, frameId: int=-1) -> pd.DataFrame:
    """
        Name: Pixel intensity
        Category: Quantification
    """
    if frameId < 0:
        data = input.data
    else:
        data = input.data[frameId]

    px_intensity = np.zeros(shape=(256), dtype=np.int32)

    for px in data:
        px_intensity[px] += 1

    output = pd.DataFrame(px_intensity)
    print(output.Name)
    return output

def _framePixelIntensity(input: np.ndarray):
    return pixelIntensity(ImageStack(data=[input]), 0)

class ZProjectionTypes(enum.Enum):
    max = 0
    min = 1
    mean = 2

@damaker.operation(alias='Z Projection', category='Process', ndim=3)
def channelZProjection(input: ImageStack, projectionType: ZProjectionTypes=ZProjectionTypes.max) -> ImageStack:
    """
        Name: Z Projection
        Category: Process
    """
    if projectionType == ZProjectionTypes.max:
        return input.clone(input.data.max(0)[np.newaxis])
    elif projectionType == ZProjectionTypes.min:
        return input.clone(input.data.min(0)[np.newaxis])
    elif projectionType == ZProjectionTypes.mean:
        return input.clone(input.data.mean(0)[np.newaxis])


# TODO: Verify types of the channels to be ImageStack

class MathOperationTypes(enum.Enum):
    AND = 0
    OR = 1
    ADD = 2
    SUB = 3

@damaker.operation(alias='Math', category='Process')
def mathOperators(input1: ImageStack, input2: ImageStack, opType: MathOperationTypes=MathOperationTypes.SUB) -> ImageStack:
    """
        Name: Math
        Category: Process
    """
    inputs = [input1, input2]
    if opType == MathOperationTypes.ADD:
        return _operatorADD(inputs)
    elif opType == MathOperationTypes.AND:
        return _operatorAND(inputs)
    elif opType == MathOperationTypes.OR:
        return _operatorOR(inputs)
    elif opType == MathOperationTypes.SUB:
        return _operatorSUB(inputs)

def _operatorAND(input: list[ImageStack], threshold: int=1) -> ImageStack:
    if len(input) == 0:
        raise damaker.LengthMismatchException()

    output: ImageStack = input[0].copy()
    for stack in input:
        output.data = np.where(stack.data >= threshold, output.data, 0)
    return output

def _operatorOR(input: list[ImageStack]) -> ImageStack:
    if len(input) == 0:
        raise damaker.LengthMismatchException()

    stacks = []
    for stack in input:
        stacks.append(stack)

    output: ImageStack = input[0].copy(np.maximum.reduce(stacks))
    return output

def _operatorADD(input: list[ImageStack]) -> ImageStack:
    if len(input) == 0:
        raise damaker.LengthMismatchException()
    if input[0].format != np.uint8:
        raise damaker.FormatMismatchException()

    output = input[0].copy()
    output.data = output.data.astype(np.uint16)
    for stack in input:
        output.data += stack.data
    output.data = output.data.clip(0, 255)
    output.data = output.data.astype(np.uint8)
    return output

def _operatorSUB(input: ImageStack) -> ImageStack:
    if len(input) == 0:
        raise damaker.LengthMismatchException()
    if input[0].format != np.uint8:
        raise damaker.FormatMismatchException()

    output = input[0].copy()
    output.data = output.data.astype(np.uint16)
    for stack in input:
        output.data -= stack.data
    output.data = output.data.clip(0, 255)
    output.data = output.data.astype(np.uint8)
    return output

@damaker.operation(alias='Brightness & Contrast', category='Transform')
def changeBrightnessAndContrast(input: ImageStack, brightness: int, contrast: int) -> ImageStack:
    """
        Name: Brightness & Contrast
        Category: Transform
    """
    if input.format != np.uint8:
        raise damaker.FormatMismatchException()

    def contrastFactor(c):
        return (259*(c + 255)) / (255*(259 - c))

    factor = contrastFactor(contrast)

    data = input.data.astype(np.float16)

    data = factor*((data + brightness) - 128) + 128

    input.data = data.clip(0, 255).astype(np.uint8)
    return input

# TODO: ??
def _changeFrameBrightnessAndContrast(frame: np.ndarray, brightness: int, contrast: int):
    """
        Name: Brightness & Contrast
        Category: Transform
    """
    def contrastFactor(c):
        return (259*(c + 255)) / (255*(259 - c))

    factor = contrastFactor(contrast)

    data = frame.astype(np.float16)

    data += brightness
    data = factor*(data - 128) + 128

    frame = data.clip(0, 255).astype(np.uint8)
    return frame

avg_counter = 0
def _resetAvg():
    global avg_counter
    avg_counter = 0

@damaker.operation(alias='Mean', category='Process')
def averageImageStack(input: list[ImageStack], consensusSelection: int=0) -> ImageStack:
    """
        Name: Mean
        Category: Process
    """
    global avg_counter
    avg_counter += 1

    if len(input) == 0:
        raise damaker.LengthMismatchException()

    stacks: list[ImageStack] = []

    reference = input[0]
    shape = reference.shape
    pixelsize = reference.get('pixelsize')
    name = 'Mean'
    for stack in input:
        if shape != stack.shape:
            raise damaker.ShapeMismatchException()
        if stack.format != np.uint8:
            raise damaker.FormatMismatchException()
        if stack.get('pixelsize') != None and stack.get('pixelsize') != pixelsize:
            print(f"[Warning]: Pixel size of '{stack.get('filepath')}' does not match the reference size (X:{pixelsize.X}, Y:{pixelsize.Y},Z:{pixelsize.Z})")

        name += f"_{os.path.basename(stack.get('filepath')).split('.')[0]}"
        stacks.append(stack.data)
    name += '.tif'

    stacks = np.array(stacks, dtype=np.float32)

    output: ImageStack = input[0].clone(stacks.mean(0).astype(np.uint8))
    output.set('filepath', name)

    if consensusSelection > 0:
        output = clipImageStack(output, consensusSelection/len(input) * 255, 255)

    return output

@damaker.operation(alias='Clip intensity', category='Transform')
def clipImageStack(input: ImageStack, tmin: int=0, tmax: int=255) -> ImageStack:
    """
        Name: Clip intensity
        Category: Transform
    """
    input.data[input.data < tmin] = 0
    input.data[input.data > tmax] = 0
    return input

class ResliceType(enum.Enum):
    top = 0
    bottom = 1
    left = 2
    right = 3

# TODO: Review reslice if too slow
@damaker.operation(alias='Reslice', category='Process', ndim=3)
def resliceChannel(input: ImageStack, resliceType: ResliceType=ResliceType.top) -> ImageStack:
    """
        Name: Reslice
        Category: Process
    """
    if resliceType == ResliceType.top:
        return _channelResliceTop(input)
    elif resliceType == ResliceType.bottom:
        return channelReverse(_channelResliceTop(input))
    elif resliceType == ResliceType.left:
        return _channelResliceLeft(input)
    elif resliceType == ResliceType.right:
        return channelReverse(_channelResliceLeft(input))

def _channelResliceTop(input: ImageStack) -> ImageStack:
    if input.ndim != 3:
        raise damaker.DimensionCountMismatchException()

    Z, Y, X = input.shape

    reslice = np.swapaxes(output.data, 0, 1) # (Z, Y, X) -> (Y, Z, X)
    reslice = reslice.astype(np.float64)

    new_Z = Z * output.px_sizes.Z / output.px_sizes.Y
    new_Z = int(new_Z)

    result = np.zeros((Y, new_Z, X))

    try:
        for i in range(Y):
            result[i, :, :] =  cv2.resize(reslice[i], (X, new_Z), interpolation=cv2.INTER_NEAREST)
    except:
        return input

    output: ImageStack = input.copy(result.astype(np.uint8))
    output.set('pixelsize', PixelSize(input.px_sizes.Y, input.px_sizes.Y, input.px_sizes.X))
    output.set('filepath', "reslicedTop_" + input.metadata.basename())

    return input

def _channelResliceLeft(input: ImageStack) -> ImageStack:
    if input.ndim != 3:
        raise damaker.DimensionCountMismatchException()

    Z, Y, X = input.shape

    reslice = np.swapaxes(input.data, 0, 2) # (Z, Y, X) -> (X, Y, Z)
    reslice = np.swapaxes(reslice, 1, 2) # (X, Y, Z) -> (X, Z, Y)
    reslice = reslice.astype(np.float64)

    new_Z = Z * input.px_sizes.Z / input.px_sizes.X
    new_Z = int(new_Z)

    result = np.zeros((X, new_Z, Y))

    try:
        for i in range(X):
            result[i, :, :] =  cv2.resize(reslice[i], (Y, new_Z), interpolation=cv2.INTER_NEAREST)
    except:
        return input

    output: ImageStack = input.copy(result.astype(np.uint8))
    output.set('pixelsize', PixelSize(input.px_sizes.X, input.px_sizes.X, input.px_sizes.Y))
    output.set('filepath', "reslicedLeft_" + input.metadata.basename())

    return output

# TODO: reverse optional axis
@damaker.operation(alias='Reverse stack', category='Transform', ndim=3)
def channelReverse(input: ImageStack) -> ImageStack:
    """
        Name: Reverse stack
        Category: Transform
    """
    input.data = input.data[::-1]
    return input

def _sliceVolume(data, s_z, s_y, s_x, threshold=0):
    return np.count_nonzero(data[data >= threshold]) * s_z * s_y * s_x

@damaker.operation(alias='Volume', category='Quantification', ndim=3)
def channelTotalVolume(input: ImageStack, minObjSize: int=0) -> pd.DataFrame:
    """
        Name: Volume
        Category: Quantification
    """
    l, n = ndimage.label(input.data, np.ones((3, 3, 3)))

    f = ndimage.find_objects(l)

    count = []

    for i in range(len(f)):
        count.append(np.count_nonzero(l[f[i]] == i+1))
    count = np.array(count)

    output = pd.DataFrame(count[count >= minObjSize].sum() * input.px_sizes.Z * input.px_sizes.Y * input.px_sizes.X)
    output.Name = input.name
    return output

@damaker.operation(alias='Volume distribution', category='Quantification', ndim=3)
def channelVolumeArray(input: ImageStack) -> pd.DataFrame:
    """
        Name: Volume distribution
        Category: Quantification
    """
    z, y, x = input.shape

    volumes = []

    for i in range(z):
        volumes.append(_sliceVolume(input.data[i], input.px_sizes.Z, input.px_sizes.Y, input.px_sizes.X))

    output = pd.DataFrame(volumes)
    output.Name = "AxisQuantif_" + input.name
    return output

# TODO: combine pd.DataFrame
@damaker.operation(alias='Volume distribution per axis', category='Quantification', ndim=3)
def channelAxisQuantification(input: ImageStack, outputPath: utils.FolderPathStr) -> pd.DataFrame:
    """
        Name: Volume distribution per axis
        Category: Quantification
    """
    axisFront = channelVolumeArray(input)
    axisTop = channelVolumeArray(_channelResliceTop(input))
    axisLeft = channelVolumeArray(_channelResliceLeft(input))

    utils._axisQuantifSaveCSV([axisFront, axisTop, axisLeft], outputPath, input.name)

@damaker.operation(alias='Mesh distance', category='Quantification')
def meshCompareDistance(mesh1: Mesh, mesh2: Mesh, largest_region: bool=False) -> pd.DataFrame:
    """
        Name: Mesh distance
        Category: Quantification
    """
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

    output = pd.DataFrame(obj1.pointdata["Distance"])
    output.Name = f'MeshDistance_{mesh1.filename}_{mesh2.filename}'
    return output

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

# TODO: stack format converter
@damaker.operation(alias='Format converter', category='Import')
def channelFromBinary(input: ImageStack) -> ImageStack:
    """
        Name: Format converter
        Category: Import
    """
    input.data[input.data > 0] = 255
    return input

# _jar_path = 'C:/Users/PC/source/DAMAKER/damaker/weka/bin/weka_segmentation_gateway.jar'
# def segmentation(input: ImageStack, classifier: utils.FilePathStr) -> ImageStack:
#     """
#         Name: Apply Trainable Weka Segmentation 3D
#         Category: Segmentation
#     """
#     input = input.copy()
#     # process = subprocess.Pope
#     # n("java -Xms200M -Xmx8G -jar " + _jar_path)
#     gateway = JavaGateway()

#     z, y, x = input.shape
#     arr = bytes(input.data.flatten().tolist())
#     img = gateway.entry_point.numpyToImagePlus(arr, x, y, z)
#     segmented = gateway.entry_point.runSegmentation(img, os.path.abspath(classifier))

#     res = []
#     for frame in segmented:
#         res += frame
#     input.data = np.array(res).reshape(z, y, x)
#     channelFromBinary(input)

#     input.name = classifier.split("/")[-1].split(".")[0] + "_" + input.name

#     gateway.shutdown()

#     return input

# def segmentationMultiClassifier(input: ImageStack, classifiers: BatchParameters, outputDir: utils.FolderPathStr):
#     """
#         Name: Apply Trainable Weka Segmentation 3D (Multiple Classifiers)
#         Category: Segmentation
#     """
#     classifiers.load()
#     print(classifiers.fileList)
#     for file in classifiers.fileList:
#         segmentation(input, classifiers.folder + "/" + file).save(outputDir)

# TODO: Verify pixelsize when resampling
@damaker.operation(alias='Resample', category='Import', ndim=3)
def resampleImageStack(input: ImageStack, sizeX: int, sizeY: int, sizeZ: int) -> ImageStack:
    """
        Name: Resample
        Category: Import
    """
    print(f"{sizeX}, {sizeY}, {sizeZ}")
    arr = sitk.GetImageFromArray(input.data.astype(np.uint8))
    arr.SetSpacing(tuple(reversed(input.get('pixelsize'))))

    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    # flt.SetOutputSpacing((px_sizeX, px_sizeY, px_sizeZ))
    flt.SetSize((int(sizeX), int(sizeY), int(sizeZ)))

    input.data = sitk.GetArrayFromImage(flt.Execute(arr))
    # input.px_sizes = PhysicalPixelSize(px_sizeZ, px_sizeY, px_sizeX)
    return input

def _resamplePixelSize(input: ImageStack, x:float, y:float, z:float) -> ImageStack:
    pixelsize = input.get('pixelsize')
    arr = sitk.GetImageFromArray(input.data.astype(np.float32))
    arr.SetSpacing(tuple(reversed(pixelsize)))

    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetOutputSpacing((x, y, z))
    flt.SetSize((int(input.shape[2] * (x / pixelsize.X)), int(input.shape[1] * (y / pixelsize.Y)), int(input.shape[0] * (z / pixelsize.Z))))

    input.data = sitk.GetArrayFromImage(flt.Execute(arr))
    input.set('pixelsize', PixelSize(z, x, y))

    return input

@damaker.operation(alias='Homogenize with reference', category='Import', ndim=3)
def resampleLike(input: ImageStack, ref: ImageStack) -> ImageStack:
    """
        Name: Homogenize with reference
        Category: Import
    """
    arr = sitk.GetImageFromArray(input.data.astype(np.float32))
    arr.SetSpacing(tuple(reversed(input.get('pixelsize'))))

    ref_arr = sitk.GetImageFromArray(ref.data.astype(np.float32))
    ref_arr.SetSpacing(tuple(reversed(ref.get('pixelsize'))))

    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetReferenceImage(ref_arr)

    input.data = sitk.GetArrayFromImage(flt.Execute(arr))
    # ??
    return input

@damaker.operation(alias='Homogenize Mean', category='Import')
def resampleMean(input: ImageStack) -> ImageStack:
    """
        Name: Homogenize Mean
        Category: Import
    """
    shapes = []
    pixelsize = []
    for stack in input:
        shapes.append(stack.shape)
        pixelsize.append(tuple(stack.get('pixelsize')))

    shape = np.array(shapes).mean(0)
    px_size = np.array(pixelsize).mean(0)

    flt = sitk.ResampleImageFilter()
    flt.SetInterpolator(sitk.sitkLinear)
    flt.SetOutputSpacing(px_size[2], px_size[1], px_size[0])
    flt.SetSize(shape[2], shape[1], shape[0])

    for stack in input:
        resampleImageStack(stack, shape[2], shape[1], shape[0], px_size[2], px_size[1], px_size[0])

    return input

def _channelToImage(chn):
    ret = sitk.GetImageFromArray(chn.data.astype(np.float32))
    ret.SetSpacing(tuple(reversed(chn.pixelsize)))
    return ret

def _imageToImageStack(img, chn=None):
    if chn == None:
        chn = ImageStack("reg")
    chn.data = sitk.GetArrayFromImage(img)
    chn.data = chn.data.astype(np.uint8)
    res_px = img.GetSpacing()
    chn.pixelsize = PhysicalPixelSize(res_px[2], res_px[1], res_px[0])
    return chn

# def registration(input: ImageStack, reference: ImageStack, nb_iteration: int=200, retTransform=None) -> ImageStack:
#     """
#         Name: SITK Registration direct
#         Category: Registration
#     """
#     def resample(image, transform):
#         reference_image = image
#         interpolator = sitk.sitkLinear
#         default_value = 0.0
#         return sitk.Resample(image, reference_image, transform, interpolator, default_value)

#     def _plotImage(img):
#         utils._plotImageStack(ImageStack("", sitk.GetArrayFromImage(img)))

#     ref = _channelToImage(reference)

#     mov =  _channelToImage(input)

#     flt = sitk.ResampleImageFilter()
#     flt.SetReferenceImage(ref)
#     mov = flt.Execute(mov)

#     initial_transform = sitk.CenteredTransformInitializer(
#         ref,
#         mov,
#         sitk.Euler3DTransform(),
#         sitk.CenteredTransformInitializerFilter.GEOMETRY
#     )

#     registration_method = sitk.ImageRegistrationMethod()

#     # Similarity metric settings.
#     registration_method.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)
#     registration_method.SetMetricSamplingStrategy(registration_method.RANDOM)
#     registration_method.SetMetricSamplingPercentage(0.01)
#     registration_method.SetInterpolator(sitk.sitkLinear)

#     # registration_method.SetOptimizerAsExhaustive(numberOfSteps=[0,1,1,0,0,0], stepLength = np.pi)
#     # registration_method.SetOptimizerScales([1,1,1,1,1,1])

#     # Optimizer settings.
#     registration_method.SetOptimizerAsGradientDescent(
#         learningRate=1.0,
#         numberOfIterations=nb_iteration,
#         convergenceMinimumValue=1e-6,
#         convergenceWindowSize=10,
#     )
#     registration_method.SetOptimizerScalesFromPhysicalShift()

#     # Setup for the multi-resolution framework.
#     registration_method.SetShrinkFactorsPerLevel(shrinkFactors=[4, 2, 1])
#     registration_method.SetSmoothingSigmasPerLevel(smoothingSigmas=[2, 1, 0])
#     registration_method.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()

#     registration_method.SetInitialTransform(initial_transform, inPlace=False)
#     # registration_method.SetInitialTransform(initial_transform, inPlace=True)

#     final_transform = registration_method.Execute(
#         ref, mov
#     )


#     print(f'Final metric value: {registration_method.GetMetricValue()}')
#     print(
#         f'Optimizer stopping condition, {registration_method.GetOptimizerStopConditionDescription()}'
#     )

#     if retTransform == True:
#         return final_transform

#     mov_res: sitk.Image = sitk.Resample(
#         mov,
#         ref,
#         final_transform,
#         sitk.sitkLinear,
#         0.0,
#         mov.GetPixelID(),
#     )

#     # reference.data = sitk.GetArrayFromImage(ref)
#     input = _imageToImageStack(mov_res, input)

#     print(f'registration complete: {input}')
#     return input

# def registrationMultiImageStack(input: BatchParameters, reference: SingleImageStack, refImageStack: int=1, nb_iteration: int=200, outputPath: utils.FolderPathStr="") -> None:
#     """
#         Name: SITK Registration though reference
#         Category: Registration
#     """
#     input.load()
#     ref = _channelToImage(reference[0])

#     while not input.finished():
#         channels = input.next()
#         final_transform = None
#         for chn in channels:
#             if chn.id == refImageStack:
#                 final_transform = registration(chn, reference[0], retTransform=True)
#                 break
#         if final_transform == None:
#             print("No suitable channel found")
#             continue

#         final = []
#         for chn in channels:
#             mov = sitk.GetImageFromArray(chn.data.astype(np.float32))
#             mov.SetSpacing(tuple(reversed(chn.px_sizes)))
#             mov_res: sitk.Image = sitk.Resample(
#                 mov,
#                 ref,
#                 final_transform,
#                 sitk.sitkLinear,
#                 0.0,
#                 mov.GetPixelID(),
#             )

#             final.append(_imageToImageStack(mov_res, chn))
#         utils.channelsSave(final, outputPath)

@damaker.operation(alias='Erosion', category='Process')
def erosion(input: ImageStack, bool, iterations: int, border_value: int=0, brute_force: bool=False) -> ImageStack:
    input.data = ndimage.binary_erosion(input.data, None, iterations, None, None, border_value, 0, brute_force)
    return input

# scipy.ndimage.binary_dilation(input, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)[source]
@damaker.operation(alias='Dilatation', category='Process')
def dilation(input: ImageStack, iterations: int= 1, mask: ImageStack=None, border_value:int = 0, origin: int=0, brute_force: bool=False) -> ImageStack:
    input.data = ndimage.binary_dilation(input.data, None, iterations, mask, border_value, origin, brute_force)
    return input

@damaker.operation(alias='PCA', category='Quantification')
def dmk_PCA(input: pd.DataFrame, classes: list[str], features: list[str], n_components: int=6) -> pd.DataFrame:
    ## Data scaling

    x1 = input.loc[:, features].values
    y1 = input.loc[:, classes].values
    x1 = StandardScaler().fit_transform(x1)

    ## Perform PCA

    pca = PCA(n_components=n_components)
    principalComponents = pca.fit_transform(x1)
    principalDataframe = pd.DataFrame(
        data = principalComponents,
        columns = [f'PC{i}' for i in range(1, n_components+1)]
    )

    return pd.concat([principalDataframe, input[classes]], axis = 1)