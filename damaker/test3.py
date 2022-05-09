from utils import *
from processing import *
from vedo import *
from pipeline import *

import SimpleITK as sitk
import matplotlib.pyplot as plt

def resample(image, transform):
    reference_image = image
    interpolator = sitk.sitkLinear
    default_value = 0.0
    return sitk.Resample(image, reference_image, transform, interpolator, default_value)

def plotSITKImage(img):
    plotChannel(TiffChannel("", sitk.GetArrayFromImage(img)))

chn1 = openTiff_hybrid("../resources/registration/C1-E0.tif")[0]
ref = sitk.GetImageFromArray(chn1.data.astype(np.float32))
ref.SetSpacing(tuple(chn1.px_sizes))


chn2 = openTiff_hybrid("../resources/registration/C1-E1.tif")[0]
mov = sitk.GetImageFromArray(chn2.data.astype(np.float32))
mov.SetSpacing(tuple(chn2.px_sizes))


flt = sitk.ResampleImageFilter()
flt.SetInterpolator(sitk.sitkLinear)
flt.SetOutputSpacing(tuple(chn1.px_sizes))
flt.SetSize((
    int(chn1.px_sizes.X / chn2.px_sizes.X * chn2.shape[2]),
    int(chn1.px_sizes.Y / chn2.px_sizes.Y * chn2.shape[1]),
    int(chn1.px_sizes.Z / chn2.px_sizes.Z * chn2.shape[0])
    ))

ref = flt.Execute(ref)
mov = flt.Execute(mov)


initial_transform = sitk.CenteredTransformInitializer(
    ref,
    mov,
    sitk.Euler3DTransform(),
    sitk.CenteredTransformInitializerFilter.GEOMETRY
)

chn1.data = sitk.GetArrayFromImage(mov)

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
    numberOfIterations=100,
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


mov_res = sitk.Resample(
    mov,
    ref,
    final_transform,
    sitk.sitkLinear,
    0.0,
    mov.GetPixelID(),
)

chn1.data = sitk.GetArrayFromImage(ref)
chn2.data = sitk.GetArrayFromImage(mov_res)

plotChannelRGB(chn1, chn2)