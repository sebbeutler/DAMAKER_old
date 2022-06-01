import os

from tiffile import TiffFile

from .Channel import Channel, Channels

import numpy as np
from skimage import measure

from aicsimageio.writers import OmeTiffWriter
from aicsimageio.readers import bioformats_reader
from aicsimageio.types import PhysicalPixelSizes

from vedo import Mesh, Plotter

class StrFilePath(str):
    pass

class StrFolderPath(str):
    pass

class NamedArray:
    name: str=""
    data: list=[]

def loadChannelsFromFile(filename: StrFilePath):
    """
        Name: Import .tif
        Category: Import
    """ 
    if not os.path.isfile(filename):
        print("[DAMAKER] Warning: file '" + filename + "' not found.")
        return None
    
    channels = _loadChannels_tiffile(filename)    
    # channels = _loadChannels_aicsi(filename)    
    metadata = bioformats_reader.BioFile(filename).ome_metadata
    
    px_sizes = PhysicalPixelSizes(
        metadata.images[0].pixels.physical_size_z,
        metadata.images[0].pixels.physical_size_y,
        metadata.images[0].pixels.physical_size_x
    )
    
    for ch in channels:
        if type(ch) is Channel:
            ch.px_sizes = px_sizes
            print(f'Loaded: {ch}')
    return channels

def _loadChannels_aicsi(filename: StrFilePath):
    # verify if the file exist
    if not os.path.isfile(filename):
        print("[DAMAKER] Warning: file '" + filename + "' not found.")
        return None
    
    channels = []
        
    file = bioformats_reader.BioformatsReader(filename)
    fn = filename.split("/")[-1]
    fn = ".".join(fn.split(".")[:-1])
    
    # TODO: test get all channel at the same time then split them for better performance
    # for i in range(0, file.dims.C):
    channels.append(Channel(fn, file.get_image_data("CZYX"), file.physical_pixel_sizes, 0))
    
    return channels

def _loadChannels_tiffile(filename: StrFilePath):
    # verify if the file exist
    if not os.path.isfile(filename):
        print("[DAMAKER] Warning: file '" + filename + "' not found.")
        return None
        
    with TiffFile(filename) as file:
        data = file.asarray()
        axes = file.series[0].axes
        
    fn = filename.split("/")[-1]
    fn = ".".join(fn.split(".")[:-1])
    
    targetorder = 'CZYX'
    axesorder = {}
    for i in range(len(axes)):
        axesorder[axes[i]] = i
        
    transpose = []
    for char in targetorder:
        if char in axesorder.keys():
            transpose.append(axesorder[char])
    
    data = data.transpose(tuple(transpose))           
    
    # Split the file by channel
    if len(data.shape) == 4:
        chns = []
        for i in range(data.shape[0]):
            chns.append(Channel(fn, data[i], id=i+1))
        return chns    
    elif len(data.shape) == 3:
        return [Channel(fn, data, id=1)]
    elif len(data.shape) == 2:
        return [Channel(fn, data[np.newaxis], id=1)]

def channelSave(chn: Channel, folderPath: StrFolderPath, includeChannelId: bool=False):
    """
        Name: Save channel
        Category: Export
    """ 
    chn.save(folderPath, includeChannelId)

def channelsSave(channels: Channels, folderPath: StrFolderPath):
    """
        Name: Combine channels
        Category: Export
    """    
    if type(channels) is Channel:
        return channels.save(folderPath)
    if len(channels) == 1:
        return channels[0].save(folderPath)
    for ch in channels:
        if type(ch) != Channel:
            return
    out = channels[0].clone(np.array([chn.data for chn in channels]))
    out.save(folderPath)

def channelSaveToObj(chn: Channel, stepsize: int=2, outputDir: StrFolderPath=""):
    """
        Name: Export to .obj
        Category: Export
    """ 
    chn = chn.copy()

    for i in range(stepsize):    
        chn.data = np.insert(chn.data, 0, np.zeros_like(chn.data[0]), axis=0)
        chn.data = np.insert(chn.data, -1, np.zeros_like(chn.data[0]), axis=0)        
        
        chn.data = np.insert(chn.data, 0, np.zeros_like(chn.data[:, 0, :]), axis=1)
        chn.data = np.insert(chn.data, -1, np.zeros_like(chn.data[:, 0, :]), axis=1)        
        
        chn.data = np.insert(chn.data, 0, np.zeros_like(chn.data[:, :, 0]), axis=2)
        chn.data = np.insert(chn.data, -1, np.zeros_like(chn.data[:, :, 0]), axis=2)
    
    
    # plot(chn)
    vertices, triangles, normals, values = measure.marching_cubes(chn.data, 0, step_size=stepsize, spacing=(chn.px_sizes.Z, chn.px_sizes.Y, chn.px_sizes.X), method="lorensen")    
    
    filename = outputDir + '/' + chn.name + '.obj'
    with open(filename, 'w') as file:        
        for v in vertices:
            file.write("v {} {} {}\n".format(*v))
            
        for f in triangles:
            file.write("f {} {} {}\n".format(*(f + 1)))
    print(f'saved: {filename}')

