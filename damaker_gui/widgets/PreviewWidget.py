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

luts = [lut_red, lut_green, lut_blue]

class PreviewWidget(QGraphicsScene):
    def __init__(self, view: QGraphicsView, slider: QSlider, channels: list, fileInfo=None, channel_id=None, frame_id=0):
        super().__init__()

        self.channels = channels        
        self.slider = slider       
        
        self.fileInfo = fileInfo
        self.channel_id = channel_id
        self.frame_id = frame_id
        self.image = QGraphicsPixmapItem()
        self.addItem(self.image)
        
        self.view = view
        self.view.mouseMoveEvent = lambda e: self.mouseMoved(e)
        self.view.setMouseTracking(True)
        self.view.setScene(self)
        
        self.reset(channels)
        
        
        self.threadpool = QThreadPool()
        
    @property
    def channel(self):
        if self.channel_id is None:
            return self.channels[0]
        return self.channels[self.channel_id]

    @property
    def frame(self):
        return self.channel.data[self.frame_id]
    
    def reset(self, channels):  
        if channels is None:
            return
        
        self.channels = channels
        
        self.slider.setMinimum(0)
        self.slider.setMaximum(self.channel.shape[0]-1)
        self.slider.setValue(0)
        self.slider.setTracking(True)
        # self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.update)        
        
        self.view.setFixedSize(self.channel.shape[2], self.channel.shape[1])
        self.setFrame(self.channel.data[0])
        
        if self.fileInfo != None:
            self.fileInfo.preview = self
            self.fileInfo.update()
        
    
    def setFrame(self, frame: np.ndarray):
        self.image.setPixmap(QPixmap.fromImage(qimage2ndarray.array2qimage(frame)))
    
    def update(self):
        self.frame_id = self.slider.value()
        # self.setBackgroundBrush(Qt.darkBlue)
        
        frame = np.zeros((self.channel.shape[1],self.channel.shape[2], 3), np.int16)
        
        for chn in self.channels:
            if chn.lut is None:
                chn.lut = luts[chn.id]
            frame[:, :, 0] += chn.lut[:, 0][chn.data[self.frame_id]]
            frame[:, :, 1] += chn.lut[:, 1][chn.data[self.frame_id]]
            frame[:, :, 2] += chn.lut[:, 2][chn.data[self.frame_id]]        
        
        self.setFrame(frame.clip(0, 255))
        if self.fileInfo != None:
            self.fileInfo.update()
    
    def loadChannels(self, filename: str):
        fw = FileLoaderWorker(filename)
        fw.signals.loaded.connect(self.reset)
        self.threadpool.start(fw)
    
    def mouseMoved(self, event):
        m_pos: QPoint = event.pos()
        self.fileInfo.mx = m_pos.x()
        self.fileInfo.my = m_pos.y()
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
        