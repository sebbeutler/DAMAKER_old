from PySide2.QtWidgets import QSlider, QGraphicsSceneMouseEvent, QSizePolicy, QLabel, QGraphicsSceneDragDropEvent
from PySide2.QtGui import QMouseEvent, QPainter
from PySide2.QtCore import Signal, QPointF, QThreadPool, QPoint, QObject, QRunnable, QThread, Slot

import pyqtgraph as pg

import numpy as np
import damaker

from damaker.Channel import Channel
from damaker.utils import loadChannelsFromFile
# from damaker_gui.widgets import clearLayout

from damaker_gui.windows import files_rc

lut_green = np.zeros((256, 3), np.uint8)
lut_green[:, 1] = np.arange(256)

lut_red = np.zeros((256, 3), np.uint8)
lut_red[:, 0] = np.arange(256)

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

lut_pos = np.arange(0, 1+1/255, 1/255)

_luts = [pg.ColorMap(lut_pos, lut_green, name='green'),
         pg.ColorMap(lut_pos, lut_red, name='red'),
         pg.ColorMap(lut_pos, lut_blue, name='blue'),
         pg.ColorMap(lut_pos, lut_yellow, name='yellow'),
         pg.ColorMap(lut_pos, lut_cyan, name='cyan'),
         pg.ColorMap(lut_pos, lut_magenta, name='magenta'),
         pg.ColorMap(lut_pos, lut_grays, name='grays')]

def getLut(name: str) -> pg.ColorMap:
    for lut in _luts:
        if lut.name == name:
            return lut
    return _luts[0] # Default

