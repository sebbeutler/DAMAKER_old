
import os, sys
from typing_extensions import Self
# from __future__ import annotations

_filedir = os.path.dirname(__file__)
os.system(f"pyside2-uic -o {_filedir}/ui/UI_MainWindowV2.py --from-imports {_filedir}/ui/MainWindowV2.ui")
os.system(f"pyside2-uic -o {_filedir}/ui/UI_BatchParametersWidget.py --from-imports {_filedir}/ui/BatchParametersWidget.ui")
os.system(f"pyside2-uic -o {_filedir}/ui/UI_FunctionForm.py --from-imports {_filedir}/ui/FunctionForm.ui")

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtCore import Signal, Qt
App = QApplication(sys.argv)

import damaker_gui.widgets as widgets
from damaker_gui.ui.UI_MainWindowV2 import Ui_MainWindow

def setStatusMessage(msg: str, duration: int=0):
    if MainWindow.Instance != None:
        MainWindow.Instance.ui.statusbar.showMessage(msg, duration)

def run(exit=True):
    MainWindow(App)
    # TODO: Splash screen
    print(sys.argv)
    if exit:
        sys.exit(App.exec_())
    else:
        App.exec_()

class MainWindow(QMainWindow):
    tabSelected = Signal(QWidget)
    tabChanged = Signal()
    viewChanged = Signal(widgets.IView)
    Instance: None | Self = None

    def __init__(self, app: QApplication):
        super().__init__()
        MainWindow.Instance = self

        # self.show()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlag(Qt.FramelessWindowHint)

        self._docks: list[widgets.ContentDock] = []
        for key, value in self.ui.__dict__.items():
            if key.startswith('dock'):
                dock: widgets.ContentDock = value
                self._docks.append(dock)
                dock.connectCurrentChanged(self.tabSelected.emit)
                dock.tabChangedSignal.connect(self.tabChanged.emit)

        # -Workspace- #
        self.workspace = widgets.WorkspaceWidget()
        self.workspace.signalOpen.connect(self.openFile)        
        self.ui.dock1_2.addTab(self.workspace)

        # -Settings-
        self.settings = widgets.AppSettingsWidget()
        self.settings.theme.setTheme("Dark")
        self.ui.dock1_3.addTab(self.settings)

        # -Console- #
        self.console = widgets.ConsoleWidget()
        self.ui.dock1_3.addTab(self.console)

        # -ROIs- #
        self.roi = widgets.ROIWidget()
        self.ui.dock2_2.addTab(self.roi)
        self.ui.dock2_2.setCurrentIndex(2)

        # -Preview Z-Stack- #
        self.ui.dock1_1.addTab(widgets.PreviewFrame())
        self.ui.dock1_1.addTab(widgets.PreviewFrame())

        # -Operations- #
        self.operationList = widgets.FunctionListWidget()
        self.ui.dock2_2.addTab(self.operationList)

        # -Pipeline- #
        self.pipeline = widgets.PipelineViewer()
        self.ui.dock2_1.addTab(self.pipeline)
        self.operationList.connectPipeline(self.pipeline)

        # -LUT- #
        self.colorMap = widgets.LutSelectorWidget()
        self.ui.dock2_3.addTab(self.colorMap)

        # -Brightness&Contrast- #
        self.colorAdjust = widgets.ColorAdjustWidget()
        self.ui.dock2_2.addTab(self.colorAdjust)

        # -Open file from args- #
        for arg in sys.argv[1:]:
            self.openFile(arg)

        # self.showMaximized()
        self.show()
        self.setFocus(Qt.FocusReason.PopupFocusReason)

    @property
    def docks(self) -> list[widgets.ContentDock]:
        return self._docks

    @property
    def currentViews(self) -> list[widgets.IView]:
        views = []
        for dock in self.docks:
            widget = dock.currentWidget().widget
            if issubclass(type(widget), widgets.IView):
                views.append(widget)
        return views

    def addTab(self, dockId: int=1, widget: QWidget=QWidget()) -> widgets.ContentDock:
        raise "Select target dock !!!!"
        for i in range(self.docks):
            if i == dockId:
                self.docks[i].addTab(widget)
        return self

    def getTabByName(self, name: str) -> QWidget | None:
        for dock in self.docks:
            widget = dock.getTabByName(name)
            if widget != None:
                return widget
        return None

    def getTabsByType(self, _type: type) -> list[QWidget]:
        _widgets = []
        for dock in self.docks:
            _widgets += dock.getTabsByType(_type)
        return _widgets            

    def closeTab(self, widget: QWidget) -> bool:
        for dock in self.docks:
            if dock.closeTab(dock.getWidgetIndex(widget)):
                return True
        return False

    def openFile(self, path: str):
        if path.endswith(".tif") or path.endswith(".tiff"):
            self.docks[0].addTab(widgets.PreviewFrame(path=path))
        else:
            self.ui.statusbar.showMessage(f"No suitable format found for file: '{path}'", 10000)
            print(f"📛 No suitable format found for file: '{path}'")

    def keyPressEvent(self, event):
        # print(f"Key: {str(event.key())} Text Press: {str(event.text())}")
        if event.key() == Qt.Key_Escape:
            self.close()
        return super().keyPressEvent(event)
