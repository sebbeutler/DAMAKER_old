from PySide2.QtWidgets import QTabWidget
from PySide2.QtCore import *

import damaker_gui.widgets as widgets

class InputWidget(QTabWidget, widgets.IParameterWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.batchMode = widgets.BatchSelectionWidget() 
        self.fileMode = widgets.FilePickerWidget()
        self.viewMode = widgets.ChannelSelectorWidget()

        self.addTab(self.batchMode, 'Batch Mode')
        self.addTab(self.fileMode, 'File Mode')
        self.addTab(self.viewMode, 'View Mode')

    def getValue(self):
        return self.currentWidget().getValue()