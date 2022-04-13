from vedo.applications import *
from vedo.picture import Picture
from tiffile import *
from os.path import exists

import numpy as np

class TiffObject:
    def __init__(self, name: str="", data: np.ndarray=[], metadata: list={}, channel: int=0):
        self.name = name
        self.data = np.array(data)
        self.shape = self.data.shape
        self.metadata = metadata
        self.channel = channel
    
    def save(self, filename: str):
        imwrite(filename, self.data, metadata=self.metadata)
    
    def invert(self):
        self.data = 255 - self.data

def openTiff(filename: str):
    """Open a .tiff/.tif file

    Args:
        filename (str): name of the file

    Returns:
        TiffObject: the corresponding object loaded from the file
        list(TiffObject): a list of TiffObject corresponding to each channel of the file
    """
    # verify if the file exist
    if not exists(filename):
        print("[DAMAKER] Warning: file '" + filename + "' not found.")
        return None
    
    # load data from the file
    with TiffFile(filename) as file:
        data = file.asarray()
        metadata = file.imagej_metadata
        print("File loaded")
        
    fn = filename.split("/")[-1]
    # Split the file by channel
    if len(data.shape) == 3:
        return TiffObject(fn, data, metadata)
    elif len(data.shape) == 4:
        objs = []
        for i in range(data.shape[1]):
            objs.append(TiffObject(fn, data[:, i, :, :], metadata, i))
        return objs

def crop(obj: TiffObject, p1, p2):
    obj.data = obj.data[:, p1[1]:p2[1], p1[0]:p2[0]]
    obj.shape = obj.data.shape
    return obj

_plt = None
def plot(tiff: TiffObject):
    global _plt
    actors = []

    for i in range(tiff.shape[0]):
        actors.append(Picture(tiff.data[i]))

    _plt = Browser(actors, bg="light blue", screensize=[tiff.shape[1], tiff.shape[2]], axes=2)
    _plt.show()