def listSaveCSV(data: NamedArray, path: StrFolderPath):
    """
        Name: Export to .csv
        Category: Export
    """ 
    if type(data) is NamedArray:
        data = [data]
    for array in data:
        if not type(array) is NamedArray:
            continue
        filename = array.name
        if not filename.endswith(".csv"):
            filename += ".csv"        
        with open(path + "/" + filename, "w") as file:
            file.write("\n".join(map(str, list(array.data))))
        print(f'saved: {filename}')

def _axisQuantifSaveCSV(axis_data, path: StrFolderPath, filename: str):
    if len(axis_data) != 3:
        raise ValueError("Need only 3 axis")
    listSaveCSV(axis_data[0], path, filename + "_front.csv")
    listSaveCSV(axis_data[1], path, filename + "_top.csv")
    listSaveCSV(axis_data[2], path, filename + "_left.csv")
    
def createDirectory(path: StrFolderPath):
    """
        Name: Create folder
        Category: Export
    """ 
    os.makedirs(path, exist_ok=True)
        

import matplotlib.pyplot as plt
from vedo.applications import Browser
from vedo.picture import Picture

def _plotChannel(input: Channel):   
    actors = []

    for i in range(input.shape[0]):
        actors.append(Picture(input.data[i], flip=True))

    _plt = Browser(actors, bg="light blue", screensize=[input.shape[1], input.shape[2]], axes=2)
    _plt.show()

def _plotFrame(data: np.ndarray):
    _plt = Plotter(bg="light blue")
    _plt.add(Picture(data, flip=True))
    _plt.show()

def _plotChannelRGB(ch_r: Channel=None, ch_g: Channel=None, ch_b: Channel=None):
    def getrgb(arr, col):
        rgb = np.zeros((arr.shape[0], arr.shape[1], arr.shape[2], 3))
        rgb[:, :, :, col] = arr[:, :, :]
        return rgb
    
    red = getrgb(ch_r.data, 0).astype(np.uint16) if ch_r is not None else 0
    green = getrgb(ch_g.data, 1).astype(np.uint16) if ch_g is not None else 0
    blue = getrgb(ch_b.data, 2).astype(np.uint16) if ch_b is not None else 0
    
    res = red + green + blue
    res = res.clip(0, 255)
        
    plotChannel(Channel("", res))

def _plotFrameRGB(data_r=None, data_g=None, data_b=None):
    def getrgbF(arr, col):
        rgb = np.zeros((arr.shape[0], arr.shape[1], 3))
        rgb[:, :, col] = arr[:, :]
        return rgb
    
    red = getrgbF(data_r, 0).astype(np.uint16) if data_r is not None else 0
    green = getrgbF(data_g, 1).astype(np.uint16) if data_g is not None else 0
    blue = getrgbF(data_b, 2).astype(np.uint16) if data_b is not None else 0
    
    res = red + green + blue
    res = res.clip(0, 255)
        
    _plotFrame(res)

def _plotArray(data, title=""):
    plt.plot(data)
    plt.title(title)
    plt.show()

def _plotArrays(data_list, labels=[], title=""):
    if len(labels) != len(data_list):
        labels = [""] * len(data_list)
    
    for i in range(len(data_list)):
        plt.plot(data_list[i], label=labels[i])
    plt.title(title)
    plt.legend()
    plt.show()

def _plotMesh(filename: StrFilePath, rotate: bool=True, mirror: bool=False):
    mesh = Mesh(filename)
    if rotate:
        mesh = mesh.rotate(90)
    if mirror:
        mesh = mesh.mirror("z")
    mesh.show()

def _plotAxisQuantifications(data_list: list, labels=[], title=""):
    if len(labels) != len(data_list):
        labels = [""] * len(data_list)
        
    axis_label = ["front", "top", "left"]
    
    for i in range(3):
        for j in range(len(data_list)):
            plt.plot(data_list[j][i], label=labels[j])
    
        plt.title(title + " - Axis " + axis_label[i])
        plt.legend()
        plt.show()