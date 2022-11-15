from PySide2.QtWidgets import QFormLayout, QFrame, QSpinBox
from PySide2.QtCore import *

import damaker_gui.widgets as widgets

class InputROIWidget(widgets.IParameterWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def getValue(self):
        pass

class RectROIInput(QFrame, widgets.IParameterWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QFormLayout()
        self.setLayout(self._layout)

        self.x1 = QSpinBox()
        self._layout.addRow("x1: ", self.x1)

        self.y1 = QSpinBox()
        self._layout.addRow("y1: ", self.y1)

        self.x2 = QSpinBox()
        self._layout.addRow("x2: ", self.x2)

        self.y2 = QSpinBox()
        self._layout.addRow("y2: ", self.y2)

        self.refresh_btn = widgets.ActionButton(self.refreshRoi, "Refresh", u":/flat-icons/icons/flat-icons/synchronize.svg")
        self._layout.addWidget(self.refresh_btn)

    def refreshRoi(self):
        pass

    def getValue(self):
        pass