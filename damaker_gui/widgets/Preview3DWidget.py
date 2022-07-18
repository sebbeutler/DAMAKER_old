from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from pyqtgraph.opengl import GLVolumeItem, GLViewWidget, GLGridItem, GLAxisItem
import pyqtgraph as pg

import numpy as np
import damaker

from damaker.Channel import Channel
import damaker.processing

class Preview3DWidget(GLViewWidget):
    def __init__(self):
        super().__init__()
        
        g = GLGridItem()
        g.scale(10, 10, 1)
        self.addItem(g)
        
        ax = GLAxisItem()
        self.addItem(ax)
        self.setCameraPosition(distance=1000)
        
    
    def addChannel(self, chn: Channel):
        chn = chn.copy()
        lut: np.ndarray = chn.lut.getLookupTable(nPts=256)
        
        damaker.processing.resampleChannel(chn, chn.shape[2], chn.shape[1], int(500))
        chn.data = chn.data.astype(np.ubyte)
        
        vol = np.zeros(chn.shape + (4,), dtype=np.ubyte)
        vol[:, :, :, 0] = lut[chn.data][...,0]
        vol[:, :, :, 1] = lut[chn.data][...,1]
        vol[:, :, :, 2] = lut[chn.data][...,2]
        vol[:, :, :, 3] = chn.data
        
        
        # vol = np.array([ 
        #                 [[[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],
        #                  [[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],
        #                  [[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],],
        #                 [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
        #                  [[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],
        #                  [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],],
        #                 [[[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],
        #                  [[255,255,255,255],[0,0,0,0],[0,0,0,0],[255,255,255,255]],
        #                  [[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],]
        #                 ], dtype=np.ubyte)
        
        volumeItem = GLVolumeItem(vol.swapaxes(0, 2))
        volumeItem.rotate(180, 1, 0, 0)
        volumeItem.translate(-chn.shape[2]/2,-chn.shape[1]/2, -chn.shape[0]/2)
        self.addItem(volumeItem)
    
    