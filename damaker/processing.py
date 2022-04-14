import math
from vedo.applications import *
from vedo.picture import Picture
from tiffile import *
from os.path import exists
import cv2

import numpy as np

class TiffChannel:
    def __init__(self, name: str="", data: np.ndarray=[], metadata: list={}, channel: int=0):
        self.name = name
        self.data = np.array(data)
        self.metadata = metadata
        self.channel = channel
    
    @property
    def shape(self):
        return self.data.shape
    
    def save(self, filename: str):
        imwrite(filename, self.data, metadata=self.metadata)
    
    def invert(self):
        self.data = 255 - self.data

def openTiff(filename: str):
    """Open a .tiff/.tif file

    Args:
        filename (str): name of the file

    Returns:
        TiffChannel: the corresponding object loaded from the file
        list(TiffChannel): a list of TiffChannel corresponding to each channel of the file
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
        return TiffChannel(fn, data, metadata)
    elif len(data.shape) == 4:
        objs = []
        for i in range(data.shape[1]):
            objs.append(TiffChannel(fn, data[:, i, :, :], metadata, i))
        return objs

def crop(chn: TiffChannel, p1, p2):
    chn.data = chn.data[:, p1[1]:p2[1], p1[0]:p2[0]]
    return chn

def rotate(chn: TiffChannel, degrees: float):
    # create a rotation matric
    w, h = (chn.shape[2], chn.shape[1])
    img_center = (chn.shape[2]/2, chn.shape[1]/2)
    rot = cv2.getRotationMatrix2D(img_center, 30, 1)
    
    # calculate the new size of a frame
    rad = math.radians(30)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    # re-center the frame
    rot[0, 2] += ((b_w / 2) - img_center[0])
    rot[1, 2] += ((b_h / 2) - img_center[1])
    
    # new stack of frame with the correct size
    new_data = np.zeros(shape=(chn.shape[0], b_h, b_w), dtype=np.int32)
    
    # apply rotation
    for i in range(chn.shape[0]):
        new_data[i] = cv2.warpAffine(chn.data[i], rot, (b_w, b_h), flags=cv2.INTER_LINEAR)
    
    chn.data = new_data

_plt = None
def plot(tiff: TiffChannel):
    global _plt
    actors = []

    for i in range(tiff.shape[0]):
        actors.append(Picture(tiff.data[i]))

    _plt = Browser(actors, bg="light blue", screensize=[tiff.shape[1], tiff.shape[2]], axes=2)
    _plt.show()