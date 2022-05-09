import math
from aicsimageio import AICSImage
from vedo import *
from vedo.picture import Picture
import numpy as np
from vedo.applications import *
from aicsimageio.writers import OmeTiffWriter
from tiffile import *
from utils import *
from processing import *
import cv2
from vedo.pyplot import plot as vplot
from vedo.pyplot import PlotBars
import os
import time

import vedo

import aicsimageio.readers.bioformats_reader as br
from aicsimageio.writers import OmeTiffWriter

_cube = np.array([
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
    ])

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
    
def test17():
    chn = openTiff("../resources/E1.tif")[0]
    print(chn.px_sizes)
    chn.save("test.tif")
    chn = openTiff("test.tif")[0]
    print(chn.px_sizes)

def test18():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    pl = Plotter()
    pl.add(Picture(chn.data.max(0)))
    pl.show()

def test19():
    arr = np.array([ 
        [
            [0, 1, 2],
            [3, 4, 5]
        ],
        [
            [0, 8, 0],
            [5, 0, 19]
        ]
    ])
    
    print(arr.max(1))

def test20():
    arr1 = np.full((100, 100), 255)
    
    arr2 = np.zeros((100, 100))
    arr2[25:75, 25:75] = 255
    
    arr3 = np.where(arr2 == 0, 0, arr1)
    
    plotFrame(arr1)
    plotFrame(arr2)
    plotFrame(arr3)

def test21():
    chns = openTiff("../resources/E1.tif")
    operatorADD(chns[0], chns[1])
    
    plot(chns[0])

def test22():
    a = np.array([0, 255, 255], dtype=np.uint8)
    b = np.array([0, 1, 1], dtype=np.uint8)
    a = a.astype(np.uint16)
    a += b
    a = a.clip(0, 255)
    print(a)

def test23():
    chns = openTiff("../resources/E1.tif")
    operatorNOT(chns[0], chns[1], 15)
    
    plot(chns[0])

def test24():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    plotFrame(zProjectionMax(chn))
    plotFrame(zProjectionMean(chn))

def test25():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn2 = chn.copy()
    chn2.channel = 1
    saveChannels("test.tif", [chn, chn2])

def test26():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    plot(chn)
    plotFrame(zProjectionMax(chn))
    plotFrame(zProjectionMean(chn))

def test27():
    chn1 = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn2 = openTiff("../resources/Threshold3.4UserAveragedC1E3.tif")[0]
    
    chn1.invert()
    chn2.invert()
    
    chn1.channel = 0
    chn2.channel = 1
    
    saveChannels("test.tif", [chn1, chn2])
    
    result = openTiff("test.tif")
    plot(result[0])
    plot(result[1])

def test28():
    chn1 = openTiff_tiffile("../resources/E1.tif")[0]
    
    img = chn1.data[55]
    
    img = np.array(img, dtype=np.float16)
    
    img -= 50
    contrast = 100
    pmin = 148
    pmax = 255
    p_range = pmax - pmin
    
    img[img < 148] = 0
    # img = np.where(img != 0, (img / 255) * p_range + pmin, img)
    
    plotFrame(img)

def test29():
    chn1 = openTiff_tiffile("../resources/E1.tif")[0]
    
    img = chn1.data[55]
    
    img = np.array(img, dtype=np.float16)
    
    def contrast(c):
        return (259*(c + 255)) / (255*(259 - c))

    f = contrast(150)
    
    img += 100
    img = f*(img - 128) + 128
    
    img = img.clip(0, 255)    
    img = img.astype(np.uint8)
    
    plotFrame(img)

def test30():
    
    chn1 = openTiff_tiffile("../resources/E1.tif")[0]
    changeBrightnessAndContrast(chn1, -50, -75)
    plot(chn1)

