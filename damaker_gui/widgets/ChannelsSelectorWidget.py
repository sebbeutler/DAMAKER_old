from math import comb
from PySide2.QtWidgets import QFrame, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QComboBox, QSizePolicy

from damaker import Channels

import damaker_gui
import damaker_gui.widgets as widgets
from damaker_gui.widgets.ITabWidget import IView

class ChannelSelectorWidget(QFrame):
    def __init__(self, choices=[]):
        super().__init__()
        self.choices = choices
        self._layout = QVBoxLayout()
        self._layout.setSpacing(4)
        self._layout.setMargin(0)
        
        self.setLayout(self._layout)
        
        self.comboBoxs: list[ChannelComboBox] = [ChannelComboBox(self, self.choices)]        
        self._layout.addWidget(self.comboBoxs[0])
        
        self.btnAdd = QPushButton("+")
        self.btnAdd.clicked.connect(self.addChannelEntry)
        self._layout.addWidget(self.btnAdd)
        
        damaker_gui.Window().tabChanged.connect(self.updateChoices)
        self.updateChoices()
        damaker_gui.Window().viewChanged.connect(self.updateChoices)
        
    
    def addChannelEntry(self):
        self.comboBoxs.append(ChannelComboBox(self, self.choices))        
        self._layout.insertWidget(self._layout.count() -2, self.comboBoxs[-1])
    
    def getValues(self) -> list[str]:
        res = []
        for i in range(self._layout.count()):
            _item = self._layout.itemAt(i)
            if issubclass(type(_item.widget()), ChannelComboBox):
                res.append(_item.widget().currentText())
        return res

    def removeChannel(self, chn: QWidget):
        if self._layout.count() <= 2:
            return
        self._layout.removeWidget(chn)
        if chn != None:
            chn.setParent(None)
    
    def updateChoices(self):
        self.choices = [widget.name for widget in damaker_gui.Window().getTabsByType(IView)]
        
        for comboBox in self.comboBoxs:
            current = comboBox.currentText()
            comboBox.comboBox.clear()
            comboBox.comboBox.addItems(self.choices)

    def getChannels(self) -> Channels:
        channels = []
        previews: list[widgets.PreviewFrame] = damaker_gui.Window().getTabsByType(widgets.PreviewFrame)
        choices = self.getValues()
        
        for preview in previews:
            if preview.name in choices:
                channels += preview.view.data
        
        return channels
    
    
class ChannelComboBox(QFrame):
    def __init__(self, parent, choices=[]):
        super().__init__()
        self._parent = parent
        self._layout = QHBoxLayout()
        self._layout.setSpacing(4)
        self._layout.setMargin(0)
        self.setLayout(self._layout)
        
        self.comboBox = QComboBox()
        # self.comboBox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.comboBox.addItems(choices)
        self._layout.addWidget(self.comboBox)
        
        self.btnSuppr = QPushButton("-")
        self.btnSuppr.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btnSuppr.setMinimumWidth(10)
        self.btnSuppr.clicked.connect(lambda: self._parent.removeChannel(self))
        self._layout.addWidget(self.btnSuppr)
    
    def currentText(self):
        return self.comboBox.currentText()
        