class PreviewWidget(pg.ImageView):  
    mouseMoved = Signal(QMouseEvent, QPointF)
    channelAdded = Signal()
    channelsChanged = Signal(str)
    
    def __init__(self, channels: list=[], fileInfo=None, slider: QSlider=None):
        super().__init__()

        self.threadpool = QThreadPool()

        self.fileInfo = fileInfo
        self.slider = slider
        self.frameId = 0
        self.shape = (0, 0, 0)
        
        self.view.state['wheelScaleFactor'] = -1.0 / 50.0
        self.view.sigRangeChangedManually.connect(lambda: self.updateTextInfo())
        
        if self.slider != None:
            self.slider.setRange(0, 1)
            self.slider.valueChanged.connect(self.updateFrame)
            self.slider.setTracking(True)     
        
        self.channels: dict[Channel, pg.ImageItem] = {}
        
        self.ui.histogram.hide()
        self.ui.roiBtn.hide()
        self.ui.menuBtn.hide()
        self.ui.roiPlot.setVisible(False)
        self.ui.roiPlot.hide()
        self.view.setBackgroundColor((32, 32, 32))   
        
        self.textInfo = QLabel("Slide: ", self)
        self.textInfo.setMinimumWidth(100)
        self.textInfo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.textInfo.setStyleSheet("color: rgb(125, 125, 125);")
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
    
        self.scene._mouseMoveEvent = self.scene.mouseMoveEvent
        self.scene.mouseMoveEvent = self.mouseMoveEvent
        
        self.updateFrame()
    
    @property
    def data(self) -> list[Channel]:
        return list(self.channels.keys())
    
    def enableCross(self, enable: bool):
        if enable:    
            self.addItem(self.vLine)
            self.addItem(self.hLine)
        else:            
            self.removeItem(self.vLine)
            self.removeItem(self.hLine)
    
    def updateFramePercentage(self, percentage):
        self.updateFrame(int(max(min(percentage, 1),0)*(self.shape[0]-1)))
        
    def updateFrame(self, frameId=None):        
        if self.slider != None:  
            self.frameId = self.slider.value()
        
        if frameId != None:
            self.frameId = frameId
        
        for chn, img in self.channels.items():
            img.setImage(chn.data[self.frameId], autoLevels=False)
        
        if self.fileInfo != None:
            self.fileInfo.update()
        
        self.updateTextInfo()
    
    def addChannels(self, channels: list[Channel]):
        if type(channels) == Channel:
            channels = [channels]
        if len(channels) == 0:
            return
        if self.shape == (0,0,0):
            self.shape = channels[0].shape
        for chn in channels:
            if chn.shape[1:] != self.shape[1:]:
                print("Channel dimension not valid")
                continue
            img = pg.ImageItem()
            img.axisOrder = 'row-major'
            if chn.lut is None:
                chn.lut = _luts[chn.id-1]
            img.setColorMap(chn.lut)
            img.setCompositionMode(QPainter.CompositionMode.CompositionMode_Plus)
            self.addItem(img)
            self.channels[chn] = img 
        
        # self.view.autoRange()
        self.channelAdded.emit()
    
    def clear(self):
        for chn, img in self.channels.items():
            self.removeItem(img)
            # chn.free()
        
        self.channels.clear()
        self.shape = (0,0,0)
    
    def reset(self, channels=[]):
        if channels is None or len(channels) == 0:
            return
        
        self.clear()
        self.addChannels(channels)
        
        self.sliderUpdateRange()

        if self.fileInfo != None:
            self.fileInfo.preview = self
            self.fileInfo.update()
        
        self.updateFrame(0)
        if len(self.channels) > 0:
            self.channelsChanged.emit(list(self.channels.keys())[0].name)
    
    def removeChannel(self, channel: Channel):
        if channel not in self.channels.keys():
            return
        self.removeItem(self.channels[channel])
        del self.channels[channel]      
    
    def loadFile(self, filename: str):
        print(f"loading {filename}")
        fw = FileLoaderWorker(filename)
        fw.signals.loaded.connect(self.reset)
        self.threadpool.start(fw)
    
    def loadFiles(self, files: list[str]):
        if type(files) is str:
            self.loadFile(files)
        elif type(files) is list:
            self.loadFile(files[0])
    
    def mouseMoveEvent(self, e: QGraphicsSceneMouseEvent):
        self.scene._mouseMoveEvent(e)      
        if len(self.channels) == 0:
            return
        m_pos = self.view.mapSceneToView(e.scenePos())
        
        if self.fileInfo != None:
            self.fileInfo.mx = int(max(0, m_pos.x()))
            self.fileInfo.my = int(max(0, m_pos.y()))
            self.fileInfo.preview = self
            self.fileInfo.update()
        self.mouseMoved.emit(e, m_pos)
    
    def updateTextInfo(self):
        vrange = self.view.viewRange()
        try:
            zoom = "%.2f" % ((((vrange[0][0] - vrange[0][1]) / self.shape[2]) + ((vrange[1][0] - vrange[1][1]) / self.shape[1])) * -1 / 2)
        except:
            zoom = ""
        self.textInfo.setText(f"Slide: {self.frameId+1}/{self.shape[0]} Zoom: {zoom}")
        self.textInfo.adjustSize()
        
    
    def viewMouseMoved(self, event: QMouseEvent):
        if self.sceneRect().contains(event.pos().x(), event.pos().y()):
            m_pos: QPoint = self.mapViewToScene(event.pos())
        else:
            m_pos = QPoint(0,0)
        self.fileInfo.mx = int(max(0, m_pos.x()))
        self.fileInfo.my = int(max(0, m_pos.y()))
        self.fileInfo.preview = self
        self.fileInfo.update()
        
        self.mouseMoved.emit(event, m_pos.x(), m_pos.y())
    
    def sliderUpdateRange(self):
        if self.slider != None:
            self.slider.setMinimum(0)
            self.slider.setMaximum(self.shape[0]-1)
            self.slider.setValue(0)
    
    @property
    def count(self):
        return len(self.channels.keys())
        
    
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
        channels = []
        if type(self.filename) is str:
            channels += loadChannelsFromFile(self.filename)
        elif type(self.filename) is list:
            for file in self.filename:
                channels += loadChannelsFromFile(file)
        if len(channels) == 0:
            self.signals.error.emit()
        else:
            self.signals.loaded.emit(channels)