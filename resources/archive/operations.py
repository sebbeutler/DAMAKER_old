from typing import Type
from webbrowser import Opera
from Channel import Channel, Frame

from abc import ABC, abstractmethod
import math

from utils import *

import cv2
import numpy as np
from scipy import ndimage

class OperationOutput:
    def __init__(self, data=None):
        self.output = data
    
    def get(self):
        return self.output

    def set(self, data):
        self.output = data

class Operation(ABC):
    def __init__(self, input: list[type], output: type):
        self.input_types = input
        self.output_type = output
        self.output = OperationOutput()
    
    @abstractmethod
    def run(self):
        pass
    
    def execute(operations: list):
        for op in operations:
            op.run()

class ChannelOperation(Operation):
    def __init__(self, input: list[type], output: type, channel: Channel):
        super().__init__(input, output)
        if type(channel) is OperationOutput:
            channel = channel.get()
        self.output.set(channel)
    
    @property
    def channel(self):
        return self.output.get()

class ChannelLoad(ChannelOperation):
    def __init__(self, filename: str, channel: int=0):
        super().__init__([str], Channel, Channel())
        self.filename = filename
        self.channel_id = channel
    
    def run(self):
        self.channel.copyFrom(loadChannel(self.filename)[self.channel_id])
        return self.channel

class ChannelInvert(ChannelOperation):
    def __init__(self, chn: Channel):
        super().__init__([Channel], Channel, chn)
    
    def run(self):
        self.channel.data = 255 - self.channel.data
        return self.channel

class ChannelCrop(ChannelOperation):
    def __init__(self, chn: Channel, x1: int, y1: int, x2: int, y2: int):
        super().__init__([Channel, int, int, int, int], Channel, chn)
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)
    
    def run(self):
        self.channel.data = self.channel.data[:, self.p1[1]:self.p2[1], self.p1[0]:self.p2[0]]
        return self.channel

class ChannelRotate(ChannelOperation):
    def __init__(self, chn: Channel, angle: float, interpolation: str="bicubic"):
        super().__init__([Channel, float, str], Channel, chn)
        self.angle = angle
        self.interploation = interpolation
    
    def run(self):
        interpolations = {
        "nearest": cv2.INTER_NEAREST,
        "bilinear": cv2.INTER_LINEAR,
        "bicubic": cv2.INTER_CUBIC,
        "area": cv2.INTER_AREA,
        "lanczos4": cv2.INTER_LANCZOS4
        }
        
        assert self.interploation in interpolations.keys()
        
        # create a rotation matric
        w, h = (self.channel.shape[2], self.channel.shape[1])
        img_center = (self.channel.shape[2]/2, self.channel.shape[1]/2)
        rot = cv2.getRotationMatrix2D(img_center, self.angle, 1)
        
        # calculate the new size of a frame
        rad = math.radians(self.angle)
        sin = math.sin(rad)
        cos = math.cos(rad)
        b_w = int((h * abs(sin)) + (w * abs(cos)))
        b_h = int((h * abs(cos)) + (w * abs(sin)))

        # re-center the frame
        rot[0, 2] += ((b_w / 2) - img_center[0])
        rot[1, 2] += ((b_h / 2) - img_center[1])
        
        # new stack of frame with the correct size
        new_data = np.zeros(shape=(self.channel.shape[0], b_h, b_w), dtype=np.int32)
        
        # apply rotation
        for i in range(self.channel.shape[0]):
            new_data[i] = cv2.warpAffine(self.channel.data[i], rot, (b_w, b_h), flags=interpolations[self.interploation])
        
        self.channel.data = new_data
        return self.channel

def rotateType(chn: Channel, rotType):
    if rotType == cv2.ROTATE_180:
        new_data = np.zeros(shape=chn.shape, dtype=np.int32)
    else:
        new_data = np.zeros(shape=(chn.shape[0], chn.shape[2], chn.shape[1]), dtype=np.int32)
    
    for i in range(chn.shape[0]):
        new_data[i] = cv2.rotate(chn.data[i], rotType)
    chn.data = new_data

