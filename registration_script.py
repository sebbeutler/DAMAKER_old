from damaker.utils import *
from damaker.pipeline import *

import SimpleITK as sitk

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
        
def registration_opt(input: Channel, reference: SingleChannel) -> Channel:            
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
    registration_method.SetMetricSamplingStrategy(registration_method.NONE)
    registration_method.SetMetricSamplingPercentage(0.01)
    registration_method.SetInterpolator(sitk.sitkLinear)
    
    # registration_method.SetOptimizerAsExhaustive(numberOfSteps=[0,1,1,0,0,0], stepLength = np.pi)
    # registration_method.SetOptimizerScales([1,1,1,1,1,1])

    # Optimizer settings.
    registration_method.SetOptimizerAsGradientDescent(
        learningRate=1.0,
        numberOfIterations=200,
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
    
    # if retTransform == True:
    #     return final_transform

    # mov_res: sitk.Image = sitk.Resample(
    #     mov,
    #     ref,
    #     final_transform,
    #     sitk.sitkLinear,
    #     0.0,
    #     mov.GetPixelID(),
    # )
    
    # # reference.data = sitk.GetArrayFromImage(ref)
    # input = _imageToChannel(mov_res, input)
    
    # print(f'registration complete: {input}')
    # return input

if __name__ == '__main__':
    chn = loadChannelsFromFile("resources/batch/E1.tif")[0]
    ref = loadChannelsFromFile("resources/registration/E0_C1.tif")[0]
    registration_opt(chn, ref)