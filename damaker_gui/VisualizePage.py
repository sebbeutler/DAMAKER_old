import numpy as np
import inspect, enum, re
from inspect import getmembers, isfunction, signature   

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

import damaker.processing
import damaker.utils
from damaker.Channel import Channel, Channels
from damaker.utils import StrFilePath, StrFolderPath
from damaker.pipeline import Operation, Pipeline
from damaker_gui.widgets.FunctionListWidget import FunctionsListWidget

from .widgets.PreviewWidget import *
from .windows.UI_MainWindow import Ui_MainWindow

def clearLayout(layout):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        if widgetToRemove != None:
            widgetToRemove.setParent(None)

class ChannelBtn(QPushButton):
    def __init__(self, name: str, chn: Channel, preview: PreviewWidget):
        super().__init__(name)
        self.channel = chn
        self.preview = preview
        
        self.setCheckable(True)
        self.setChecked(True)
        self.setFixedWidth(30)
        self.toggled.connect(self.toggleChannel)
    
    def toggleChannel(self, checked):
        self.channel.show = checked
        self.preview.updateFrame()

class VisualizePage:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.preview = PreviewWidget(self.ui.mainView, self.ui.slider_frame, [], self.ui.fileInfo)
        
        self.previewTop = PreviewWidget(self.ui.topView, None, [], self.ui.fileInfo)
        self.previewLeft = PreviewWidget(self.ui.leftView, None, [], self.ui.fileInfo)

        self.preview.signals.channelsChanged.connect(lambda: self.updateChannels())
        self.updateChannels()
        
        self.ui.slider_frame.valueChanged.connect(self.resliceViewsUpdate)
        self.preview.loadChannels = self.loadChannels
    
    def addChannels(self, chn):
        if type(chn) is list:
            for channel in chn:
                self.addChannels(channel)
            self.updateChannels()
            return
        def loadFrames(channel):
            if channel.data.dtype != np.uint8:
                channel.data = channel.data.astype(np.uint8)
            channel.frames = np.zeros(channel.shape + (3,), np.uint16)        
            channel.frames[:, :, :, 0] += channel.lut[:, 0][channel.data]
            channel.frames[:, :, :, 1] += channel.lut[:, 1][channel.data]
            channel.frames[:, :, :, 2] += channel.lut[:, 2][channel.data]   
             
        if chn.lut is None:
            chn.lut = luts[chn.id-1]
        
        chnTop = damaker.processing.resliceTop(chn)
        chnLeft = damaker.processing.resliceLeft(chn)
        
        print(chn.shape, chnTop.shape, chnLeft.shape)
        
        loadFrames(chn)
        loadFrames(chnTop)
        loadFrames(chnLeft)
        
        self.preview.channels.append(chn)
        self.previewTop.channels.append(chnTop)
        self.previewLeft.channels.append(chnLeft)
        
        self.preview.updateFrame()
        self.previewTop.updateFrame()
        self.previewLeft.updateFrame()
        
        self.functions = FunctionsListWidget()
        # self.functions.operationTriggered.connect(lambda name: self.functionListClicked(name))
        # self.ui.visualize_functionList.layout().addWidget(self.functions)
    
    def updateChannels(self):
        clearLayout(self.ui.channelList_layout)
        for chn in self.preview.channels:
            btn = ChannelBtn(f'Ch{chn.id}', chn, self.preview)
            self.ui.channelList_layout.addWidget(btn)
        self.ui.channelList_layout.addStretch()
    
    def resliceViewsUpdate(self):
        if len(self.preview.channels) == 0:
            return
        frame_id = self.preview.slider.value() / self.preview.channel.shape[0]
        self.previewTop.updateFrame(int(frame_id * self.previewTop.channel.shape[0]))
        self.previewLeft.updateFrame(int(frame_id * self.previewLeft.channel.shape[0]))
    
    def loadChannels(self, filename: str):
        fw = FileLoaderWorker(filename)
        fw.signals.loaded.connect(self.addChannels)
        self.preview.threadpool.start(fw)
        