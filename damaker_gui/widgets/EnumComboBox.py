from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

import enum

class EnumComboBox(QComboBox):
    def __init__(self, enum_: enum.EnumMeta):
        super().__init__()
        self.enum = enum_
        for e in self.enum:
            self.addItem(e.name)
        self.setFixedHeight(25)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)