import math
from aicsimageio import AICSImage
from vedo import *
from vedo.picture import Picture
import numpy as np
from vedo.applications import *
from aicsimageio.writers import OmeTiffWriter
from tiffile import *
from processing import *
import cv2
from vedo.pyplot import plot as vplot
from vedo.pyplot import PlotBars

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
    chn = TiffChannel("test", i, [])
    plot(chn)

def test6():
    chn = openTiff('../resources/Threshold3.4UserAveragedC1E1.tif')
    chn.invert()
    plot(chn)

def test7():
    with TiffFile('../resources/Threshold3.4UserAveragedC1E1.tif') as tif:
        md = tif.imagej_metadata
    for k, e in md.items():
        print(f'{k} {e}')

def test8():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    crop(chn, (50, 50), (100, 100))
    plot(chn)

def test9():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    
    w, h = (chn.shape[2], chn.shape[1])
    img_center = (chn.shape[2]/2, chn.shape[1]/2)
    rot = cv2.getRotationMatrix2D(img_center, 30, 1)
    
    rad = math.radians(30)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    rot[0, 2] += ((b_w / 2) - img_center[0])
    rot[1, 2] += ((b_h / 2) - img_center[1])
    
    out_img = cv2.warpAffine(chn.data[55], rot, (b_w, b_h), flags=cv2.INTER_LINEAR)
    
    cv2.imshow("img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def test10():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    chn.invert()
    rotate(chn, 30)
    plot(chn)

def test11():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    rotate90(chn)
    plot(chn)

def test12():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    flipHorizontally(chn)
    plot(chn)

def test13():
    chn = openTiff("../resources/E1.tif")[0]
    img = chn.data[55]
    
    px_int = np.zeros(shape=(256), dtype=np.int32)
    
    for px in img:
        px_int[px] += 1
    
    vplot(px_int).show()

def test14():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    chn.invert()
    plot(chn)
    rotate90(chn)
    plot(chn)
    flipVertically(chn)
    plot(chn)


import aicsimageio.readers.bioformats_reader as br
from aicsimageio.writers import OmeTiffWriter

def test15():
    file = br.BioformatsReader("../resources/Threshold3.4UserAveragedC1E1.tif")
    OmeTiffWriter.save(file.data, "test.tif", physical_pixel_sizes=file.physical_pixel_sizes)    
    
    with TiffFile("../resources/E1.tif") as tiff:
        print(tiff.ome_metadata)
    
    with TiffFile("test.tif") as tiff:
        print(tiff.ome_metadata)

def test16():
    file_metadata = br.BioFile("../resources/Threshold3.4UserAveragedC1E1.tif")
    print(file_metadata.ome_metadata.images)

if __name__ == '__main__':
    test16()