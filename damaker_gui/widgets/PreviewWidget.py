from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

import numpy as np
import qimage2ndarray

import sys
sys.path.insert(1, '../')

from damaker.Channel import Channel
from damaker.utils import loadChannelsFromFile

lut_red = np.zeros((256, 3), np.uint8)
lut_red[:, 0] = np.arange(256)

lut_green = np.zeros((256, 3), np.uint8)
lut_green[:, 1] = np.arange(256)

lut_blue = np.zeros((256, 3), np.uint8)
lut_blue[:, 2] = np.arange(256)

lut_yellow = np.zeros((256, 3), np.uint8)
lut_yellow[:, 0] = np.arange(256)
lut_yellow[:, 1] = np.arange(256)

lut_cyan = np.zeros((256, 3), np.uint8)
lut_cyan[:, 1] = np.arange(256)
lut_cyan[:, 2] = np.arange(256)

lut_magenta = np.zeros((256, 3), np.uint8)
lut_magenta[:, 0] = np.arange(256)
lut_magenta[:, 2] = np.arange(256)

lut_grays = np.zeros((256, 3), np.uint8)
lut_grays[:, 0] = np.arange(256)
lut_grays[:, 1] = np.arange(256)
lut_grays[:, 2] = np.arange(256)

luts = [lut_red, lut_green, lut_blue, lut_yellow, lut_cyan, lut_magenta, lut_grays]

class PreviewWidgetSignals(QObject):
    channelsChanged = Signal()
    
class PreviewWidget(QGraphicsScene):
    
    def __init__(self, view: QGraphicsView, slider: QSlider, channels: list=[], fileInfo=None, frame_id=0):
        super().__init__()

        self.signals = PreviewWidgetSignals()

        self.channels = channels        
        self.slider = slider  
        
        self.frame_id = frame_id
        
        self.fileInfo = fileInfo
        self.image = QGraphicsPixmapItem()
        self.addItem(self.image)
        
        self.view = view
        self.view.mouseMoveEvent = lambda e: self.viewMouseMoved(e)
        self.view.setMouseTracking(True)
        self.view.setScene(self)        
        self.view.wheelEvent = self.onScroll
        
        if self.slider != None:
            self.slider.valueChanged.connect(self.update)
            self.slider.setTracking(True)    
            # self.slider.setTickInterval(1)   
        
        self.threadpool = QThreadPool()
        
        
    @property
    def channel(self):
        if len(self.channels) > 0:
            return self.channels[0]
        return None

    @property
    def frame(self):
        return self.channel.data[self.frame_id]
    
    def reset(self, channels):
        if channels is None:
            return
        
        self.channels = channels
        
        if self.slider != None:
            self.slider.setMinimum(0)
            self.slider.setMaximum(self.channel.shape[0]-1)
            self.slider.setValue(0)        
            
        self.updateFrame()
        
        if self.fileInfo != None:
            self.fileInfo.preview = self
            self.fileInfo.update()
        
        self.image.setScale(1)
        self.signals.channelsChanged.emit()
    
    def updateFrame(self, id: int=None):
        if id == None:
            id = self.frame_id
        frame = sum([chn.frames[id] for chn in self.channels if chn.show])
        try:
            self.image.setPixmap(QPixmap.fromImage(qimage2ndarray.array2qimage(frame)))
        except:
            pass
    
    def recenter(self):        
        size = self.view.size()
        img_r = self.image.boundingRect()
        scale = self.image.scale()
        pos: QPointF = self.view.mapToScene(int(size.width()/2-img_r.width()*scale/2),int(size.height()/2-img_r.height()*scale/2))
        self.image.setPos(pos.x(), pos.y())        
        self.setSceneRect(pos.x(), pos.y(), int(img_r.width()*scale), int(img_r.height()*scale))
        
    def zoom(self, amount=0.1):        
        self.image.setScale(self.image.scale() + amount)
        self.recenter()
    
    def zoomIn(self):
        self.zoom(0.1)
    
    def zoomOut(self):
        self.zoom(-0.1)
    
    def onScroll(self, e: QGraphicsSceneWheelEvent):
        self.zoom(e.delta()/1200)
        
    def update(self):
        if self.slider != None:
            self.frame_id = self.slider.value()
        # self.setBackgroundBrush(Qt.darkBlue)   
        if len(self.channels) > 0:
            self.updateFrame()
        
        if self.fileInfo != None:
            self.fileInfo.update()
    
    def loadChannels(self, filename: str):
        fw = FileLoaderWorker(filename)
        fw.signals.loaded.connect(self.reset)
        self.threadpool.start(fw)
    
    def viewMouseMoved(self, event):
        m_pos: QPoint = self.view.mapToScene(event.pos())
        self.fileInfo.mx = int(max(0, m_pos.x()))
        self.fileInfo.my = int(max(0, m_pos.y()))
        self.fileInfo.preview = self
        self.fileInfo.update()
    
    def dropEvent(self, event: QGraphicsSceneDragDropEvent):
        super().dropEvent(event)
        
        if event.mimeData().hasUrls:
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.loadChannels(links[0])
        else:
            event.ignore()
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
    
class FileLoaderSignals(QObject):
    loaded = Signal(list)
    error = Signal()

class FileLoaderWorker(QRunnable):
    def __init__(self, filename: str):
        super(FileLoaderWorker, self).__init__()
        
        self.filename = filename
        self.signals = FileLoaderSignals()

    @Slot()
    def run(self):
        channels = loadChannelsFromFile(self.filename)
        if channels is None:
            self.signals.error.emit()
        else:
            self.signals.loaded.emit(channels)
        