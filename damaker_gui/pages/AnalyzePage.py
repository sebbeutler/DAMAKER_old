
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

import damaker_gui.widgets as widgets

from damaker_gui.widgets.Preview3DWidget import Preview3DWidget
from damaker_gui.windows.UI_MainWindow import Ui_MainWindow

from .Page import Page

class AnalyzePage(Page):
    def __init__(self, ui: Ui_MainWindow):
        super().__init__(ui)
        
        self.p3D = widgets.Preview3DWidget()
        self.ui.layout_page_analyse.addWidget(self.p3D)