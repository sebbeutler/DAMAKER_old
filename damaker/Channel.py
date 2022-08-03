from aicsimageio.types import PhysicalPixelSizes
import numpy as np
from aicsimageio.writers import OmeTiffWriter
from ome_types.model import OME
import pyqtgraph as pg

class Channel:
    def __init__(self, name: str="", data: np.ndarray=[], physicalPixelSizes: PhysicalPixelSizes=None, id: int=0, lut: pg.ColorMap=None, metadata: OME=None):
        self.name = name
        self.data = np.array(data)
        self.px_sizes = physicalPixelSizes
        self.id = id
        self.lut = lut
        self.metadata = metadata
        
        self.show = True
        self.frames = None
    
    @property
    def shape(self):
        return self.data.shape
    
    def save(self, folderPath: str="", includeChannelId: bool=False, filename: str=""):
        if folderPath != "" and folderPath[-1] not in "/\\":
            folderPath += "/"
        if filename == "":
            if includeChannelId:
                filename = f'{self.name}_C{self.id}.tif'
            else:
                filename = f'{self.name}.tif'
        
        if len(self.data.shape) == 3:
            OmeTiffWriter.save(self.data, folderPath + filename, physical_pixel_sizes=self.px_sizes, dim_order="ZYX")
        elif len(self.data.shape) == 4:
            OmeTiffWriter.save(self.data, folderPath + filename, physical_pixel_sizes=self.px_sizes, dim_order="CZYX")
        print(f'saved: {filename}') 
        
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
        if self.px_sizes != None:
            return f"'{self.name}' [C:{self.id}, size:{self.shape} px:(%.2f,%.2f,%.2f)" % (self.px_sizes.X,self.px_sizes.Y,self.px_sizes.Z)
        else:
            return f"'{self.name}' [C:{self.id}, size:{self.shape}"

class SingleChannel(Channel):
    pass

class Channels(list[Channel]):
    pass

class Frame:
    def __init__(self, data: np.ndarray=[]):
        self.data = np.array(data)