def test31():
    chn1 = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn1.invert()
    
    chn2 = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E2.tif")[0]
    chn2.invert()
    
    chn3 = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E3.tif")[0]
    chn3.invert()
    
    chn_res = averageChannels(chn1, chn2, chn3)
    
    plot(chn_res)
    
    thresholdChannel(chn_res, 200, 255)
    
    plot(chn_res)

def test32():
    s = time.time()
    chn = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    metadata = br.BioFile("../resources/Threshold3.4UserAveragedC1E1.tif").ome_metadata
    e = time.time()
    print(e - s)
    
    # s1 = time.time()
    # chn = openTiff("../resources/Threshold3.4UserAveragedC1E2.tif")[0]
    # e1 = time.time()
    # print(e1 - s1)

def test33():
    chn = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    metadata = br.BioFile("../resources/Threshold3.4UserAveragedC1E1.tif").ome_metadata
    
    s_x = metadata.images[0].pixels.physical_size_x
    s_y = metadata.images[0].pixels.physical_size_y
    s_z = metadata.images[0].pixels.physical_size_z
    
    Z, Y, X = chn.shape
    
    print(s_x, s_y, s_z)
    print(Z, Y, X)
    
    reslice = np.swapaxes(chn.data, 0, 1)
    
    img = reslice[55]
    
    reslice = cv2.resize(img, (X, int(Z*s_z/s_x)), interpolation=cv2.INTER_CUBIC)
    plotFrame(reslice)

def test34():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    plot(resliceTop(chn))

def test35():
    a = np.array([ [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] ])
    cv2.resize(a, (2, 2, 2))

def test36():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    chn1 = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E2.tif")[0]
    chn1.invert()
    
    def getrgb(arr, col):
        rgb = np.zeros((arr.shape[0], arr.shape[1], arr.shape[2], 3))
        rgb[:, :, :, col] = arr[:, :, :]
        return rgb
    
    red = getrgb(chn.data, 0)
    green = getrgb(chn1.data, 1)
    
    res = red.astype(np.uint16) + green.astype(np.uint16)
    res = res.clip(0, 255)
    
    chn.data = res
    plot(chn)

def test37():
    chn = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    chn1 = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E2.tif")[0]
    chn1.invert()
    
    resA = operatorAND(chn, chn1)
    
    plotRGB(resA)

def test38():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    plot(resliceLeft(chn))

def test39():
    chn = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    
    plot(chn)
    chn.data = chn.data[::-1]
    plot(chn)

def getTag(tags, currTag, z, y, x, s_z, s_y, s_x):
    result = currTag
    if z != 0:
        for t_y in range( max(0, y-1), min(s_y, y+2) ):
            for t_x in range( max(0, x-1), min(s_x, x+2) ):
                tag = tags[z-1, t_y, t_x]
                if tag != 0 and (tag < result or result == 0):
                    result = tag
    
    for t_x in range( max(0, x-1), min(s_x, x+2) ):
        if y-1 >= 0:
            tag = tags[z, y - 1, t_x]
            if tag != 0 and (tag < result or result == 0):
                result = tag
    
    if x-1 >= 0:
        tag = tags[z, y, x-1]
        if tag != 0 and (tag < result or result == 0):
            result = tag
    
    return result            
    

