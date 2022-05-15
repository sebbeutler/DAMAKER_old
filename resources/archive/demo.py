from pipeline import *
from processing import *
from utils import *

import folderPicker

import os
import re
import gc

"""
- invert
- crop
- rotate
- rotate90
- rotate180
- rotate270
- flipHorizontally
- flipVertically
- pixelIntensity
- zProjectionMax
- zProjectionMean
- zProjectionMin
- operatorAND
- operatorOR
- operatorADD
- operatorSUB
- changeBrightnessAndContrast
- averageChannels
- thresholdChannel
- resliceTop
- resliceLeft
- reverseChannel
- channelTotalVolume
- channelVolumeArray
- meshCompareDistance
- 
- selectChannel
- openTiff_hybrid
- saveChannels
- channelSaveToObj
- listSaveCSV
- loadChannelssFromDir
- 
- plotChannel
- plotChannelRGB
- plotArray
- plotMesh
- 
- pipeline
"""


output_dir = "result/"
input_dir = "../resources/batch/"

# intput_dir = folderPicker.getFolder("Input folder:") + "/"
# output_dir = folderPicker.getFolder("Output folder:") + "/"

pipeline = Pipeline()

pipeline.add(print, "1: Creating output folder")
etape1 = pipeline.add(createDirectory, output_dir)

pipeline.add(print, "2: Loading files")
step2_E1 = pipeline.add(loadChannelssFromDir, input_dir, "E1.tif")
step2_E2 = pipeline.add(loadChannelssFromDir, input_dir, "E2.tif")
step2_E3 = pipeline.add(loadChannelssFromDir, input_dir, "E3.tif")
step2_E4 = pipeline.add(loadChannelssFromDir, input_dir, "E4.tif")
step2_E5 = pipeline.add(loadChannelssFromDir, input_dir, "E5.tif")

pipeline.add(print, "3: Averaging")
step3_E1 = pipeline.add(averageChannels, step2_E1)
step3_E2 = pipeline.add(averageChannels, step2_E2)
step3_E3 = pipeline.add(averageChannels, step2_E3)
step3_E4 = pipeline.add(averageChannels, step2_E4)
step3_E5 = pipeline.add(averageChannels, step2_E5)

# pipeline.add(plotChannel, step3_E1)

pipeline.add(print, "4: Apply threshold")
step4_E1 = pipeline.add(thresholdChannelLevel, step3_E1, 5, 5)
step4_E2 = pipeline.add(thresholdChannelLevel, step3_E2, 5, 5)
step4_E3 = pipeline.add(thresholdChannelLevel, step3_E3, 5, 5)
step4_E4 = pipeline.add(thresholdChannelLevel, step3_E4, 5, 5)
step4_E5 = pipeline.add(thresholdChannelLevel, step3_E5, 5, 5)

# pipeline.add(plotChannel, step4_E1)

# pipeline.add(print, "5: Quantification - Total volume")
# step5_E1 = pipeline.add(channelTotalVolume, step4_E1)
# step5_E2 = pipeline.add(channelTotalVolume, step4_E2)
# step5_E3 = pipeline.add(channelTotalVolume, step4_E3)
# step5_E4 = pipeline.add(channelTotalVolume, step4_E4)
# step5_E5 = pipeline.add(channelTotalVolume, step4_E5)

# pipeline.add(print, "E1: ", step5_E1)
# pipeline.add(print, "E2: ", step5_E2)
# pipeline.add(print, "E3: ", step5_E3)
# pipeline.add(print, "E4: ", step5_E4)
# pipeline.add(print, "E5: ", step5_E5)

# pipeline.add(print, "6: Quantification - Per axis volume")
# step6_E1 = pipeline.add(channelAxisQuantification, step4_E1)
# step6_E2 = pipeline.add(channelAxisQuantification, step4_E2)
# step6_E3 = pipeline.add(channelAxisQuantification, step4_E3)
# step6_E4 = pipeline.add(channelAxisQuantification, step4_E4)
# step6_E5 = pipeline.add(channelAxisQuantification, step4_E5)

# pipeline.add(print, "7: Quantification - Save as spreadsheet")
# pipeline.add(listSaveCSV, [step5_E1], output_dir, "E1_volume.csv")
# pipeline.add(listSaveCSV, [step5_E2], output_dir, "E2_volume.csv")
# pipeline.add(listSaveCSV, [step5_E3], output_dir, "E3_volume.csv")
# pipeline.add(listSaveCSV, [step5_E4], output_dir, "E4_volume.csv")
# pipeline.add(listSaveCSV, [step5_E5], output_dir, "E5_volume.csv")

# pipeline.add(axisQuantifSaveCSV, step6_E1, output_dir, "E1_axis")
# pipeline.add(axisQuantifSaveCSV, step6_E2, output_dir, "E2_axis")
# pipeline.add(axisQuantifSaveCSV, step6_E3, output_dir, "E3_axis")
# pipeline.add(axisQuantifSaveCSV, step6_E4, output_dir, "E4_axis")
# pipeline.add(axisQuantifSaveCSV, step6_E5, output_dir, "E5_axis")

# pipeline.add(print, "8: Quantification - Plot")
# pipeline.add(plotAxisQuantifications, [step6_E1, step6_E2, step6_E3, step6_E4, step6_E5], ["E1", "E2", "E3", "E4", "E5"], "Volume per axis")

pipeline.add(print, "9: Average between samples")
step9 = pipeline.add(averageChannels, [step4_E1, step4_E2, step4_E3, step4_E4, step4_E5])

# pipeline.add(plotChannel, step9)

pipeline.add(print, "10: Thresholding")
step10_th5 = pipeline.add(thresholdChannelLevel, step9, 5, 5, False)
step10_th4 = pipeline.add(thresholdChannelLevel, step9, 5, 4, False)

pipeline.add(channelSave, step10_th4, "th4.tif")
pipeline.add(channelSave, step10_th5, "th5.tif")

# pipeline.add(plotChannel, step10_th4)
# pipeline.add(plotChannel, step10_th5)

# pipeline.add(print, "11: Export -> .obj")
# pipeline.add(channelSaveToObj, step10_th5, output_dir + "average_th5.obj", 1)
# pipeline.add(channelSaveToObj, step10_th4, output_dir + "average_th4.obj", 1)

# pipeline.add(print, "12: Tissue shape")
# pipeline.add(meshCompareDistance, output_dir + "average_th4.obj", output_dir + "average_th5.obj")

pipeline.run()