import numpy as np
import inspect, enum, re, gc
from inspect import getmembers, isfunction, signature   

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from vedo import Mesh

import damaker.processing
import damaker.utils
from damaker.Channel import Channel, Channels, SingleChannel
from damaker.utils import NamedArray, StrFilePath, StrFolderPath
from damaker.pipeline import BatchParameters, Operation, Pipeline
from damaker_gui.widgets.BatchSelectionWidget import BatchSelectionWidget
from damaker_gui.widgets.EnumComboBox import EnumComboBox
from damaker_gui.widgets.FilePickerWidget import FilePickerWidget, FolderPickerWidget
from damaker_gui.widgets.FunctionListWidget import FunctionsListWidget
from damaker_gui.widgets.FunctionParametersWidget import FunctionParametersWidget

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
        
        self.functions = FunctionsListWidget()
        self.functions.operationTriggered.connect(lambda name: self.functionMenuClicked(name))
        self.ui.visualize_functionListLayout.addWidget(self.functions)
        
        self.functionParameters = FunctionParametersWidget()
        self.ui.visualize_functionListLayout.addWidget(self.functionParameters)
        
        self.ui.visualize_btn_addChannel.clicked.connect(self.addFile)
    
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
            
            
        self.ui.label_appState.setText("Reslicing ...")

        chn.id = len(self.preview.channels) + 1
             
        if chn.lut is None:
            chn.lut = luts[chn.id-1]
        
        chnTop = damaker.processing._resliceTop(chn)
        chnLeft = damaker.processing._resliceLeft(chn)
        
        # loadFrames(chn)
        # loadFrames(chnTop)
        # loadFrames(chnLeft)
        
        # print("Lut done.")
        
        self.preview.channels.append(chn)
        self.previewTop.channels.append(chnTop)
        self.previewLeft.channels.append(chnLeft)
        
        self.preview.updateFrame()
        self.previewTop.updateFrame()
        self.previewLeft.updateFrame()
        
        self.ui.label_appState.setText("Loading complete.")

    
    def updateChannels(self):
        clearLayout(self.ui.visualize_layout_channelList)
        for chn in self.preview.channels:
            btn = ChannelBtn(f'Ch{chn.id}', chn, self.preview)
            self.ui.visualize_layout_channelList.addWidget(btn)
        # self.ui.visualize_layout_channelList.addStretch()
    
    def resliceViewsUpdate(self):
        if len(self.preview.channels) == 0:
            return
        frame_id = self.preview.slider.value() / self.preview.channel.shape[0]
        self.previewTop.updateFrame(int(frame_id * self.previewTop.channel.shape[0]))
        self.previewLeft.updateFrame(int(frame_id * self.previewLeft.channel.shape[0]))
    
    def loadChannels(self, filename: str):
        self.preview.channels.clear()
        self.previewTop.channels.clear()
        self.previewLeft.channels.clear()
        
        gc.collect()
        
        self.ui.label_appState.setText("Loading file")
        fw = FileLoaderWorker(filename)
        fw.signals.loaded.connect(self.addChannels)
        self.preview.threadpool.start(fw)
    
    def addFile(self, event):
        filename = QFileDialog.getOpenFileName(None, 'Open file', 
         self.ui.fileSystemModel.rootPath(),"Any (*.*)")[0]
        self.ui.label_appState.setText("Loading file")
        fw = FileLoaderWorker(filename)
        fw.signals.loaded.connect(self.addChannels)
        self.preview.threadpool.start(fw)
        
    def functionMenuClicked(self, name):
        self.functionParameters.clearLayouts()
        self.functionParameters.ui.edit_operation_name.setHidden(False)
        self.functionParameters.ui.checkbox_enabled.setHidden(False)
        self.functionParameters.ui.btn_add_operation.setHidden(True)
        self.functionParameters.ui.btn_modify_operation.setHidden(False)
        
        func = self.functions.getFunction(name)
        if func == None:
            return
        self.functionParameters.ui.currentFunction.setText(name)
        sign = signature(func)
        self.functionParameters.ui.edit_operation_name.setText(func.__name__)
        self.functionParameters.ui.checkbox_enabled.setChecked(True)
        
        if sign.return_annotation in [Channel, Channels, NamedArray]:
            self.functionParameters.outputDir.setHidden(False)
            self.functionParameters.outputDir.setText("")
        else:
            self.functionParameters.outputDir.setHidden(True)
        
        for name in sign.parameters:
            param = sign.parameters[name]
            if param.annotation == inspect._empty:
                continue
            
            default_arg = None
            if param.default != inspect._empty:
                default_arg = param.default   
            
            label = QLabel(name)
            label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
            label.setFixedHeight(25)
            self.functionParameters.ui.layout_fnames.addWidget(label)
                
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if default_arg != None:
                    spinBox.setValue(int(default_arg))
                else:
                    spinBox.setValue(0)
                self.functionParameters.ui.layout_fargs.addWidget(spinBox)
            if param.annotation is float:
                spinBox = QDoubleSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if default_arg != None:
                    spinBox.setValue(float(default_arg))
                else:
                    spinBox.setValue(0.0)
                self.functionParameters.ui.layout_fargs.addWidget(spinBox)
            elif param.annotation in [Channel, Channels, BatchParameters, Mesh]:
                self.functionParameters.ui.layout_fargs.addWidget(BatchSelectionWidget(self.ui.fileSystemModel.rootPath()))
            elif param.annotation is SingleChannel:
                self.functionParameters.ui.layout_fargs.addWidget(FilePickerWidget(self.ui.fileSystemModel.rootPath()))
            elif param.annotation is StrFilePath:
                self.functionParameters.ui.layout_fargs.addWidget(FilePickerWidget(self.ui.fileSystemModel.rootPath()))
            elif param.annotation is StrFolderPath:
                self.functionParameters.ui.layout_fargs.addWidget(FolderPickerWidget(self.ui.fileSystemModel.rootPath()))
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setFixedHeight(18)
                if default_arg != None:
                    textEdit.setText(default_arg)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.functionParameters.ui.layout_fargs.addWidget(textEdit)
            elif type(param.annotation) is type(enum.Enum):
                self.functionParameters.ui.layout_fargs.addWidget(EnumComboBox(param.annotation))
            elif param.annotation is bool:
                checkBox = QCheckBox("")
                if default_arg != None:
                    checkBox.setChecked(default_arg)
                self.functionParameters.ui.layout_fargs.addWidget(checkBox)