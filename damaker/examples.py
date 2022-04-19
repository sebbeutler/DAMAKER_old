from processing import *
from vedo.pyplot import plot as vedoplot


def ex_openTiff():
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    plot(chn)

def ex_openMultipleChannelTiff():
    chn = openTiff("../resources/E1.tif")
    plot(chn[0])
    plot(chn[1])

def ex_transformations():    
    chn = openTiff("../resources/Threshold3.4UserAveragedC1E1.tif")
    
    chn.invert()
    
    rotate(chn, 30, "nearest")
    
    rotate180(chn)
    
    crop(chn, (100, 100), (400, 600))
    
    flipVertically(chn)
    
    plot(chn)

def ex_pixelIntensity():
    chn = openTiff("../resources/E1.tif")[0]
    
    px_int = pixelIntensity(chn)
    px_int[100] = 0
    vedoplot(px_int).show()

if __name__ == '__main__':
    # ex_openTiff()
    # ex_openMultipleChannelTiff()
    ex_transformations()
    # ex_pixelIntensity()