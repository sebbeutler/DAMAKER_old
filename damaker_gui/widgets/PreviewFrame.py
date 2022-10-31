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
            top.append(damaker.processing._resliceTop(channel))
            left.append(damaker.processing._resliceLeft(channel))
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

        self.frame_btn_channels = QFrame()
        self._layout.addWidget(self.frame_btn_channels)

        self.layout_btn_channels = QHBoxLayout()
        self.layout_btn_channels.setMargin(0)
        self.layout_btn_channels.setSpacing(3)
        self.frame_btn_channels.setLayout(self.layout_btn_channels)

        # Slider #
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)

        # View #
        self.view: widgets.PreviewWidget = widgets.PreviewWidget([], None, self.slider)
        self.view.channelsChanged.connect(self.changeTitle.emit)

        self._layout.addWidget(self.view)
        self._layout.addWidget(self.slider)

        # ROI #
        self.roi_buttons = widgets.ROIButtons(self.view)
        self._layout.addWidget(self.roi_buttons)

        # 3D THREAD #
        self.thread3DView = widgets.Loader3DViewThread()
        self.preview3D = None

        # ORTHO THREAD #
        self.threadOrtho = ReslicerWorker()        
        self.threadOrtho.finished.connect(self.setProjections)
        self.idProj = (0, 0)
        self.projX: list[Channel] = None
        self.projY: list[Channel] = None

        if path != "":
            self.view.loadFile(path)
        self.view.channelsChanged.connect(self.requestFocus)
        self.view.channelsChanged.connect(self.updated)

        if channels != []:
            self.view.addChannels(channels)

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
        widgets.clearLayout(self.layout_btn_channels, True)
        for chn in self.view.channels.keys():
            btn = ChannelBtn(f'Ch{chn.id}', chn.id)
            btn.channelToggled.connect(self.toggleChannel)
            btn.channelRemoveTriggered.connect(self.removeChannel)
            self.layout_btn_channels.addWidget(btn)
        self.layout_btn_channels.addStretch()        
        if damaker_gui.Window() != None and hasattr(damaker_gui.Window(), 'lutSelector'):
            damaker_gui.Window().lutSelector.updateForm(self)

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