def test40():
    chn = openTiff_tiffile("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    data = chn.data
    
    # Z=1.237393717277487, Y=0.568182463843709, X=0.568182463843709
    
    # data = np.array([
    #     [
    #         [2, 4, 0, 1, 5],
    #         [4, 1, 0, 1, 5],
    #         [2, 2, 4, 0, 1],
    #         [2, 4, 1, 0, 4],
    #         [5, 2, 1, 4, 4]
    #     ],
    #     [
    #         [2, 4, 2, 2, 5],
    #         [4, 1, 0, 1, 5],
    #         [2, 2, 4, 0, 1],
    #         [2, 4, 1, 0, 4],
    #         [5, 2, 2, 4, 4]
    #     ]
    # ])
    
    tags = np.zeros_like(data)
    
    s_z, s_y, s_x = data.shape
    
    threshold = 2    
    tag_count = 1
    for z in range(s_z):
        for y in range(s_y):
            for x in range(s_x):
                if data[z, y, x] >= threshold:
                    tag = getTag(tags, tags[z, y, x], z, y, x, s_z, s_y, s_x)
                    if tag == 0:
                        tags[z, y, x] = tag_count
                        tag_count += 1
                    else:
                        tags[z, y, x] = tag
    
    print(tag_count)

from scipy import ndimage

def test41():
    data = np.array([
        [
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0]
        ]
    ])
    
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    data = chn.data
    
    l, n = ndimage.label(data, np.ones((3, 3, 3)))
    
    f = ndimage.find_objects(l)
    
    count = []
    
    for i in range(len(f)):
        count.append(np.count_nonzero(l[f[i]] == i+1))
    
    count = np.array(count)
    print(count[count >= 10].shape)
    print(count[count >= 10].sum() * 1.237 *0.56 *0.56)
    
    
    data = resliceLeft(chn).data
    
    l, n = ndimage.label(data, np.ones((3, 3, 3)))
    
    f = ndimage.find_objects(l)
    
    count = []
    
    for i in range(len(f)):
        count.append(np.count_nonzero(l[f[i]] == i+1))
    
    count = np.array(count)
    print(count[count >= 10].shape)
    print(count[count >= 10].sum() * 0.56 *0.56 *0.56)

