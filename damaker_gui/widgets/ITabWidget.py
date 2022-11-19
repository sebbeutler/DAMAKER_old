"""
from PySide6.QtWidgets import QFrame, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

import damaker_gui.widgets as widgets

class TemplateITabWidget(QFrame, widgets.ITabWidget):
    name: str = "ROI"
    icon: str = u":/flat-icons/icons/flat-icons/radar_plot.svg"

    @property
    def toolbar(self) -> list[widgets.ActionButton]:
        return [widgets.ActionButton(self.addSet, "New set", u":/flat-icons/icons/flat-icons/plus.png"),]

    def __init__(self, parent=None):
        super().__init__(parent)
"""

from typing import Callable
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal, QObject, QSize

import damaker_gui

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

class ITabWidget():
    name: str = "Untitled"
    icon: str = u":/flat-icons/icons/flat-icons/questions.svg"
    toolbar: list[ActionButton] = []

    focus = Signal(object)
    changeTitle = Signal(str)

    def tabEnterFocus(self):
        pass

    def requestFocus(self):
        self.focus.emit(self)

    def closing(self):
        pass

class IView(ITabWidget):
    def updated(self):
        damaker_gui.MainWindow.Instance.viewChanged.emit(self)

    def isView(obj):
        return obj is not None and issubclass(type(obj), IView)
