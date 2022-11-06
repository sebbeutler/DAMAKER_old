from PySide2.QtWidgets import QListWidget, QListWidgetItem, QGroupBox, QHBoxLayout, QFrame
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

import damaker_gui.widgets as widgets
import pyqtgraph as pg

class ROIWidget(QListWidget, widgets.ITabWidget):
    name: str = "ROI"
    icon: str = u":/flat-icons/icons/flat-icons/radar_plot.svg"

    @property
    def toolbar(self) -> list[widgets.ActionButton]:
        return [widgets.ActionButton(self.addSet, "New set", u":/flat-icons/icons/flat-icons/plus.png"),]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.addSet()

    def addSet(self):
        item = QListWidgetItem("ROI set")
        self.addItem(item)
        self.setItemWidget(item, ROISet("ROI set"))

    def updateList(self):
        pass

class ROISet(QGroupBox):
    def __init__(self, name: str="ROI set"):
        super().__init__(name)


class ROIButtons(QFrame):
    def __init__(self, view=None):
        super().__init__(None)

        self.view: widgets.PreviewWidget = view

        self._layout = QHBoxLayout()
        self.setLayout(self._layout)

        self._layout.addWidget(widgets.ActionButton(self.addLine, "Line"))
        self._layout.addWidget(widgets.ActionButton(self.addPolyLine, "PolyLine"))
        self._layout.addWidget(widgets.ActionButton(self.addRect, "Rect"))
        self._layout.addWidget(widgets.ActionButton(self.addCircle, "Circle"))
        self._layout.addWidget(widgets.ActionButton(self.addEllipse, "Ellipse"))
        self._layout.addWidget(widgets.ActionButton(self.addCrosshair, "Crosshair"))

        self.roi_list: list[pg.ROI] = []

    def focusROI(self, roi):
        self.view.currentROI = roi

    def addRoi(self, roi: pg.ROI):
        roi.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        roi.sigClicked.connect(self.focusROI)
        self.view.addItem(roi)
        self.roi_list.append(roi)

    def addLine(self):
        roi = pg.LineSegmentROI([[10, 64], [120,64]], pen='r')
        self.addRoi(roi)

    def addPolyLine(self):
        roi = pg.PolyLineROI([[10, 64], [120,64], [200,64]])
        self.addRoi(roi)

    def addRect(self):
        roi = pg.RectROI([10, 64], [120,64])
        self.addRoi(roi)

    def addCircle(self):
        roi = pg.CircleROI([10, 64], radius=4)
        self.addRoi(roi)

    def addEllipse(self):
        roi = pg.EllipseROI([10, 64], [20, 20])
        self.addRoi(roi)

    def addCrosshair(self):
        roi = pg.CrosshairROI([10, 64])
        self.addRoi(roi)
