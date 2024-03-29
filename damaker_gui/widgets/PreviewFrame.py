from PySide2.QtWidgets import QPushButton, QFrame, QVBoxLayout, QHBoxLayout, QHBoxLayout, QAction, QSlider, QFileDialog, QGraphicsSceneDragDropEvent
from PySide2.QtCore import Signal, Qt, QThread, Slot

from aicsimageio.writers import OmeTiffWriter
import numpy as np

import damaker
from damaker.Channel import Channel

import damaker_gui
import damaker_gui.widgets as widgets

class ChannelBtn(QPushButton):
    channelToggled = Signal(QPushButton, int)
    channelRemoveTriggered = Signal(QPushButton, int)

    def __init__(self, name: str, chId: int):
        super().__init__(name)
        self.id = chId
        self.setCheckable(True)
        self.setChecked(True)
        self.setFixedWidth(30)
        self.toggled.connect(lambda: self.channelToggled.emit(self, self.id))
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        act = QAction("Remove", self)
        act.triggered.connect(lambda: self.channelRemoveTriggered.emit(self, self.id))
        self.addAction(act)

class ReslicerWorker(QThread):
    finished = Signal(list, list)
    loaded: bool = False
    def __init__(self, channels: Channel=[]):
        super().__init__()
        self.channels = channels

    @Slot()
    def run(self):
        top = []
        left = []
        for channel in self.channels:
            top.append(damaker.processing._channelResliceTop(channel))
            left.append(damaker.processing._channelResliceLeft(channel))
        self.finished.emit(top, left)

