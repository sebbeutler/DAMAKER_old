from PySide2.QtWidgets import QFormLayout, QFrame, QComboBox
import damaker_gui.widgets as widgets
from damaker_gui.widgets.PreviewWidget import _luts
from . import clearLayout
import damaker_gui

class LUTComboBox(QComboBox):
    def __init__(self, channel, _callback):
        super().__init__()
        self.channel = channel
        self._callback = _callback
    
    def updateChannelLUT(self, text):
        for lut in _luts:
            if lut.name == text:
                self._callback(self.channel, lut)

class LutSelectorWidget(QFrame, widgets.ITabWidget):
    name: str = "Color map"
    icon: str = u":/flat-icons/icons/flat-icons/landscape.svg"
    
    def __init__(self, parent=None, target: widgets.PreviewFrame=None):
        super().__init__(parent)
        self._layout = QFormLayout()
        self.setLayout(self._layout)
        self.target = target
    
    def updateForm(self, target: widgets.PreviewFrame=None):
        if target is None: return
        self.target = target 
        clearLayout(self._layout)
        for chn in self.target.view.channels.keys():
            comboBox = LUTComboBox(chn, self.setChannelLUT)
            for lut in _luts:
                comboBox.addItem(lut.name)
            comboBox.setCurrentText(chn.lut.name)
            comboBox.currentTextChanged.connect(comboBox.updateChannelLUT)
            self._layout.addRow("Channel %d :" % chn.id, comboBox)
        if damaker_gui.Window() != None and damaker_gui.Window().ui.dock2.getWidgetIndex(target) == -1:
            damaker_gui.Window().addTab(2, self)
    
    def setChannelLUT(self, channel, colorMap):
        channel.lut = colorMap
        if channel in self.target.view.channels.keys():
            self.target.view.channels[channel].setColorMap(channel.lut)
        
        for chn in self.target.projX + self.target.projY:
            if chn.id == channel.id:
                chn.lut = channel.lut
        
        self.target.view.updateFrame()
        if damaker_gui.Window() != None:
            damaker_gui.Window().orthogonalProjection.setColorMap(self.target, channel.id, channel.lut)
            damaker_gui.Window().orthogonalProjection.updateFrames()
        