from aicsimageio.types import PhysicalPixelSizes
import numpy as np
from aicsimageio.writers import OmeTiffWriter

class Channel:
    def __init__(self, name: str="", data: np.ndarray=[], physicalPixelSizes: PhysicalPixelSizes=None, id: int=0, lut=None):
        self.name = name
        self.data = np.array(data)
        self.px_sizes = physicalPixelSizes
        self.id = id
        self.lut = lut
    
    @property
    def shape(self):
        return self.data.shape
    
    def save(self, folderPath: str=""):
        if folderPath != "" and folderPath[-1] not in "/\\":
            folderPath += "/"
        OmeTiffWriter.save(self.data, folderPath + f'{self.name}_C{self.id}.tif', physical_pixel_sizes=self.px_sizes)    
        
    def copy(self):
        return Channel(self.name, self.data.copy(), self.px_sizes, self.id, self.lut)

    def copyFrom(self, channel, copy_array=False):
        self.name = channel.name
        self.data = channel.data if not copy_array else channel.data.copy()
        self.px_sizes = channel.px_sizes
        self.id = channel.id
        self.lut = channel.lut
    
    def clone(self, data: np.ndarray):
        return Channel(self.name, data.copy(), self.px_sizes, self.id, self.lut)

    def free(self):
        del self.data
    
    def __str__(self):
        return f"'{self.name}' chn n°{self.id} dim:{self.shape} px:X=%.2f Y=%.2f Z=%.2f" % (self.px_sizes.X,self.px_sizes.Y,self.px_sizes.Z)

class Channels(list):
    pass

class Frame:
    def __init__(self, data: np.ndarray=[]):
        self.data = np.array(data)