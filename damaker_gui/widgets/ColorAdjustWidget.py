from smtpd import PureProxy
from PySide2.QtWidgets import QFrame, QVBoxLayout, QSlider, QLabel, QSizePolicy, QPushButton
from PySide2.QtCore import Signal, Qt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from damaker.Channel import Channels
from damaker_gui.widgets.QFrameLayout import LayoutTypes, QFrameLayout

from damaker_gui.windows.UI_MainWindow import Ui_MainWindow

import damaker as dmk
import damaker_gui.widgets as widgets

class ColorSlider(QFrameLayout):
    def __init__(self, name: str="", _range: tuple[int]=(0, 1000)):
        super().__init__(None, LayoutTypes.Vertical, 0, 0)
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(_range[0], _range[1])
        self.slider.setValue(0)
        self.layout.addWidget(self.slider)
        
        self.label = QLabel(name)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    
    def setLabel(self, name: str=""):
        self.label.setText(name)
    
    def value(self):
        return self.slider.value()
    
    def setValue(self, value):
        self.slider.setValue(value)
        
    @property
    def valueChanged(self):
        return self.slider.valueChanged

class ColorAdjustWidget(QFrameLayout, widgets.ITabWidget):
    name: str = "Brigntess/Contrast"
    icon: str = u":/flat-icons/icons/flat-icons/timeline.svg"
    
    NeedUpdateSignal = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent, LayoutTypes.Vertical, 20, 0)
        self.channels = []
        
        self.figure = Figure(figsize=(0.5, 0.5))
        self.brightnessPlot = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.axes.plot([1, 2,3], [1, 2 ,3])
        
        # self.layout.addWidget(self.brightnessPlot)
        
        self.slider_max = ColorSlider("Maximum")
        self.layout.addWidget(self.slider_max)
        self.slider_min = ColorSlider("Minimum")
        self.layout.addWidget(self.slider_min)
        self.slider_brightness = ColorSlider("Brightness")
        self.layout.addWidget(self.slider_brightness)
        self.slider_contrast = ColorSlider("Contrast")
        self.layout.addWidget(self.slider_contrast)
        
        self.slider_brightness.slider.valueChanged.connect(self.updateBrightnessContrast)
        self.slider_contrast.slider.valueChanged.connect(self.updateBrightnessContrast)
        self.slider_min.slider.valueChanged.connect(self.updateBrightnessContrastMinMax)
        self.slider_max.slider.valueChanged.connect(self.updateBrightnessContrastMinMax)
        
        self.btns = QFrameLayout(None, LayoutTypes.Horizontal)
        
        self.btn_apply = QPushButton("Apply")
        self.btn_apply.clicked.connect(self.applyBrightnessContrast)
        self.btns.layout.addWidget(self.btn_apply)
        self.btn_reset = QPushButton("Reset")        
        self.btn_reset.clicked.connect(self.resetBrightnessContrast)
        self.btns.layout.addWidget(self.btn_reset)
        
        self.layout.addWidget(self.btns)
        
        
    def updateBrightnessContrastMinMax(self):
        print("MIN")
        _min = self.slider_min.value()
        _max = self.slider_max.value()
        
        if _min>_max or _max<_min:
            _min = _max
        
        brightness = (-_min + (255-_max))/2
        contrast = (_min + (255-_max))/2
        
        self.updateBrightnessContrast((brightness, contrast))
    
    def updateBrightnessContrast(self, minMax: tuple=None):
        if type(minMax) is tuple:
            brightness = minMax[0]
            contrast = minMax[1]
            self.slider_brightness.valueChanged.disconnect(self.updateBrightnessContrast)
            self.slider_contrast.valueChanged.disconnect(self.updateBrightnessContrast)
            self.slider_brightness.valueChanged.connect(self.updateBrightnessContrast)
            self.slider_contrast.valueChanged.connect(self.updateBrightnessContrast)
        else:
            brightness = self.slider_brightness.value()
            contrast = self.slider_contrast.value()
            _min = -brightness + contrast
            _max = -brightness - contrast + 255
            self.slider_min.valueChanged.disconnect(self.updateBrightnessContrastMinMax)
            self.slider_max.valueChanged.disconnect(self.updateBrightnessContrastMinMax)
            self.slider_min.valueChanged.connect(self.updateBrightnessContrastMinMax)
            self.slider_max.valueChanged.connect(self.updateBrightnessContrastMinMax)
        
        for chn, img in self.channels:
            frame = dmk.processing._changeFrameBrightnessAndContrast(chn.data[self.previewMain.frameId], brightness, contrast)
            img.setImage(frame, autoLevels=False)
    
    def applyBrightnessContrast(self):
        brightness = self.slider_brightness.value()
        contrast = self.slider_contrast.value()
        for chn, img in self.previewMain.channels.items():
            dmk.processing.changeBrightnessAndContrast(chn, brightness, contrast)
        self.reset(True)
        self.resetBrightnessContrast()
    
    def resetBrightnessContrast(self):
        self.slider_brightness.setValue(0)
        self.slider_contrast.setValue(0)
        self.slider_min.setValue(0)
        self.slider_max.setValue(255)
    
        self.NeedUpdateSignal.emit()