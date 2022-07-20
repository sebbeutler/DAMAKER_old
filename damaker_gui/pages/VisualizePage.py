import inspect, enum, gc  
import numpy as np

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

# import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from vedo import Mesh

import damaker as dmk
import damaker_gui.widgets as widgets

from damaker_gui.widgets.PreviewWidget import _luts
from damaker_gui.windows.UI_MainWindow import Ui_MainWindow
from damaker_gui.pages.Page import Page

def clearLayout(layout):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        if widgetToRemove != None:
            widgetToRemove.setParent(None)

class ChannelBtn(QPushButton):
    channelToggled = Signal(QPushButton, int)
    channelRemoveTriggered = Signal(QPushButton, int)
    
    def __init__(self, name: str, chId: int):
        super().__init__(name)
        self.id = chId
        self.setCheckable(True)
        self.setChecked(True)
        self.setFixedWidth(30)
        self.toggled.connect(lambda: self.channelToggled.emit(self, self.id))
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        act = QAction("Remove", self)
        act.triggered.connect(lambda: self.channelRemoveTriggered.emit(self, self.id))
        self.addAction(act)

class VisualizePage(Page):
    def __init__(self, ui: Ui_MainWindow):
        super().__init__(ui)
        
        self.previewMain = widgets.PreviewWidget(slider=self.ui.slider_frame, fileInfo=self.ui.fileInfo)
        self.preview3D = widgets.Preview3DWidget()
        self.previewTop = widgets.PreviewWidget(fileInfo=self.ui.fileInfo)
        self.previewLeft = widgets.PreviewWidget(fileInfo=self.ui.fileInfo)
        
        self.resliceWorker = None
        
        self.ui.layout_mainPreview.addWidget(self.previewMain)
        self.ui.layout_tap_preview3D.addWidget(self.preview3D)
        self.ui.layout_topPreview.addWidget(self.previewTop)
        self.ui.layout_leftPreview.addWidget(self.previewLeft)
        
        self.previewMain.enableCross(True)
        self.previewMain.signals.channelsChanged.connect(lambda: self.updateBtnChannels())
        self.previewMain.signals.channelsChanged.connect(lambda: self.resetTabLUT()())
        
        self.previewMain.loadChannels = self.loadChannels
        
        self.functions = widgets.FunctionsListWidget()
        self.functions.operationTriggered.connect(lambda name: self.functionMenuClicked(name))
        self.ui.visualize_functionListLayout.addWidget(self.functions)
        
        self.functionParameters = widgets.FunctionParametersWidget()
        self.functionParameters.ui.btn_modify_operation.setText("Duplicate")
        self.functionParameters.ui.btn_modify_operation.clicked.connect(lambda: self.applyFunction(True))
        self.functionParameters.ui.btn_add_operation.setText("Apply")
        self.functionParameters.ui.btn_add_operation.clicked.connect(self.applyFunction)
        self.ui.visualize_functionListLayout.addWidget(self.functionParameters)
        
        self.ui.visualize_btn_addChannel.clicked.connect(self.addFile)
        
        self.figure = Figure(figsize=(0.5, 0.5))
        self.brightnessPlot = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.axes.plot([1, 2,3], [1, 2 ,3])
        # self.brightnessPlot.getFigure().delaxes(self.subplot)
        self.ui.tab_brightnesscontrast_layout.insertWidget(0, self.brightnessPlot)
        
        self.ui.slider_brightness.valueChanged.connect(self.updateBrightnessContrast)
        self.ui.slider_contrast.valueChanged.connect(self.updateBrightnessContrast)
        self.ui.slider_bc_min.valueChanged.connect(self.updateBrightnessContrastMinMax)
        self.ui.slider_bc_max.valueChanged.connect(self.updateBrightnessContrastMinMax)
        
        self.ui.contrast_apply.clicked.connect(self.applyBrightnessContrast)
        self.ui.contrast_reset.clicked.connect(self.resetBrightnessContrast)
        
        self.previewMain.slider.sliderReleased.connect(self.updatePxInt)
        
        self.previewMain.mouseMoved.connect(self.moveCross)
        
        self.ui.tab_views_addBtn.clicked.connect(self.newView)
        self.ui.visualize_viewsList.currentItemChanged.connect(self.viewsItemChanged) 
        self.ui.visualize_viewsList.addItem("View1") 
        self.ui.visualize_viewsList.setItemSelected(self.ui.visualize_viewsList.item(0), True)
        self.viewsCount = 1
        self.views = {"View1": []}
        self.viewTabs = {}
        self.currentViewName = "View1"
        self.addAnnexTab("View1")
        
        self.recorder = widgets.RecordFunctionsWidget(self.ui.tab_record_layout)
        
        self.updateBtnChannels()
        self.resetTabLUT()
        
        self.loadChannels("C:/Users/PC/source/DAMAKER/resources/prev_pipeline/out-reg/E1_C2.tif")
        # self.loadChannels("C:/Users/Seb/Documents/docs/uni/stage/DAMAKER/resources/test/Threshold3.4UserAveragedC1E1.tif")
    
    class LUTComboBox(QComboBox):
        def __init__(self, channel, _callback):
            super().__init__()
            self.channel = channel
            self._callback = _callback
        
        def updateChannelLUT(self, text):
            for lut in _luts:
                if lut.name == text:
                    self._callback(self.channel, lut)
    
    def resetTabLUT(self):
        for i in reversed(range(self.ui.layout_tab_LUT.rowCount())):
            self.ui.layout_tab_LUT.removeRow(i)
        
        for chn in self.currentView:
            comboBox = VisualizePage.LUTComboBox(chn, self.setChannelLUT)
            for lut in _luts:
                comboBox.addItem(lut.name)
            comboBox.setCurrentText(chn.lut.name)
            comboBox.currentTextChanged.connect(comboBox.updateChannelLUT)
            self.ui.layout_tab_LUT.addRow("Channel %d :" % chn.id, comboBox)
    
    def setChannelLUT(self, channel, colorMap):
        channel.lut = colorMap
        if channel in self.previewMain.channels.keys():
            self.previewMain.channels[channel].setColorMap(channel.lut)
        
        for chn in self.previewTop.channels.keys():
            if chn.id == channel.id:
                self.previewTop.channels[chn].setColorMap(channel.lut)
        for chn in self.previewLeft.channels.keys():
            if chn.id == channel.id:
                self.previewLeft.channels[chn].setColorMap(channel.lut)
        
        self.updateFrames()
        
    def updateBrightnessContrastMinMax(self):
        _min = self.ui.slider_bc_min.value()
        _max = self.ui.slider_bc_max.value()
        
        if _min>_max or _max<_min:
            _min = _max
        
        brightness = (-_min + (255-_max))/2
        contrast = (_min + (255-_max))/2
        
        self.updateBrightnessContrast((brightness, contrast))
    
    def updateBrightnessContrast(self, minMax: tuple=None):
        if type(minMax) is tuple:
            brightness = minMax[0]
            contrast = minMax[1]
            self.ui.slider_brightness.valueChanged.disconnect(self.updateBrightnessContrast)
            self.ui.slider_contrast.valueChanged.disconnect(self.updateBrightnessContrast)
            self.ui.slider_brightness.setValue(brightness)
            self.ui.slider_contrast.setValue(contrast)
            self.ui.slider_brightness.valueChanged.connect(self.updateBrightnessContrast)
            self.ui.slider_contrast.valueChanged.connect(self.updateBrightnessContrast)
            self.ui.bc_min_label.setText(str(self.ui.slider_bc_min.value()))
            self.ui.bc_max_label.setText(str(self.ui.slider_bc_max.value()))
        else:
            brightness = self.ui.slider_brightness.value()
            contrast = self.ui.slider_contrast.value()
            _min = -brightness + contrast
            _max = -brightness - contrast + 255
            self.ui.slider_bc_min.valueChanged.disconnect(self.updateBrightnessContrastMinMax)
            self.ui.slider_bc_max.valueChanged.disconnect(self.updateBrightnessContrastMinMax)
            self.ui.slider_bc_min.setValue(_min)
            self.ui.slider_bc_max.setValue(_max)
            self.ui.slider_bc_min.valueChanged.connect(self.updateBrightnessContrastMinMax)
            self.ui.slider_bc_max.valueChanged.connect(self.updateBrightnessContrastMinMax)
            self.ui.bc_min_label.setText(str(_min))
            self.ui.bc_max_label.setText(str(_max))
        
        for chn, img in self.previewMain.channels.items():
            frame = dmk.processing._changeFrameBrightnessAndContrast(chn.data[self.previewMain.frameId], brightness, contrast)
            img.setImage(frame, autoLevels=False)
    
    def applyBrightnessContrast(self):
        brightness = self.ui.slider_brightness.value()
        contrast = self.ui.slider_contrast.value()
        for chn, img in self.previewMain.channels.items():
            dmk.processing.changeBrightnessAndContrast(chn, brightness, contrast)
        self.reset(True)
        self.resetBrightnessContrast()
    
    def resetBrightnessContrast(self):
        self.ui.slider_brightness.setValue(0)
        self.ui.slider_contrast.setValue(0)
        self.ui.slider_bc_min.setValue(0)
        self.ui.slider_bc_max.setValue(255)
    
        self.updateFrames()
    
    def updatePxInt(self):
        if len(self.currentView) == 0:
            return
        
        self.figure.delaxes(self.axes)
        self.axes = self.figure.add_subplot(111)        
        
        x = np.arange(256)
        y1 = dmk.processing.pixelIntensity(self.currentView[0], self.previewMain.frameId).data
        y2 = dmk.processing.pixelIntensity(self.currentView[0]).data        
        
        self.axes.plot(x, y1)
        self.axes.get_xaxis().set_visible(False)
        self.axes.get_yaxis().set_visible(False)
        
        self.brightnessPlot.draw()        
    
    @property
    def currentView(self):
        return self.views[self.currentViewName]
    
    def addAnnexTab(self, viewName):
        frame = QFrame()
        frame_layout = QVBoxLayout()
        slider = QSlider()
        preview = widgets.PreviewWidget(slider=slider, fileInfo=self.ui.fileInfo)        
        
        slider.setOrientation(Qt.Orientation.Horizontal)
        frame_layout.addWidget(preview)
        frame_layout.addWidget(slider)
        frame.setLayout(frame_layout)
        self.ui.visualize_annexesTabs.addTab(frame, viewName)
        self.viewTabs[viewName] = preview
    
    def viewsItemChanged(self, current, previous):
        self.selectView(current.text())
    
    def selectView(self, viewName):
        if viewName not in self.views.keys():
            return
        found = False
        for i in range(self.ui.visualize_viewsList.count()):
            if self.ui.visualize_viewsList.item(i).text() == viewName:
                self.ui.visualize_viewsList.setItemSelected(self.ui.visualize_viewsList.item(i), True)
                found = True
        if not found: 
            return
        
        self.currentViewName = viewName
        self.reset()
    
    def newView(self, channels=None):
        self.viewsCount += 1
        viewName = "View%d" % self.viewsCount
        if type(channels) is list:
            self.views[viewName] = channels
        else:
            self.views[viewName] = []
        self.ui.visualize_viewsList.addItem(viewName)
        self.addAnnexTab(viewName)
        self.selectView(viewName)

    def moveCross(self, event :QGraphicsSceneMouseEvent, pos: QPointF):
        if event.buttons() == Qt.RightButton:
            self.previewMain.hLine.setPos(pos.y())
            self.previewMain.vLine.setPos(pos.x())
            
            self.previewTop.updateFramePercentage(pos.y()/self.previewMain.shape[1])
            self.previewLeft.updateFramePercentage(pos.x()/self.previewMain.shape[2])
    
    def reset(self, preserveFrameId=False):
        self.previewMain.clear()
        self.previewTop.clear()
        self.previewLeft.clear()
        gc.collect()
        
        for chn in self.currentView:            
            self.previewMain.addChannels(chn)
        
        if self.resliceWorker != None and self.resliceWorker.isRunning():
            self.resliceWorker.terminate()
        self.resliceWorker = ReslicerWorker(self.currentView)
        self.resliceWorker.signals.finished.connect(self.resetOrthoView)
        self.resliceWorker.start()
        
        if type(preserveFrameId) is bool and preserveFrameId is True:
            self.updateFrames()
        else:
            self.updateFrames(0)
        self.previewMain.sliderUpdateRange()
        self.previewMain.view.autoRange()
        self.updateBtnChannels()
        self.resetTabLUT()
        
        self.viewTabs[self.currentViewName].reset(self.currentView)
        
        self.preview3D.clear()
        for channel in self.previewMain.channels:
            self.preview3D.addChannel(channel)
    
    def resetOrthoView(self, top, left):
        self.previewTop.clear()
        self.previewTop.addChannels(top)
        self.previewTop.updateFrame(0)
        self.previewTop.view.autoRange()
        self.previewLeft.clear()
        self.previewLeft.addChannels(left)
        self.previewLeft.updateFrame(0)
        self.previewLeft.view.autoRange()
        self.resliceWorker = None
    
    def addChannels(self, channels):
        if channels is None or (type(channels) is list and len(channels) == 0):
            return
        if type(channels) is dmk.Channel:
            channels = [channels]
        if type(channels) is list:
            for channel in channels:
                channel.id = len(self.currentView) + 1
                self.currentView.append(channel)
            self.ui.label_appState.setText("Loading complete.")
        
        self.reset()
    
    def updateBtnChannels(self):
        clearLayout(self.ui.visualize_layout_channelList)
        for chn in self.currentView:
            btn = ChannelBtn(f'Ch{chn.id}', chn.id)
            btn.channelToggled.connect(self.toggleChannel)
            btn.channelRemoveTriggered.connect(self.removeChannel)
            self.ui.visualize_layout_channelList.addWidget(btn)
    
    def toggleChannel(self, btn: QPushButton, id: int):
        for chn, img in self.allChannelImage():
            if chn.id == id:
                if btn.isChecked():
                    img.show()                
                else:
                    img.hide()
        self.updateFrames()
    
    def removeChannel(self, btn: QPushButton, id):
        for i in range(len(self.currentView)):
            if self.currentView[i].id == id:
                self.currentView.remove(self.currentView[i])
                break
        self.reset()
    
    def allChannels(self):
        return list(self.previewMain.channels.keys()) + list(self.previewLeft.channels.keys()) + list(self.previewTop.channels.keys())

    def allChannelImage(self):
        return list(self.previewMain.channels.items()) + list(self.previewLeft.channels.items()) + list(self.previewTop.channels.items())

    def updateFrames(self, frameId=None):
        self.previewMain.updateFrame(frameId)
        self.previewLeft.updateFrame(frameId)
        self.previewTop.updateFrame(frameId)
    
    def previews(self):
        return [self.previewMain, self.previewTop, self.previewLeft]
    
    def loadChannels(self, filename: str):
        self.currentView.clear()        
        self.ui.label_appState.setText("Loading file")
        fw = widgets.FileLoaderWorker(filename)
        fw.signals.loaded.connect(self.addChannels)
        self.previewMain.threadpool.start(fw)
    
    def addFile(self, event):
        filename = QFileDialog.getOpenFileName(None, 'Open file', 
         self.ui.fileSystemModel.rootPath(),"Any (*.*)")[0]
        self.ui.label_appState.setText("Loading file")
        fw = widgets.FileLoaderWorker(filename)
        fw.signals.loaded.connect(self.addChannels)
        self.previewMain.threadpool.start(fw)
        
    def functionMenuClicked(self, name):
        self.functionParameters.clearForm()
        self.functionParameters.setHiddenAll(False)
        self.functionParameters.ui.checkbox_enabled.setHidden(True)
        self.functionParameters.ui.btn_batchMode.setHidden(True)
        self.functionParameters.outputDir.setHidden(True)
        
        func = self.functions.getFunction(name)
        if func == None:
            return
        self.functionParameters.function = func
        self.functionParameters.ui.edit_operation_name.setText(name)
        
        sign = inspect.signature(func)        
        for argName in sign.parameters:
            param = sign.parameters[argName]
            if param.annotation == inspect._empty:
                continue
            
            default_arg = None
            if param.default != inspect._empty:
                default_arg = param.default
            
            formWidget = None
                
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if default_arg != None:
                    spinBox.setValue(int(default_arg))
                else:
                    spinBox.setValue(0)
                formWidget = spinBox
            if param.annotation is float:
                spinBox = QDoubleSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if default_arg != None:
                    spinBox.setValue(float(default_arg))
                else:
                    spinBox.setValue(0.0)
                formWidget = spinBox
            elif param.annotation in [dmk.Channel, Mesh]:
                formWidget = self.newInputComboBox()
            elif param.annotation is dmk.Channels:
                formWidget = widgets.ChannelSelectorWidget(self.views.keys())
            elif param.annotation is widgets.BatchParameters:
                formWidget = widgets.BatchSelectionWidget(self.ui.fileSystemModel.rootPath())
            elif param.annotation is dmk.SingleChannel:
                formWidget = widgets.FilePickerWidget(self.ui.fileSystemModel.rootPath())
            elif param.annotation is dmk.StrFilePath:
                formWidget = widgets.FilePickerWidget(self.ui.fileSystemModel.rootPath())
            elif param.annotation is dmk.StrFolderPath:
                formWidget = widgets.FolderPickerWidget(self.ui.fileSystemModel.rootPath())
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setFixedHeight(18)
                if default_arg != None:
                    textEdit.setText(default_arg)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                formWidget = textEdit
            elif type(param.annotation) is type(enum.Enum):
                formWidget = widgets.EnumComboBox(param.annotation)
            elif param.annotation is bool:
                checkBox = QCheckBox("")
                if default_arg != None:
                    checkBox.setChecked(default_arg)
                formWidget = checkBox
            if formWidget != None:
                self.functionParameters.ui.layout_settingsForm.addRow(argName+":", formWidget)
    
    def newInputComboBox(self):
        comboBox = QComboBox()
        for i in range(self.ui.visualize_viewsList.count()):
            item = self.ui.visualize_viewsList.item(i)
            comboBox.addItem(item.text())
        comboBox.setCurrentText(self.currentViewName)
        return comboBox

    def applyFunction(self, duplicate:bool=False):
        func: function = self.functionParameters.function
        if func is None:
            return        
        
        targetView = ""
        channelCount = 0
        args = []
        for i in range(self.functionParameters.ui.layout_settingsForm.rowCount()):
            widget = self.functionParameters.ui.layout_settingsForm.itemAt(i, QFormLayout.ItemRole.FieldRole).widget()
            
            if type(widget) is QSpinBox:
                args.append(int(widget.value()))
            elif type(widget) is QDoubleSpinBox:
                args.append(float(widget.value()))
            elif type(widget) is widgets.EnumComboBox:
                sel = widget.currentText()
                for e in widget.enum:
                    if e.name == sel:
                        args.append(e)
                        break
            elif type(widget) is widgets.BatchSelectionWidget:
                args.append(widget.getBatch())     
            elif type(widget) is QComboBox:
                args.append(self.views[widget.currentText()])
                channelCount = len(self.views[widget.currentText()])
                if targetView == "":
                    targetView = widget.currentText()
            elif type(widget) in [QLineEdit, widgets.FilePickerWidget, widgets.FolderPickerWidget]:
                args.append(widget.text())
            elif type(widget) is QCheckBox:
                args.append(widget.isChecked())
            elif type(widget) is widgets.ChannelSelectorWidget:
                channels = []
                for val in widget.getValues():
                    channels += self.views[val]
                args.append(channels)
            else:
                args.append(None)
        
        self.recorder.addOperation(dmk.Operation(func, args, func.__name__))
        
        sign = inspect.signature(func)
        if sign.return_annotation is dmk.Channel:
            newChannels = []
            if channelCount == 0:
                channelCount = 1
            for i in range(channelCount):
                argTmp = []
                argId = 0
                for argName in sign.parameters:
                    param = sign.parameters[argName]
                    if param.annotation == dmk.Channel:
                        argTmp.append(args[argId][i])
                    else:
                        argTmp.append(args[argId])
                    argId += 1
                newChannels.append(func(*argTmp))
            if duplicate == False:
                if targetView != "":
                    self.views[targetView] = newChannels
                    self.currentViewName = targetView
                    self.reset()
            else:
                self.newView(newChannels)
        else:
            for i in range(channelCount):
                argTmp = []
                argId = 0
                for argName in sign.parameters:
                    param = sign.parameters[argName]
                    if param.annotation == dmk.Channel:
                        argTmp.append(args[argId][i])
                    else:
                        argTmp.append(args[argId])
                    argId += 1
                func(*argTmp)


class ReslicerSignals(QObject):
    finished = Signal(list, list)

class ReslicerWorker(QThread):
    def __init__(self, channels: dmk.Channel=[]):
        super(ReslicerWorker, self).__init__()        
        self.channels = channels
        self.signals = ReslicerSignals()

    @Slot()
    def run(self):
        top = []
        left = []
        for channel in self.channels:
            top.append(dmk.processing._resliceTop(channel))
            left.append(dmk.processing._resliceLeft(channel))
        self.signals.finished.emit(top, left)