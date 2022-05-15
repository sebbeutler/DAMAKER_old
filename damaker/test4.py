import sys
sys.path.insert(0, '../')

from damaker.utils import *
from damaker.processing import *
from vedo import *
from pipeline import *

import SimpleITK as sitk
import matplotlib.pyplot as plt

chns = loadChannels("../resources/E1.tif")

lut_red = np.zeros((256, 3), np.uint8)
lut_red[:, 0] = np.arange(256)

lut_green = np.zeros((256, 3), np.uint8)
lut_green[:, 1] = np.arange(256)

lut_blue = np.zeros((256, 3), np.uint8)
lut_blue[:, 2] = np.arange(256)

luts = [lut_red, lut_green, lut_blue]

frame = np.zeros((chns[0].shape[1],chns[0].shape[2], 3), np.int32)
frame_id = 55

for chn in chns:
    if chn.lut is None:
        chn.lut = luts[chn.id]
    frame[:, :, 0] += chn.lut[:, 0][chn.data[frame_id]]
    frame[:, :, 1] += chn.lut[:, 1][chn.data[frame_id]]
    frame[:, :, 2] += chn.lut[:, 2][chn.data[frame_id]] 
frame = frame.clip(0, 255)

plotFrame(frame)
