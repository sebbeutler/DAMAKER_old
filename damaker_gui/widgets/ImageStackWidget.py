from PySide2.QtWidgets import QFrame, QSlider, QGraphicsSceneMouseEvent, QSizePolicy, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QAction, QSlider, QFileDialog, QGraphicsSceneDragDropEvent
from PySide2.QtGui import QMouseEvent, QPainter, Qt
from PySide2.QtCore import Signal, QPointF, QThreadPool, QPoint, QObject, QRunnable, Slot

import pyqtgraph as pg

import damaker
from damaker.imagestack import ImageStack
import damaker_gui.widgets as widgets


class SliderListWidget(widgets.QFrameLayout):
    def addSlider(self, slider_range: tuple[int, int]):
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(slider_range[0], slider_range[1])
        self.layout.addWidget(slider)

    def reset(self):
        raise NotImplemented()

class ImageWidget(pg.ImageView):
    def __init__(self, imagestack: ImageStack=None, sliders: SliderListWidget= None):
        super().__init__()

        self.view.state['wheelScaleFactor'] = -1.0 / 50.0
        self.view.sigRangeChangedManually.connect(lambda: self.updateTextInfo())

        self.ui.histogram.hide()
        self.ui.roiBtn.hide()
        self.ui.menuBtn.hide()
        self.ui.roiPlot.setVisible(False)
        self.ui.roiPlot.hide()
        self.view.setBackgroundColor((32, 32, 32))

        self.pgimages: list[pg.ImageItem] = []
        self.imagestack: ImageStack = None
        self.sliders = sliders

        if imagestack != None:
            self.setStack(imagestack)


    def setStack(self, imagestack: ImageStack):
        self.imagestack = imagestack
        print(imagestack)
        for dim in imagestack.shape:
            self.sliders.addSlider((0, dim))
        # self.setImage((..., 0))

        # self.view.autoRange()
        # self.channelAdded.emit()


    def setImage(self, id: tuple[int, ...]):
        img = pg.ImageItem()
        img.axisOrder = 'row-major'

        # TODO: convert ndarray to pg.ColorMap ?
        if self.imagestack.metadata.lut != None:
            img.setColorMap(self.imagestack.metadata.lut)
            img.setCompositionMode(QPainter.CompositionMode.CompositionMode_Plus)

        img.setImage(self.imagestack.data[id], autoLevels=False)

    def addImage(self, img: pg.ImageItem):
        self.pgimages.append(img)
        self.addImage(img)


class ImageStackWidget(widgets.QFrameLayout, widgets.IView):
    name: str = "ImageStack"
    icon: str = u":/flat-icons/icons/flat-icons/database.svg"

    @property
    def toolbar(self) -> list[widgets.ActionButton]:
        return [widgets.ActionButton(self.add3DView, "3D", u":/flat-icons/icons/flat-icons/cube.png"),
                widgets.ActionButton(self.saveChannels, "Export", u":/flat-icons/icons/flat-icons/add_image.svg"),
                widgets.ActionButton(self.loadOrthogonalViews, "Orthogonal Views", u":/flat-icons/icons/flat-icons/grid.svg")]

    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)
        self.threadpool = QThreadPool()

        # Sliders #
        self.sliders = SliderListWidget()

        # View #
        self.imageview = widgets.ImageWidget(sliders = self.sliders)

        # Layout #
        self.layout.addWidget(self.imageview)
        self.layout.addWidget(self.sliders)


    def loadFiles(self, files: list[str]):
        filepath = ""
        if type(files) is str:
            filepath = files
        elif type(files) is list and len(files) > 0:
            filepath = files[0]

        print(f"🔃 loading {filepath}")
        fw = FileLoaderWorker(filepath)
        fw.signals.loaded.connect(self.imageview.setStack)
        self.threadpool.start(fw)

    def add3DView(self):
        pass

    def saveChannels(self):
        pass

    def loadOrthogonalViews(self):
        pass

    def dropEvent(self, event: QGraphicsSceneDragDropEvent):
        super().dropEvent(event)

        if event.mimeData().hasUrls:
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.loadFiles(links)
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


class FileLoaderSignals(QObject):
    loaded = Signal(object)
    error = Signal()

class FileLoaderWorker(QRunnable):
    def __init__(self, filepath: str):
        super(FileLoaderWorker, self).__init__()

        self.filepath = filepath
        self.signals = FileLoaderSignals()

    @Slot()
    def run(self):
        imagestack = damaker.load(
            self.filepath,
            data_loader=damaker.stream.dataloader_tifffile,
            metadata_loader=damaker.stream.metadataloader_bioformats
        )

        if imagestack != None:
            self.signals.loaded.emit(imagestack)
        else:
            self.signals.error.emit()