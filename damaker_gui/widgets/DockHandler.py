from PySide6.QtWidgets import QFrame, QGridLayout, QSplitter
from PySide6.QtCore import Qt

import damaker_gui.widgets as widgets
from damaker_gui.widgets.ContentDock import ContentDock

class DockHandler(QSplitter):
    def __init__(self, parent=None, orientation: Qt.Orientation= Qt.Orientation.Horizontal):
        super().__init__(parent)
        self.row = 1
        self.col = 0
        self.setOrientation(orientation)
        
        self.addWidget()
    
    def addRow(self):
        pass
    
    def addCol(self):
        for i in range(self.row):
            self.widget()
        