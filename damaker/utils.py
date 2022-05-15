import os
from os import path

from tiffile import TiffFile
from .Channel import Channel

import numpy as np
from skimage import measure

from aicsimageio.writers import OmeTiffWriter
from aicsimageio.readers import bioformats_reader
from aicsimageio.types import PhysicalPixelSizes

class StrFilePath(str):
    pass

class StrFolderPath(str):
    pass

def loadChannelsFromFile(filename: StrFilePath):
    if not path.exists(filename):
        print("[DAMAKER] Warning: file '" + filename + "' not found.")
        return None
    
    channels = loadChannels_tiffile(filename)
    metadata = bioformats_reader.BioFile(filename).ome_metadata
    
    px_sizes = PhysicalPixelSizes(
        metadata.images[0].pixels.physical_size_z,
        metadata.images[0].pixels.physical_size_y,
        metadata.images[0].pixels.physical_size_x
    )
    
    for ch in channels:
        ch.px_sizes = px_sizes
    
    return channels

def loadChannels_aicsi(filename: StrFilePath):
    # verify if the file exist
    if not path.exists(filename):
        print("[DAMAKER] Warning: file '" + filename + "' not found.")
        return None
    
    channels = []
        
    file = bioformats_reader.BioformatsReader(filename)
    fn = filename.split("/")[-1]
    
    # TODO: test get all channel at the same time then split them for better performance
    for i in range(0, file.dims.C):
        channels.append(Channel(fn, file.get_image_data("ZYX", C=i), file.physical_pixel_sizes, i))
    
    return channels

def loadChannels_tiffile(filename: StrFilePath):
    # verify if the file exist
    if not path.exists(filename):
        print("[DAMAKER] Warning: file '" + filename + "' not found.")
        return None
        
    with TiffFile(filename) as file:
        data = file.asarray()
        
        metadata = file.imagej_metadata
        print("File loaded:", filename)
    
    print(data.shape)
    fn = filename.split("/")[-1]
    
    # Split the file by channel
    if len(data.shape) == 3:
        return [Channel(fn, data, metadata)]
    elif len(data.shape) == 4:
        data = data.swapaxes(0, 1)
        objs = []
        for i in range(data.shape[0]):
            objs.append(Channel(fn, data[i, :, :, :], metadata, i))
        return objs

def loadChannelsFromDir(path: StrFolderPath, suffix: str=""):
    channels = []
    
    files = os.listdir(path)
    for file in files:
        if not file.endswith(suffix):
            continue
        
        for chn in loadChannelsFromFile(path + "/" + file):
            channels.append(chn)
    
    return channels

def channelSave(chn: Channel, folderPath: StrFolderPath):
    chn.save(folderPath)

def saveChannels(filename: StrFilePath, channels: list[Channel]):
    shape = channels[0].shape
    
    for ch in channels:
        if ch.shape != shape:
            raise TypeError("[DAMAKER] saveChannels(): channels do not have the same shape")
    
    data = [None] * len(channels)
    for ch in channels:
        data[ch.channel] = ch.data
    
    for ch in data:
        if ch is None:
            raise AttributeError("[DAMAKE] saveChannels(): channels ids are incorrect.")
    
    data = np.array(data)
    OmeTiffWriter.save(data, filename, "CZYX", physical_pixel_sizes=channels[0].px_sizes)

def channelSaveToObj(chn: Channel, filename: StrFilePath, stepsize=2):
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
    
    with open(filename, 'w') as file:        
        for v in vertices:
            file.write("v {} {} {}\n".format(*v))
            
        for f in triangles:
            file.write("f {} {} {}\n".format(*(f + 1)))

def listSaveCSV(data_list, path: StrFolderPath, filename: str=""):
    if filename != "":
        path += "/" + filename
    with open(path, "w") as file:
        file.write("\n".join(map(str, data_list)))

def axisQuantifSaveCSV(axis_data, path: StrFolderPath, filename: str):
    if len(axis_data) != 3:
        raise ValueError("Need only 3 axis")
    listSaveCSV(axis_data[0], path, filename + "_front.csv")
    listSaveCSV(axis_data[1], path, filename + "_top.csv")
    listSaveCSV(axis_data[2], path, filename + "_left.csv")
    
def createDirectory(path: StrFolderPath):
    os.makedirs(path, exist_ok=True)
        

import matplotlib.pyplot as plt
from vedo.applications import Browser
from vedo.picture import Picture

def plotChannel(input: Channel):    
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
        
    plotFrame(res)

def plotArray(data, title=""):
    plt.plot(data)
    plt.title(title)
    plt.show()

def plotArrays(data_list, labels=[], title=""):
    if len(labels) != len(data_list):
        labels = [""] * len(data_list)
    
    for i in range(len(data_list)):
        plt.plot(data_list[i], label=labels[i])
    plt.title(title)
    plt.legend()
    plt.show()

def plotMesh(filename: StrFilePath, rotate=True, mirror=False):
    mesh = Mesh(filename)
    if rotate:
        mesh = mesh.rotate(90)
    if mirror:
        mesh = mesh.mirror("z")
    mesh.show()

def plotAxisQuantifications(data_list: list, labels=[], title=""):
    if len(labels) != len(data_list):
        labels = [""] * len(data_list)
        
    axis_label = ["front", "top", "left"]
    
    for i in range(3):
        for j in range(len(data_list)):
            plt.plot(data_list[j][i], label=labels[j])
    
        plt.title(title + " - Axis " + axis_label[i])
        plt.legend()
        plt.show()