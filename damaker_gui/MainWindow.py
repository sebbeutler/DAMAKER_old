if __name__ == '__main__':
    import os
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_MainWindowV2.py --from-imports ./damaker_gui/windows/MainWindowV2.ui")
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_BatchParametersWidget.py --from-imports ./damaker_gui/windows/BatchParametersWidget.ui")

import sys
import damaker_gui.widgets as widgets
from damaker_gui.windows.UI_MainWindowV2 import *

class MainWindow(QMainWindow):

    def __init__(self, app: QApplication):
        super().__init__()
        app.Window = self
        # self.show()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        
        # -Workspace- #
        self.workspace = widgets.WorkspaceWidget()
        self.workspace.signalOpen.connect(self.openFile)        
        self.ui.dock2_2.addTab(self.workspace)
        
        # -Settings-
        self.settings = widgets.AppSettingsWidget()
        self.settings.theme.setTheme("Dark")
        self.ui.dock2_2.addTab(self.settings)
        
        # -Console- #
        self.console = widgets.ConsoleWidget()
        self.ui.dock2_2.addTab(self.console)
        
        # -FileInfo- #
        self.fileInfo = widgets.FileInfoWidget()
        self.ui.dock2_1.addTab(self.fileInfo)
        
        # # -LUT selector- #
        # self.lutSelector = widgets.LutSelectorWidget()
        
        # # -Orthogonal projection- #
        # self.orthogonalProjection = widgets.OrthogonalProjectionWidget()
        
        # # -Preview Z-Stack- #
        # self.ui.dock1.addTab(widgets.PreviewFrame(fileInfo=self.fileInfo))
        
        # # -Pipeline- #
        # self.pipeline = widgets.PipelineWidget()
        # self.ui.dock1.addTab(self.pipeline)
        
        # # -Operations- #
        # self.operationList = widgets.FunctionListWidget()
        # self.ui.dock2.addTab(self.operationList)
        
        # # -Open file from args- #
        # for arg in sys.argv[1:]:
        #     self.openFile(arg)
        
        self.showMaximized()
        
    @property
    def docks(self) -> list[ContentDock]:
        return [self.ui.dock1_1, self.ui.dock1_2, self.ui.dock2_1, self.ui.dock2_2, self.ui.dock2_3]
    
    def addTab(self, dockId: int=1, widget: QWidget=QWidget()) -> ContentDock:
        for i in range(self.docks):
            if i == dockId:
                self.docks[i].addTab(widget)
        return self

    def getTabByName(self, name: str) -> QWidget:
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
            self.docks[0].addTab(widgets.PreviewFrame(path=path, fileInfo=self.fileInfo))
        else:
            self.ui.statusbar.showMessage(f"No suitable format found for file: '{path}'", 10000)
            print(f"📛 No suitable format found for file: '{path}'")
        
    def keyPressEvent(self, event):
        # print(f"Key: {str(event.key())} Text Press: {str(event.text())}")
        if event.key() == Qt.Key_Escape:
            self.close()
        return super().keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())