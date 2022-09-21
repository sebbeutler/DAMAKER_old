from smtpd import PureProxy
from typing import Callable
from PySide2.QtWidgets import QFrame, QVBoxLayout, QSlider, QLabel, QSizePolicy, QPushButton
from PySide2.QtCore import Signal, Qt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from damaker.Channel import Channels
from damaker_gui.widgets.ITabWidget import ActionButton, IView
from damaker_gui.widgets.QFrameLayout import LayoutTypes, QFrameLayout

import damaker as dmk
import damaker_gui as dmk_gui
import damaker_gui.widgets as widgets

class ColorSlider(QFrameLayout):
    def __init__(self, name: str="", _range: tuple[int]=(0, 1000), onRelease: Callable=None):
        super().__init__(None, LayoutTypes.Vertical, 0, 0)
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(_range[0], _range[1])
        self.slider.setValue(0)
        self.layout.addWidget(self.slider)
        
        self.label = QLabel(name)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        
        if onRelease != None:
            self.slider.sliderReleased.connect(onRelease)
    
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
    
    # @property
    # def toolbar(self) -> list[ActionButton]:        
    #     return [ActionButton(self.clearGraph, "Clear", u":/flat-icons/icons/flat-icons/cube.png")]
    
    def __init__(self, parent=None):
        super().__init__(parent, LayoutTypes.Vertical, 20, 0)
        self.target: widgets.PreviewFrame = None
        self.plotData: list = []
        
        self.figure = Figure(figsize=(0.5, 0.5))
        self.brightnessPlot = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.axes.axis('off')
        self.axes.stackplot([1, 2,3], [1, 2 ,3])
        
        self.layout.addWidget(self.brightnessPlot)
        
        self.slider_max = ColorSlider("Maximum", (0, 255), onRelease=self.plotGraph)
        self.slider_max.slider.setValue(255)
        self.layout.addWidget(self.slider_max)
        self.slider_min = ColorSlider("Minimum", (0, 255), onRelease=self.plotGraph)
        self.layout.addWidget(self.slider_min)
        self.slider_brightness = ColorSlider("Brightness", (-255, 255), onRelease=self.plotGraph)
        self.layout.addWidget(self.slider_brightness)
        self.slider_contrast = ColorSlider("Contrast", (-255, 255), onRelease=self.plotGraph)
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
        
        dmk_gui.Window().tabSelected.connect(self.updateGraph)
    
    def updateGraph(self, target: widgets.PreviewFrame=None):
        if not IView.isView(target): return
        if not issubclass(type(target), widgets.PreviewFrame): return
        
        if self.target != None:
            self.target.slider.sliderReleased.disconnect(self.plotGraph)
        self.target = target
        self.target.slider.sliderReleased.connect(self.plotGraph)           
    
    def clearGraph(self):
        self.axes.cla()
        self.axes.axis('off')
        self.brightnessPlot.draw()
    
    def plotGraph(self):
        self.updatePixelIntensity()
        self.clearGraph()
        self.axes.stackplot(list(range(len(self.plotData))), self.plotData)
        self.axes.axvline(x = 0, color = 'b', label = '0')
        self.axes.axvline(x = 255, color = 'b', label = '255')
        self.brightnessPlot.draw()
    
    def updatePixelIntensity(self):
        if self.target is None or len(self.target.view.channels) == 0: return
        
        img = list(self.target.view.channels.values())[0].image
        self.plotData = dmk.processing._framePixelIntensity(img).data
        
    def updateBrightnessContrastMinMax(self):
        _min = self.slider_min.value()
        _max = self.slider_max.value()
        
        if _min>_max or _max<_min:
            _min = _max
        
        brightness = (-_min + (255-_max))/2
        contrast = (_min + (255-_max))/2
        
        self.updateBrightnessContrast((brightness, contrast))
    
    def updateBrightnessContrast(self, minMax: tuple=None):
        if type(minMax) is tuple:
            brightness, contrast = minMax
            
            self.slider_brightness.valueChanged.disconnect(self.updateBrightnessContrast)
            self.slider_contrast.valueChanged.disconnect(self.updateBrightnessContrast)
            self.slider_brightness.setValue(brightness)
            self.slider_contrast.setValue(contrast)
            self.slider_brightness.valueChanged.connect(self.updateBrightnessContrast)
            self.slider_contrast.valueChanged.connect(self.updateBrightnessContrast)
        else:
            brightness = self.slider_brightness.value()
            contrast = self.slider_contrast.value()
            _min = -brightness + contrast
            _max = -brightness - contrast + 255
            
            self.slider_min.valueChanged.disconnect(self.updateBrightnessContrastMinMax)
            self.slider_max.valueChanged.disconnect(self.updateBrightnessContrastMinMax)
            self.slider_min.setValue(_min)
            self.slider_max.setValue(_max)
            self.slider_min.valueChanged.connect(self.updateBrightnessContrastMinMax)
            self.slider_max.valueChanged.connect(self.updateBrightnessContrastMinMax)
        
        if self.target != None and len(self.target.view.channels) != 0:
            for chn, img in self.target.view.channels.items():
                frame = dmk.processing._changeFrameBrightnessAndContrast(chn.data[self.target.view.frameId], brightness, contrast)
                img.setImage(frame, autoLevels=False)
        
        self.updatePixelIntensity()
        
    
    def applyBrightnessContrast(self):
        brightness = self.slider_brightness.value()
        contrast = self.slider_contrast.value()
        if self.target != None and len(self.target.view.channels) != 0:
            for chn, img in self.target.view.channels.items():
                dmk.processing.changeBrightnessAndContrast(chn, brightness, contrast)
        self.resetBrightnessContrast()
    
    def resetBrightnessContrast(self):
        self.slider_brightness.setValue(0)
        self.slider_contrast.setValue(0)
        self.slider_min.setValue(0)
        self.slider_max.setValue(255)