from PySide2.QtWidgets import QFrame
from PySide2.QtCore import Signal

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from damaker.Channel import Channels

from damaker_gui.windows.UI_MainWindow import Ui_MainWindow

import damaker as dmk

class ColorAdjustWidget(QFrame):
    NeedUpdateSignal = Signal()
    
    def __init__(self, ui: Ui_MainWindow, channels: Channels):
        super().__init__()
        self.ui = ui
        self.channels = channels
        
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
        
        for chn, img in self.channels:
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
    
        self.NeedUpdateSignal.emit()