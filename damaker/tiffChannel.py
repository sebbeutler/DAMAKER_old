from aicsimageio.types import PhysicalPixelSizes
import numpy as np
from aicsimageio.writers import OmeTiffWriter

class TiffChannel:
    def __init__(self, name: str="", data: np.ndarray=[], physicalPixelSizes: PhysicalPixelSizes=None, channel: int=0):
        self.name = name
        self.data = np.array(data)
        self.px_sizes = physicalPixelSizes
        self.channel = channel
    
    @property
    def shape(self):
        return self.data.shape
    
    def save(self, filename: str):
        OmeTiffWriter.save(self.data, filename, physical_pixel_sizes=self.px_sizes)    
        
    def copy(self):
        return TiffChannel(self.name, self.data.copy(), self.px_sizes, self.channel)

    def copyFrom(self, channel, copy_array=False):
        self.name = channel.name
        self.data = channel.data if not copy_array else channel.data.copy()
        self.px_sizes = channel.px_sizes
        self.channel = channel
    
    def clone(self, data: np.ndarray):
        return TiffChannel(self.name, data.copy(), self.px_sizes, self.channel)

    def free(self):
        del self.data

class TiffFrame:
    def __init__(self, data: np.ndarray=[]):
        self.data = np.array(data)