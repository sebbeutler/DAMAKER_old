from typing import Callable
from PySide2.QtWidgets import QWidget, QPushButton
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal, QObject, QSize

class ActionButton(QPushButton):
    def __init__(self, onClick: Callable, name: str="action", icon: str=""):
        if icon != "":
            _icon = QIcon()
            _icon.addFile(icon, QSize(), QIcon.Normal, QIcon.Off)
            super().__init__(_icon, name)
        else:
            super().__init__(name)
        self.function = onClick
        self.clicked.connect(self.function)

class ITabWidget:
    name: str = "None"
    icon: str = u":/flat-icons/icons/flat-icons/questions.svg"
    toolbar: list[ActionButton] = []
    
    changeTitle = Signal(str)
    
    def closing(self):
        pass