def test42():
    data = np.array([
        [
            [1, 0, 1],
            [0, 1, 0],
            [0, 0, 1]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [1, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    ])
    
    l, n = ndimage.label(data, np.ones((3, 3, 3)))
    print(l)

def test43():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    z, x, y = (chn.px_sizes.Z, chn.px_sizes.Y, chn.px_sizes.X)
    
    print(np.count_nonzero(chn.data[25]) * z * y * x)

    
def test44():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    # chn = resliceTop(chn)
    
    vol = channelVolumeArray(chn)
    volumeSaveCSV("testE1.csv", vol)

def test45():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    # vol1 = channelVolumeArray(chn)
    
    top = resliceTop(chn)
    vol2 = channelVolumeArray(top)
    
    # left = resliceLeft(chn)
    # vol3 = channelVolumeArray(left)
    
    vplot(vol2).show()

def test46():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    chn.invert()
    
    objs = channelTotalVolume(chn, 10)
    for i in objs:
        print(i)
    

def test47():
    
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    
    vol = Volume("../resources/Threshold3.4UserAveragedC1E1.tif", spacing=(chn.px_sizes.X, chn.px_sizes.Y, chn.px_sizes.Z))
    mesh = vol.topoints()
    # mesh.show()
    # vol.show()
    vedo.write(mesh, "test.obj")

def test48():
    arr = np.array([
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
    ])
    
    err = ndimage.binary_erosion(arr)
    
    res = np.where(err == 1, 0, arr)
    print(res)

def test49():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    
    err = ndimage.binary_erosion(chn.data, iterations=3)
    
    vol = Volume(np.where(err > 0, 0, chn.data), spacing=(chn.px_sizes.X, chn.px_sizes.Y, chn.px_sizes.Z))
    mesh = vol.topoints()
    vedo.write(mesh, "test.obj")
    mesh.show()

from skimage import measure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

def test50():
    
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E2.tif")[0]
    
    chn.data = np.insert(chn.data, 0, np.zeros_like(chn.data[0]), axis=0)
    chn.data = np.insert(chn.data, -1, np.zeros_like(chn.data[0]), axis=0)
    
    
    chn.data = np.insert(chn.data, 0, np.zeros_like(chn.data[:, 0, :]), axis=1)
    chn.data = np.insert(chn.data, -1, np.zeros_like(chn.data[:, 0, :]), axis=1)
    
    
    chn.data = np.insert(chn.data, 0, np.zeros_like(chn.data[:, :, 0]), axis=2)
    chn.data = np.insert(chn.data, -1, np.zeros_like(chn.data[:, :, 0]), axis=2)
    
    # plot(chn)
    verts, faces, normals, values = measure.marching_cubes(chn.data, int(255/4), spacing=(chn.px_sizes.Z, chn.px_sizes.Y, chn.px_sizes.X))    
    mcubes.export_obj(verts, faces, "testE2.obj")
    
    # vedo.load("test.obj").show()
    
import mcubes

def test51():
    arr = np.array([        
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ])
    
    vertices, triangles = mcubes.marching_cubes(arr, 0)
    mcubes.export_obj(vertices, triangles, "test5.obj")
    vedo.load("test5.obj").show()

def test52():
    arr = np.array([
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
    ])
    
    # res = ndimage.affine_transform(arr)
    print(cv2.scale)

def test53():
    chn = openTiff_hybrid("../resources/Threshold3.4UserAveragedC1E1.tif")[0]
    
    vol = Volume(chn.data, spacing=(chn.px_sizes.X, chn.px_sizes.Y, chn.px_sizes.Z))
    vol.show()
    
def test54():
    vedo.load("test1.obj").show()

import vispy.geometry.isosurface
from vispy import app, scene

def test55():
    verts, faces = vispy.geometry.isosurface.isosurface(_cube, 0)
    
    print(verts)
    # mcubes.export_obj(verts, faces, "test4.obj")
    # vedo.load("test4.obj").show()
    
    canvas = scene.SceneCanvas(keys='interactive')
    view = canvas.central_widget.add_view()
    surface = scene.visuals.Isosurface(_cube, color=(0.5, 0.6, 1, 1), shading='smooth', parent=view.scene)
    axis = scene.visuals.XYZAxis(parent=view.scene)
    cam = scene.TurntableCamera(elevation=30, azimuth=30)
    cam.set_range((-10, 10), (-10, 10), (-10, 10))
    view.camera = cam
    canvas.show()
    app.run()

def test56():
        
    obj1: Mesh = Mesh("../resources/Threshold3.4UserAveragedC1E1.tif.obj").mirror("z").extractLargestRegion()
    obj2: Mesh = Mesh("s2E1.obj").rotateY(90).extractLargestRegion()
    
    obj1.distanceTo(obj2, signed=True)
    obj1.cmap(input_array="Distance", cname="seismic")
    obj1.addScalarBar(title='Distance')
    obj1.show()

def test57():    
    colors = []
    for i in np.linspace(-80, 80):
        c = colorMap(i, name='seismic', vmin=-80, vmax=80)
        if abs(i) < 5:
            c = 'white'
        colors.append([i, c])

    lut = buildLUT(
        colors,
        vmin=-80,
        vmax=80,
        interpolate=True)
     
    obj2 = Mesh("s2E1.obj").rotateY(90)
    # obj2 = Mesh("s2E1.obj").rotateY(90).extractLargestRegion()
    # obj1 = Mesh("../resources/Threshold3.4UserAveragedC1E1.tif.obj").mirror("z").extractLargestRegion()
    obj1 = Mesh("../resources/Threshold3.4UserAveragedC1E1.tif.obj").mirror("z")
    
    obj1.distanceTo(obj2, signed=True)
    obj1.cmap(input_array="Distance", cname=lut)
    obj1.addScalarBar(title='Distance')
    
    obj1.show()
    
    vplot(obj1.pointdata["Distance"]).show()

def test59():
    chn = openTiff_hybrid("../resources/batch/User1C2E1.tif")[0]   
    channelSaveToObj(chn, "E1_old.obj", 1) 
    # chn = openTiff_hybrid("../resources/batch/User1C2E2.tif")[0]    
    # channelSaveToObj(chn, "E2_.obj", 1) 
    # chn = openTiff_hybrid("../resources/batch/User1C2E3.tif")[0]    
    # channelSaveToObj(chn, "E3_.obj", 1) 
     
if __name__ == '__main__':
    test59()
    