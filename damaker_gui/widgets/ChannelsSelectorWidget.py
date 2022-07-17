from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

class ChannelSelectorWidget(QFrame):
    def __init__(self, choices=[]):
        super().__init__()
        self.choices = choices
        self._layout = QVBoxLayout()
        self._layout.setSpacing(4)
        self._layout.setMargin(0)
        
        
        self.setLayout(self._layout)
        
        self.comboBoxs = [ChannelComboBox(self, self.choices)]        
        self._layout.addWidget(self.comboBoxs[0])
        
        self.btnAdd = QPushButton("+")
        self.btnAdd.clicked.connect(self.addChannelEntry)
        self._layout.addWidget(self.btnAdd)
    
    def addChannelEntry(self):
        self.comboBoxs += [ChannelComboBox(self, self.choices)]        
        self._layout.insertWidget(self._layout.count() -2, self.comboBoxs[-1])
    
    def getValues(self):
        res = []
        for i in range(self._layout.count()):
            _item = self._layout.itemAt(i)
            if type(_item.widget()) is ChannelComboBox:
                res.append(_item.widget().currentText())
        return res

    def removeChannel(self, chn: QWidget):
        if self._layout.count() <= 2:
            return
        self._layout.removeWidget(chn)
        if chn != None:
            chn.setParent(None)
        print("removed")
        
        
class ChannelComboBox(QFrame):
    def __init__(self, parent, choices=[]):
        super().__init__()
        self._parent = parent
        self._layout = QHBoxLayout()
        self._layout.setSpacing(4)
        self._layout.setMargin(0)
        self.setLayout(self._layout)
        
        self.comboBox = QComboBox()
        self.comboBox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        for item in choices:
            self.comboBox.addItem(item)
        self._layout.addWidget(self.comboBox)
        
        self.btnSuppr = QPushButton("-")
        self.btnSuppr.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btnSuppr.setMinimumWidth(10)
        self.btnSuppr.clicked.connect(lambda: self._parent.removeChannel(self))
        self._layout.addWidget(self.btnSuppr)
    
    def currentText(self):
        return self.comboBox.currentText()
        