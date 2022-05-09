from utils import *
from processing import *
from vedo import *
from pipeline import *

import SimpleITK as sitk
import matplotlib.pyplot as plt

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

chn1.data = sitk.GetArrayFromImage(ref)
chn2.data = sitk.GetArrayFromImage(mov)

plotChannelRGB(chn1, chn2)