class PreviewFrame(QFrame, widgets.IView):
    name: str = "Z-stack"
    # icon: str = u":/20x20/icons/20x20/cil-screen-desktop.png"
    icon: str = u":/flat-icons/icons/flat-icons/database.svg"

    @property
    def toolbar(self) -> list[widgets.ActionButton]:
        return [widgets.ActionButton(self.add3DView, "3D", u":/flat-icons/icons/flat-icons/cube.png"),
                widgets.ActionButton(self.saveChannels, "Export", u":/flat-icons/icons/flat-icons/add_image.svg"),
                widgets.ActionButton(self.loadOrthogonalViews, "Orthogonal Views", u":/flat-icons/icons/flat-icons/grid.svg")]

    def __init__(self, parent=None, path="", channels=[]):
        super().__init__(parent)

        self.setAcceptDrops(True)

        # Layout #
        self._layout = QVBoxLayout(self)
        self._layout.setSpacing(3)
        self._layout.setMargin(0)

        # Slider #
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)

        # View info #
        self.info = widgets.FileInfoWidget()

        # View #
        self.view: widgets.StackView = widgets.StackView([], self.info, self.slider)
        self.view.channelsChanged.connect(self.changeTitle.emit)

        self._layout.addWidget(self.view)

        # Channels buttons #
        self.frame_btn_channels = widgets.QFrameLayout(_type=widgets.LayoutTypes.Horizontal, spacing=0, margin=0)

        # Buttons frame #
        self.action_frame = widgets.QFrameLayout(_type=widgets.LayoutTypes.Vertical, spacing=0, margin=0)
        self.action_frame.layout.addWidget(self.slider)
        self.action_frame.layout.addWidget(self.frame_btn_channels)

        # Bottom frame #
        self.bottom_frame = widgets.QFrameLayout(_type=widgets.LayoutTypes.Horizontal, spacing=0, margin=0)
        self.bottom_frame.layout.addWidget(self.action_frame)
        self.bottom_frame.layout.addWidget(self.info)
        self._layout.addWidget(self.bottom_frame)

        # 3D loader thread #
        self.thread3DView = widgets.Loader3DViewThread()
        self.preview3D = None

        # Orthogonal loader thread #
        self.threadOrtho = ReslicerWorker()
        self.threadOrtho.finished.connect(self.setProjections)
        self.idProj = (0, 0)
        self.projX: list[Channel] = None
        self.projY: list[Channel] = None

        # ROI set #
        self.roi_set_list: list[widgets.ROISet] = []

        # File preload from argument #
        if path != "":
            self.view.loadFile(path)
        self.view.channelsChanged.connect(self.requestFocus)
        self.view.channelsChanged.connect(self.updated)

        if channels != []:
            self.view.addChannels(channels)

        # Signals #
        self.view.channelsChanged.connect(self.updateBtnChannels)
        self.updateBtnChannels()

    def saveChannels(self):
        path = QFileDialog.getSaveFileName(None, 'Export', widgets.WorkspaceWidget.RootPath)[0]
        if path == "":
            return
        channels = list(self.view.channels.keys())
        if len(channels) == 0: return
        OmeTiffWriter.save(np.array([chn.data for chn in channels]), path, physical_pixel_sizes=channels[0].px_sizes, dim_order="CZYX")

    def loadOrthogonalViews(self):
        self.threadOrtho.channels = list(self.view.channels.keys())
        self.threadOrtho.start()
        self.view.enableCross(True)
        print("Reslicing stack ...")

    def setProjections(self, top, left):
        self.projX = left
        self.projY = top
        print("Reslicing thread done ☑")

    def add3DView(self):
        self.thread3DView.setChannels(list(self.view.channels.keys()))
        self.thread3DView.setWidget(widgets.Preview3DWidget(name=self.name))
        self.thread3DView.loaded.connect(self.parentWidget().parentWidget().parentWidget().addTab)
        self.thread3DView.start()

    def updateBtnChannels(self):
        widgets.clearLayout(self.frame_btn_channels.layout, True)
        for chn in self.view.channels.keys():
            btn = ChannelBtn(f'Ch{chn.id}', chn.id)
            btn.channelToggled.connect(self.toggleChannel)
            btn.channelRemoveTriggered.connect(self.removeChannel)
            self.frame_btn_channels.layout.addWidget(btn)
        self.frame_btn_channels.layout.addStretch()        
        if damaker_gui.MainWindow.Instance != None and hasattr(damaker_gui.MainWindow.Instance, 'lutSelector'):
            damaker_gui.MainWindow.Instance.lutSelector.updateForm(self)

    def removeChannel(self, btn: QPushButton, id):
        toDelete = None
        for chn, img in self.view.channels.items():
            if chn.id == id:
                self.view.removeItem(img)
                toDelete = chn
        if toDelete != None:
            del self.view.channels[toDelete]
            print(f"Removed channel n°{id} ✔")
        self.view.updateFrame()
        self.layout_btn_channels.removeWidget(btn)
        btn.deleteLater()

    def toggleChannel(self, btn: QPushButton, id: int):
        for chn, img in self.view.channels.items():
            if chn.id == id:
                if btn.isChecked():
                    img.show()
                else:
                    img.hide()
        self.view.updateFrame()

    def dropEvent(self, event: QGraphicsSceneDragDropEvent):
        super().dropEvent(event)

        if event.mimeData().hasUrls:
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.view.loadFiles(links)
        else:
            event.ignore()

    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        super().dragMoveEvent(event)
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def isInstance(obj):
        return obj is not None and issubclass(type(obj), PreviewFrame)

    def connectRoiSet(self, roi_set: widgets.ROISet):
        if roi_set not in self.roi_set_list:
            self.roi_set_list.append(roi_set)

    def showRoiSet(self, roi_set: widgets.ROISet):
        self.connectRoiSet(roi_set)
        if roi_set.visible:
            return
        for i in range(roi_set.list.count()):
            roi = roi_set.list.item(i).roi
            self.view.addItem(roi)
        roi_set.visible = True

    def hideRoiSet(self, roi_set: widgets.ROISet):
        self.connectRoiSet(roi_set)
        if not roi_set.visible:
            return
        for i in range(roi_set.list.count()):
            roi = roi_set.list.item(i).roi
            self.view.removeItem(roi)
        roi_set.visible = False

    def toggleRoiSet(self, roi_set: widgets.ROISet):
        if roi_set.visible:
            self.hideRoiSet(roi_set)
        else:
            self.showRoiSet(roi_set)


class Loader3DViewThread(QThread):
    loaded = Signal(widgets.Preview3DWidget)
    def __init__(self, channels=[], widget: widgets.Preview3DWidget=None):
        super().__init__()
        self.channels = channels
        self.widget = widget

    def setChannels(self, channels):
        self.channels = channels

    def setWidget(self, widget):
        self.widget = widget

    @Slot()
    def run(self):
        if self.channels == [] or self.widget is None:
            return
        self.setPriority(QThread.HighPriority)
        print("Converting to 3D 🔅")   
        self.widget.setChannels(self.channels)
        self.loaded.emit(self.widget)
        print("Finished 3D conversion ✅")