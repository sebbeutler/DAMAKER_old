from PySide6.QtGui import QQuaternion, QVector4D, QVector3D

from pyqtgraph.opengl import GLVolumeItem, GLViewWidget, GLGridItem

import numpy as np
import damaker

from damaker.Channel import Channel, Channels
import damaker.processing
from damaker_gui.widgets.ITabWidget import IView

class Preview3DWidget(GLViewWidget, IView):
    name: str = "3D View"
    icon: str = u":/flat-icons/icons/flat-icons/cube.png"
    
    def __init__(self, parent=None, channels: Channels=None, name: str="Untitled"):
        super().__init__(parent)
                
        g = GLGridItem()
        g.scale(10, 10, 1)
        self.addItem(g)
        
        self.setCameraParams(rotation=QQuaternion(QVector4D(1., 1., 0., 0.)))        
        self.setCameraPosition(distance=1000)   
        
        if channels != None:
            self.setChannels(channels)
        
        self.name = f'[3D] {name}'
    
    def addChannel(self, chn: Channel):
        chn = chn.copy()
        lut: np.ndarray = chn.lut.getLookupTable(nPts=256)
        
        damaker.processing.resampleChannel(chn, chn.shape[2]  * chn.px_sizes.X, chn.shape[1]  * chn.px_sizes.Y, chn.shape[0]  * chn.px_sizes.Z)
        # damaker.processing._resamplePixelSize(chn, 1., 1., 1.)
        chn.data = chn.data.astype(np.ubyte)
        
        vol = np.zeros(chn.shape + (4,), dtype=np.ubyte)
        vol[:, :, :, 0] = lut[chn.data][...,0]
        vol[:, :, :, 1] = lut[chn.data][...,1]
        vol[:, :, :, 2] = lut[chn.data][...,2]
        vol[:, :, :, 3] = chn.data
        
        volumeItem = GLVolumeItem(vol, smooth=False, glOptions='additive')
        # volumeItem = GLVolumeItem(vol.swapaxes(0, 2))
        # volumeItem.rotate(180, 1, 0, 0)
        center = QVector3D(*[x/2. for x in vol.shape[:3]])
        volumeItem.translate(-center.x(), -center.y(), -center.z())
        self.addItem(volumeItem)        
        
        # ax = GLAxisItem(size=QVector3D(50, 200, 1), antialias=False, glOptions='additive')
        # self.addItem(ax)        
        
        # g = GLGridItem()
        # g.scale(100, 50, 1)
        # self.addItem(g)
        
    def setChannels(self, channels):        
        self.clear()
        for channel in channels:
            self.addChannel(channel)
    