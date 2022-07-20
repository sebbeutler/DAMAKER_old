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
    def __init__(self, parent=None):
        super().__init__(parent)
        QDockWidget.isAreaAllowed
        
        g = GLGridItem()
        g.scale(10, 10, 1)
        self.addItem(g)
        
        self.setCameraPosition(distance=1000)
        
    
    def addChannel(self, chn: Channel):
        print("Converting channels into 3D view: ", end='')
        
        chn = chn.copy()
        lut: np.ndarray = chn.lut.getLookupTable(nPts=256)
        
        # damaker.processing.resampleChannel(chn, chn.shape[2], chn.shape[1], chn.shape[0])
        # damaker.processing._resamplePixelSize(chn, 1., 1., 1.)
        chn.data = chn.data.astype(np.ubyte)
        
        vol = np.zeros(chn.shape + (4,), dtype=np.ubyte)
        vol[:, :, :, 0] = lut[chn.data][...,0]
        vol[:, :, :, 1] = lut[chn.data][...,1]
        vol[:, :, :, 2] = lut[chn.data][...,2]
        vol[:, :, :, 3] = chn.data
        
        volumeItem = GLVolumeItem(vol)
        # volumeItem = GLVolumeItem(vol.swapaxes(0, 2))
        # volumeItem.rotate(180, 1, 0, 0)
        volumeItem.translate(-50, -250, -50)
        self.addItem(volumeItem)
        
        
        ax = GLAxisItem(size=QVector3D(50, 200, 1), antialias=False, glOptions='opaque')
        self.addItem(ax)
        
        
        g = GLGridItem()
        g.scale(100, 50, 1)
        self.addItem(g)
        
        print("✔")
    
    