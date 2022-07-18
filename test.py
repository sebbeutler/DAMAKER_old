from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from pyqtgraph.opengl import GLVolumeItem, GLViewWidget, GLGridItem, GLAxisItem
import pyqtgraph as pg

import numpy as np
import sys

class Preview3DWidget(GLViewWidget):
    def __init__(self):
        super().__init__()
        self.volumeItem = None
        
        g = GLGridItem()
        g.scale(10, 10, 1)
        self.addItem(g)
        
        ax = GLAxisItem()
        self.addItem(ax)
        self.setCameraPosition(distance=1000)
    
    def setChannel(self):                  
        # vol: np.ndarray = chn.data[:,:,:, np.newaxis]
        # vol = vol.astype(np.ubyte)
        
        # lut:pg.ColorMap = chn.lut
        # vol = lut.map(chn.data)
        
        
        vol = np.array([ 
                        [[[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],
                         [[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],
                         [[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],],
                        [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
                         [[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],
                         [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],],
                        [[[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],
                         [[255,255,255,255],[0,0,0,0],[0,0,0,0],[255,255,255,255]],
                         [[0,0,0,0],[255,255,255,255],[255,255,255,255],[0,0,0,0]],]
                        ], dtype=np.ubyte)
        
        if self.volumeItem is None:
            self.volumeItem = GLVolumeItem(vol)
            self.addItem(self.volumeItem)
        else:
            self.volumeItem.setData(vol)
        
    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        # self.paintGL()

app = QApplication(sys.argv)
w = Preview3DWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLScatterPlotItem')
app.exec_()