
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from damaker_gui.widgets.Preview3DWidget import Preview3DWidget
from damaker_gui.windows.UI_MainWindow import Ui_MainWindow

class AnalyzePage:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        
        
        
        # self.ui.layout_page_analyse.addWidget(self.preview3D)