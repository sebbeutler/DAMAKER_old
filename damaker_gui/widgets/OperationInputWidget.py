from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

class OperationInputWidget(QComboBox):
    def __init__(self, operations: list[str]):
        super().__init__()
        for op in operations:
            self.addItem(op)
        self.addItem("None")
        self.setCurrentText("None")                    
        self.setDuplicatesEnabled(False)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.setFixedHeight(22)