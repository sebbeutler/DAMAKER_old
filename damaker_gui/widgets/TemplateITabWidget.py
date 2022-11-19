from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QSizePolicy
from PySide6.QtCore import Qt, Signal

import damaker as dmk
import damaker_gui as dmk_gui
import damaker_gui.widgets as widgets

from damaker_gui.widgets.QFrameLayout import *

class ColorAdjustWidget(QFrameLayout, widgets.ITabWidget):
    name: str = "Template widget"
    icon: str = u":/flat-icons/icons/flat-icons/timeline.svg"
    
    @property
    def toolbar(self) -> list[widgets.ActionButton]:        
        return [widgets.ActionButton(self.clearGraph, "Clear", u":/flat-icons/icons/flat-icons/cube.png")]
    
    def __init__(self, parent=None):
        super().__init__(parent, LayoutTypes.Vertical, spacing=5, margin=0)