class ChannelRotate90(ChannelOperation):
    def __init__(self, chn: Channel):
        super().__init__([Channel], Channel, chn)
    
    def run(self):
        rotateType(self.channel, cv2.ROTATE_90_CLOCKWISE)
        return self.channel

class ChannelRotate180(ChannelOperation):
    def __init__(self, chn: Channel):
        super().__init__([Channel], Channel, chn)
    
    def run(self):
        rotateType(chn, cv2.ROTATE_180)
        return self.channel

class ChannelRotate270(ChannelOperation):
    def __init__(self, chn: Channel):
        super().__init__([Channel], Channel, chn)
    
    def run(self):
        rotateType(chn, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return self.channel

class ChannelFlipHorizontally(ChannelOperation):
    def __init__(self, chn: Channel):
        super().__init__([Channel], Channel, chn)
    
    def run(self):
        for i in range(self.channel.shape[0]):
            self.channel.data[i] = cv2.flip(self.channel.data[i], 1)
        return self.channel

class ChannelFlipVertically(ChannelOperation):
    def __init__(self, chn: Channel):
        super().__init__([Channel], Channel, chn)
    
    def run(self):
        for i in range( self.channel.shape[0]):
            self.channel.data[i] = cv2.flip(self.channel.data[i], 0)
        return self.channel

class PixelIntensity(Operation):
    def __init__(self, chn: Channel):
        super().__init__([Channel], list)
        self.input_channel = chn
    
    def run(self):        
        px_intensity = np.zeros(shape=(256), dtype=np.int32)
        
        for px in self.channel:
            px_intensity[px] += 1
        
        self.output.set(px_intensity)
        return px_intensity

class ChannelPlot(Operation):
    def __init__(self, channel: OperationOutput):
        super().__init__([OperationOutput], None)
        if type(channel) is Channel:
            input = OperationOutput(input)
        
        if type(channel) is not OperationOutput:
            raise TypeError("the ChannelPlot operation requires a Channel or a OperationOutput that correspond to a Channel")
            
        self.input_channel = channel
    
    def run(self):
        plotChannel(self.input_channel.get())

class ChannelZProjectionMax(Operation):
    def __init__(self, channel: Channel):
        super().__init__([Channel], Frame)
        
        if type(channel) is Channel:
            input = OperationOutput(input)
        
        if type(channel) is not OperationOutput:
            raise TypeError("the ChannelZProjectionMax operation requires a Channel or a OperationOutput that correspond to a Channel")
            
        self.input_channel = channel
    
    def run(self):
        self.output = self.input_channel.get().data.max(0)
        return self.output.get()

class ChannelZProjectionMin(Operation):
    def __init__(self, channel: Channel):
        super().__init__([Channel], Frame)
        
        if type(channel) is Channel:
            input = OperationOutput(input)
        
        if type(channel) is not OperationOutput:
            raise TypeError("the ChannelZProjectionMin operation requires a Channel or a OperationOutput that correspond to a Channel")
            
        self.input_channel = channel
    
    def run(self):
        self.output = self.input_channel.get().data.min(0)
        return self.output.get()

class ChannelZProjectionMean(Operation):
    def __init__(self, channel: Channel):
        super().__init__([Channel], Frame)
        
        if type(channel) is Channel:
            input = OperationOutput(input)
        
        if type(channel) is not OperationOutput:
            raise TypeError("the ChannelZProjectionMean operation requires a Channel or a OperationOutput that correspond to a Channel")
            
        self.input_channel = channel
    
    def run(self):
        self.output = self.input_channel.get().data.mean(0)
        return self.output.get()

# TODO: Verify types of the channels to be Channel

class ChannelAND(ChannelOperation):
    def __init__(self, *channels, threshold: int=1):
        super().__init__([list, int], Channel, Channel())
        
        self.channels = []
        self.threshold = threshold
        
        for chn in channels:
            if type(chn) is OperationOutput:
                self.channels.append(chn.get())
            else:
                self.channels.append(chn)
    
    def run(self):
        self.channel.copyFrom(self.channels[0])
        for chn in self.channels[1:]:
            self.channel.data = np.where(chn.data >= self.threshold, self.channel.data, 0)
        return self.channel

class ChannelOR(ChannelOperation):
    def __init__(self, *channels):
        super().__init__([list], Channel, Channel())
        
        self.channels = []
        
        for chn in channels:
            if type(chn) is OperationOutput:
                self.channels.append(chn.get())
            else:
                self.channels.append(chn)
    
    def run(self):
        self.channel.copyFrom(self.channels[0])
        datas = []
        for channel in self.channels:
            datas.append(channel.data)
        self.channel.data = np.maximum.reduce(datas)
        return self.channel
    
class ChannelADD(ChannelOperation):
    def __init__(self, *channels):
        super().__init__([list], Channel, Channel())
        
        self.channels = []
        
        for chn in channels:
            if type(chn) is OperationOutput:
                self.channels.append(chn.get())
            else:
                self.channels.append(chn)
    
    def run(self):
        self.channel.copyFrom(self.channels[0])
        self.channel.data = self.channel.data.astype(np.uint16)
        for chn in self.channels[1:]:
            self.channel.data += chn.data
        self.channel.data = self.channel.data.clip(0, 255)
        self.channel.data = self.channel.data.astype(np.uint8)
        return self.channel

class ChannelSUB(ChannelOperation):
    def __init__(self, *channels):
        super().__init__([list], Channel, Channel())
        
        self.channels = []
        
        for chn in channels:
            if type(chn) is OperationOutput:
                self.channels.append(chn.get())
            else:
                self.channels.append(chn)
    
    def run(self):
        self.channel.copyFrom(self.channels[0])
        self.channel.data = self.channel.data.astype(np.uint16)
        for chn in self.channels[1:]:
            self.channel.data -= chn.data
        self.channel.data = self.channel.data.clip(0, 255)
        self.channel.data = self.channel.data.astype(np.uint8)
        return self.channel

class ChannelAdjustContrast(ChannelOperation):
    def __init__(self, channel: Channel, brightness: int, contrast: int):
        super().__init__([Channel, int, int], Channel, channel)

        self.brightness = brightness
        self.contrast = contrast
        
    def run(self):
        def contrastFactor(c):
            return (259*(c + 255)) / (255*(259 - c))

        factor = contrastFactor(self.contrast)
        
        data = self.channel.data.astype(np.float16)
        
        data += self.brightness
        data = factor*(data - 128) + 128
    
        self.channel.data = data.clip(0, 255).astype(np.uint8)
        return self.channel

class ChannelAverage(ChannelOperation):
    def __init__(self, *channels):
        super().__init__([list], Channel, Channel())
        
        self.channels = []
        
        for chn in channels:
            if type(chn) is OperationOutput:
                self.channels.append(chn.get())
            else:
                self.channels.append(chn)
        
    def run(self):
        self.channel.copyFrom(self.channels[0])
        
        data = []
        for chn in self.channels:
            data.append(chn.data)
        
        data = np.array(data, dtype=np.uint32)
        data: np.ndarray = data.mean(0)
        
        self.channel.data = data.astype(np.uint8)
        return self.channel

class ChannelThreshold(ChannelOperation):
    def __init__(self, channel: Channel, t_min: int, t_max: int):
        super().__init__([Channel, int, int], Channel, channel)
        
        self.t_min = t_min
        self.t_max = t_max
    
    def run(self):
        self.channel.data[self.channel.data < self.t_min] = 0
        self.channel.data[self.channel.data < self.t_max] = 0
        return self.channel

class ChannelResliceTop(ChannelOperation):    
    def __init__(self, channel: Channel):
        super().__init__([Channel], Channel, Channel())
        
        self.input_channel = channel
    
    def run(self):
        self.channel.copyFrom(self.input_channel)
        
        Z, Y, X = self.input_channel.shape
    
        reslice = np.swapaxes(self.input_channel.data, 0, 1) # (Z, Y, X) -> (Y, Z, X)
        
        new_Z = Z * self.input_channel.px_sizes.Z / self.input_channel.px_sizes.Y
        new_Z = int(new_Z)
        
        result = np.zeros((Y, new_Z, X))
        
        for i in range(Y):
            result[i, :, :] =  cv2.resize(reslice[i], (X, new_Z), interpolation=cv2.INTER_CUBIC)
            
        self.channel.name = "reslicedTop_" + self.channel.name
        self.channel.data = result 
        return self.channel

class ChannelResliceLeft(ChannelOperation):    
    def __init__(self, channel: Channel):
        super().__init__([Channel], Channel, Channel())
        
        self.input_channel = channel
    
    def run(self):
        self.channel.copyFrom(self.input_channel)
        
        Z, Y, X = self.input_channel.shape
        
        reslice = np.swapaxes(self.input_channel.data, 0, 2) # (Z, Y, X) -> (X, Y, Z)
        reslice = np.swapaxes(reslice, 1, 2) # (X, Y, Z) -> (X, Z, Y)
        
        new_Z = Z * self.input_channel.px_sizes.Z / self.input_channel.px_sizes.X
        new_Z = int(new_Z)
        
        result = np.zeros((X, new_Z, Y))
        
        for i in range(X):
            result[i, :, :] =  cv2.resize(reslice[i], (Y, new_Z), interpolation=cv2.INTER_CUBIC)
            
        self.channel.name = "reslicedLeft_" + self.channel.name
        self.channel.data = result 
        return self.channel

class ChannelReverse(ChannelOperation):
    def __init__(self, channel: Channel):
        super().__init__([Channel], Channel, channel)
    
    def run(self):
        self.channel.data = self.channel.data[::-1]
        return self.channel

class ChannelVolume(Operation):
    def __init__(self, channel: Channel, min_obj_size=0):
        super().__init__([Channel, int], float)
        
        self.input_channel = channel
        self.min_obj_size = min_obj_size
        
    def run(self):
        l, n = ndimage.label(self.input_channel.data, np.ones((3, 3, 3)))
    
        f = ndimage.find_objects(l)
        
        count = []
        
        for i in range(len(f)):
            count.append(np.count_nonzero(l[f[i]] == i+1))
        count = np.array(count)
        
        self.output = count[count >= self.min_obj_size].sum() * chn.px_sizes.Z * chn.px_sizes.Y * chn.px_sizes.X
        return self.output.get()

class ChannelVolumeArray(Operation):
    def __init__(self, channel: Channel, threshold: int=0):
        super().__init__([Channel, int], list)
        
        self.input_channel = channel
        self.threshold = threshold
        
    def run(self):
        def frameVolume(data, sizes, threshold=0):
            return np.count_nonzero(data[data >= threshold]) * sizes.Z * sizes.Y * sizes.X
    
        z, y, x = self.input_channel.shape
        
        volumes = []
        
        for i in range(z):
            volumes.append(frameVolume(chn.data[i], self.input_channel.px_sizes, self.threshold))
        
        self.output = volumes
        return self.output.get()  

class ChannelExportOBJ(Operation):
    def __init__(self, channel: Channel, filename="", step_size=2):
        super().__init__([Channel, str, int], None)
        
        self.input_channel = channel
        self.filename = filename
        self.step_size = step_size
        
        if self.filename == "":
            self.filename = channel.name + ".obj"
    
    def run(self):
        channelSaveToObj(self.input_channel, self.filename, self.step_size)


def volumeSaveCSV(filename: str, volumes):
    with open(filename, "w") as file:
        file.write("\n".join(map(str, volumes)))

if __name__ == '__main__':
    chn = loadChannel("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn2 = loadChannel("../resources/Threshold3.4UserAveragedC1E2.tif")[0]
    
    # invert = ChannelInvert(chn)
    # rotate = ChannelRotate180(invert.output)
    # chplot = ChannelPlot(rotate.output)
    
    # invert.run()
    # rotate.run()
    # chplot.run()
    
    # pipeline = [invert, rotate, chplot]
    # Operation.execute(pipeline)
    
    opn = ChannelLoad("../resources/Threshold3.4UserAveragedC1E1.tif")
    opn2 = ChannelLoad("../resources/Threshold3.4UserAveragedC1E2.tif")
    
    avg = ChannelAverage(opn.output, opn2.output)
    rot = ChannelRotate90(avg.output)
    plo = ChannelPlot(rot.output)
    
    pipeline = [opn, opn2, avg, rot, plo]
    Operation.execute(pipeline)
    
    # plotChannel(chn)