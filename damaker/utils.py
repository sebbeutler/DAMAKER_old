import os

from .dmktypes import *
from .ImageStack import *

import numpy as np
from skimage import measure

from tiffile import TiffFile

# AICSio #
# from aicsimageio.writers import OmeTiffWriter
# from aicsimageio.readers import bioformats_reader, OmeTiffReader
# from aicsimageio.types import PhysicalPixelSizes

# BIOFORMATS #
import javabridge, bioformats, xmltodict

from vedo import Mesh, Plotter

def _dataloader_bioformats(filename, StrFilePath) -> ImageStack:
    raise Exception()

def _metadataloader_bioformats(filepath: FilePathStr, _kill_vm=False) -> ImageStackMetadata:
    javabridge.start_vm(run_headless=True, class_path=bioformats.JARS, max_heap_size='500M')

    # JAVABRIDGE SILENT / NO LOG #
    myloglevel="ERROR"  # user string argument for logLevel.
    rootLoggerName = javabridge.get_static_field("org/slf4j/Logger","ROOT_LOGGER_NAME", "Ljava/lang/String;")
    rootLogger = javabridge.static_call("org/slf4j/LoggerFactory","getLogger", "(Ljava/lang/String;)Lorg/slf4j/Logger;", rootLoggerName)
    logLevel = javabridge.get_static_field("ch/qos/logback/classic/Level",myloglevel, "Lch/qos/logback/classic/Level;")
    javabridge.call(rootLogger, "setLevel", "(Lch/qos/logback/classic/Level;)V", logLevel)

    javabridge.attach()

    data = bioformats.get_omexml_metadata(filepath)
    dict_ome = xmltodict.parse(data)

    if _kill_vm:
        javabridge.kill_vm()

    metadata = ImageStackMetadata()
    metadata.pixelsize = PixelSize(
        float(dict_ome['OME']['Image']['Pixels']['@PhysicalSizeZ']),
        float(dict_ome['OME']['Image']['Pixels']['@PhysicalSizeY']),
        float(dict_ome['OME']['Image']['Pixels']['@PhysicalSizeX']),
    )
    metadata.unit = MesureUnit.strToUnit(dict_ome['OME']['Image']['Pixels']['@PhysicalSizeZUnit'])

    print('✔')
    return metadata

def _dataloader_aicsi(filename: FilePathStr) -> ImageStack:
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

def _dataloader_tiffile(filename: FilePathStr) -> np.ndarray:
    with TiffFile(filename) as file:
        data = file.asarray()
        axes = file.series[0].axes
        metadata = file.imagej_metadata

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
    print('✔')
    return data

def channelSave(chn: ImageStack, folderPath: FolderPathStr, includeChannelId: bool=False):
    """
        Name: Save channel
        Category: Export
    """ 
    chn.save(folderPath, includeChannelId)

def channelsSave(channels: ImageStack, folderPath: FolderPathStr):
    """
        Name: Save stack
        Category: Process
    """
    if type(channels) is ImageStack:
        return channels.save(folderPath)
    if len(channels) == 1:
        return channels[0].save(folderPath)
    for ch in channels:
        if type(ch) != ImageStack:
            return
    out = channels[0].clone(np.array([chn.data for chn in channels]))
    out.save(folderPath)

def channelSaveToObj(chn: ImageStack, stepsize: int=2, outputDir: FolderPathStr=""):
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

def listSaveCSV(data: NamedArray, path: FolderPathStr):
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

def _axisQuantifSaveCSV(axis_data, path: FolderPathStr, filename: str):
    if len(axis_data) != 3:
        raise ValueError("Need only 3 axis")
    listSaveCSV(axis_data[0], path, filename + "_front.csv")
    listSaveCSV(axis_data[1], path, filename + "_top.csv")
    listSaveCSV(axis_data[2], path, filename + "_left.csv")

def _createDirectory(path: FolderPathStr):
    """
        Name: Create folder
        Category: Export
    """
    os.makedirs(path, exist_ok=True)


import matplotlib.pyplot as plt
from vedo.applications import Browser
from vedo.picture import Picture

def _plotChannel(input:ImageStack):
    actors = []

    for i in range(input.shape[0]):
        actors.append(Picture(input.data[i], flip=True))

    _plt = Browser(actors, bg="light blue", screensize=[input.shape[1], input.shape[2]], axes=2)
    _plt.show()

def _plotFrame(data: np.ndarray):
    _plt = Plotter(bg="light blue")
    _plt.add(Picture(data, flip=True))
    _plt.show()

def _plotChannelRGB(ch_r:ImageStack=None, ch_g:ImageStack=None, ch_b:ImageStack=None):
    def getrgb(arr, col):
        rgb = np.zeros((arr.shape[0], arr.shape[1], arr.shape[2], 3))
        rgb[:, :, :, col] = arr[:, :, :]
        return rgb

    red = getrgb(ch_r.data, 0).astype(np.uint16) if ch_r is not None else 0
    green = getrgb(ch_g.data, 1).astype(np.uint16) if ch_g is not None else 0
    blue = getrgb(ch_b.data, 2).astype(np.uint16) if ch_b is not None else 0

    res = red + green + blue
    res = res.clip(0, 255)

    _plotChannel(Channel("", res))

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

def _plotMesh(filename: FilePathStr, rotate: bool=True, mirror: bool=False):
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