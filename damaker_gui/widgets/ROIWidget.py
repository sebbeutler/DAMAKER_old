from PySide2.QtWidgets import QListWidget, QListWidgetItem, QGroupBox, QHBoxLayout, QFrame, QVBoxLayout
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, Signal, QSize

import damaker_gui.widgets as widgets
import pyqtgraph as pg

class ROISet(QGroupBox):
    def __init__(self, name: str="ROI set"):
        super().__init__(name)
        self.list = QListWidget()
        self.list.addItem("test")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.list)

    def addRoi(self, roi: pg.ROI):
        item = QListWidgetItem(roi.__str__())
        item.roi = roi
        self.list.addItem(item)

class ROIWidget(widgets.QFrameLayout, widgets.ITabWidget):
    name: str = "ROI"
    icon: str = u":/flat-icons/icons/flat-icons/radar_plot.svg"

    @property
    def toolbar(self) -> list[widgets.ActionButton]:
        return [
            widgets.ActionButton(self.addSet, "New set", u":/flat-icons/icons/flat-icons/plus.png"),
            widgets.ActionButton(self.removeRoi, "Delete ROI"),
            widgets.ActionButton(self.toggleROI, "Show/Hide"),
        ]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.list = QListWidget()
        self.layout.addWidget(self.list)

        self.roi_btns = ROIButtons()
        self.roi_btns.clicked.connect(self.addRoi)
        self.layout.addWidget(self.roi_btns)

        self.addSet()

    def addSet(self):
        item = QListWidgetItem("ROI set")
        item.setSizeHint(QSize(0, 100))
        self.list.addItem(item)
        self.list.setItemWidget(item, ROISet("ROI set"))

    def currentSet(self) -> ROISet:
        return self.list.itemWidget(self.list.currentItem())

    def addRoi(self, roi: pg.ROI):
        roi_set = self.currentSet()
        if roi_set != None:
            roi_set.addRoi(roi)

    def removeRoi(self):
        roi_set: ROISet = self.currentSet()
        if roi_set != None:
            roi_set.list.takeItem(roi_set.list.currentRow())

    def toggleROI(self):
        raise "Note implemented"

class ROIButtons(widgets.QFrameLayout):
    clicked = Signal(pg.ROI)

    def __init__(self):
        super().__init__(_type=widgets.LayoutTypes.Horizontal)

        self.layout.addWidget(widgets.ActionButton(self.addLine, "Line"))
        self.layout.addWidget(widgets.ActionButton(self.addPolyLine, "PolyLine"))
        self.layout.addWidget(widgets.ActionButton(self.addRect, "Rect"))
        self.layout.addWidget(widgets.ActionButton(self.addCircle, "Circle"))
        self.layout.addWidget(widgets.ActionButton(self.addEllipse, "Ellipse"))
        self.layout.addWidget(widgets.ActionButton(self.addCrosshair, "Crosshair"))

    def addRoi(self, roi: pg.ROI):
        roi.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        self.clicked.emit(roi)

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
