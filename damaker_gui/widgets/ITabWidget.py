from typing import Callable
from PySide2.QtWidgets import QWidget, QPushButton
from PySide2.QtCore import Signal, QObject

class ActionButton(QPushButton):
    def __init__(self, onClick: Callable, *args):
        super().__init__(*args)
        self.function = onClick
        self.clicked.connect(self.function)

class ITabWidget:
    name: str = "None"
    icon: str = u":/flat-icons/icons/flat-icons/questions.svg"
    toolbar: list[ActionButton] = []
    
    changeTitle = Signal(str)
    
    def closing(self):
        pass