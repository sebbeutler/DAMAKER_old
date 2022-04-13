from aicsimageio import AICSImage
from vedo import *
from vedo.picture import Picture
import numpy as np
from vedo.applications import *
from aicsimageio.writers import OmeTiffWriter
from tiffile import *
from processing import *

def test1():
    img = AICSImage("../resources/Threshold3.4UserAveragedC1E1.tif")

    print(img.dims)
    # print(img.shape)
    # print(img.metadata)

    actors = []

    for i in range(img.dims.Z):
        actors.append(Picture(img.get_image_data("YX", Z=i)).binarize(invert=True))

    plt = Browser(actors, bg="light blue", screensize=[795, 634], axes=2)
    plt.show()


def test2():

    # Load a mesh and show it
    vol = plt.load("../resources/Threshold3.4UserAveragedC1E1.tif")

    plt = Slicer3DPlotter(vol,
                      bg='white', bg2='lightblue',
                      useSlider3D=False,
    )
    plt.show()

def test3():
    img = AICSImage("../resources/Threshold3.4UserAveragedC1E1.tif")
    arr = img.get_image_data("ZYX")
    print(arr.shape)

def test4(): 
    img = AICSImage("../resources/E1.tif")
    print(img.metadata)

def test5():
    # img = imread('../resources/Threshold3.4UserAveragedC1E1.tif')
    img = imread('../resources/E1.tif')
    i = img[:, 1, :, :]
    obj = TiffObject("test", i, [])
    plot(obj)

def test6():
    obj = openTiff('../resources/Threshold3.4UserAveragedC1E1.tif')
    obj.invert()
    plot(obj)

def test7():
    with TiffFile('../resources/Threshold3.4UserAveragedC1E1.tif') as tif:
        md = tif.imagej_metadata
    for k, e in md.items():
        print(f'{k} {e}')

def test8():
    obj = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    crop(obj, (50, 50), (100, 100))
    plot(obj)

if __name__ == '__main__':
    test8()