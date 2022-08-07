if __name__ == '__main__':
    import os
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_MainWindowV2.py --from-imports ./damaker_gui/windows/MainWindowV2.ui")
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_BatchParametersWidget.py --from-imports ./damaker_gui/windows/BatchParametersWidget.ui")

import sys
import damaker_gui.widgets as widgets
from damaker_gui.windows.UI_MainWindowV2 import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.show()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # print("ui loaded: ✔")
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.ui.menubar._mouseMoveEvent = self.ui.menubar.mouseMoveEvent
        # self.ui.menubar.mouseMoveEvent = self.moveWindowEvent
        # self.ui.menubar._mousePressEvent = self.ui.menubar.mousePressEvent
        # self.ui.menubar.mousePressEvent = self.mousePressEvent
        
        # self.btn = QPushButton("test", self.ui.menubar)
        
        # -Settings-
        self.settings = widgets.AppSettingsWidget()
        self.ui.dock4.addTab(self.settings)
        
        # -Workspace- #
        self.workspace = widgets.WorkspaceWidget()
        self.workspace.signalOpen.connect(self.openFile)        
        self.ui.dock4.addTab(self.workspace)
        
        # -Console- #
        self.ui.dock3.addTab(widgets.ConsoleWidget())
        
        # -FileInfo- #
        self.fileInfo = widgets.FileInfoWidget()
        self.ui.dock2.addTab(self.fileInfo)
        
        # -LUT selector- #
        self.lutSelector = widgets.LutSelectorWidget()
        
        # -Orthogonal projection- #
        self.orthogonalProjection = widgets.OrthogonalProjectionWidget()
        
        # -Preview Z-Stack- #
        self.ui.dock1.addTab(widgets.PreviewFrame(fileInfo=self.fileInfo))
        self.pipeline = widgets.PipelineWidget()
        self.ui.dock1.addTab(self.pipeline)
        
        # -Operations- #
        self.operationList = widgets.FunctionListWidget()
        self.ui.dock2.addTab(self.operationList)
        
        # self.ortho = Q
        
        
        # self.menu_view = self.ui.menubar.addMenu("View")
        # self.menu_view.addAction("")
        
        for arg in sys.argv[1:]:
            self.openFile(arg)
        
        self.showMaximized()
        
    @property
    def docks(self):
        return [self.ui.dock1, self.ui.dock2, self.ui.dock3, self.ui.dock4]
    
    def addTab(self, dockId: int=1, widget: QWidget=QWidget(), tabName: str="None") -> QWidget:
        if dockId == 1:
            self.ui.dock1.addTab(widget, tabName)
        if dockId == 2:
            self.ui.dock2.addTab(widget, tabName)
        if dockId == 3:
            self.ui.dock3.addTab(widget, tabName)
        if dockId == 4:
            self.ui.dock4.addTab(widget, tabName)
        return widget

    def closeTab(self, widget: QWidget) -> bool:
        for dock in self.docks:
            if dock.closeTab(dock.getWidgetIndex(widget)):
                return True
        return False
                    
    
    def openFile(self, path: str):
        if path.endswith(".tif") or path.endswith(".tiff"):
            self.ui.dock1.addTab(widgets.PreviewFrame(path=path, fileInfo=self.fileInfo))
        else:
            self.ui.statusbar.showMessage(f"No suitable format found for file: '{path}'", 10000)
        
    # ------------------ @ EVENTS ------------------   
    def keyPressEvent(self, event):
        # print(f"Key: {str(event.key())} Text Press: {str(event.text())}")
        if event.key() == Qt.Key_Escape:
            self.close()
        return super().keyPressEvent(event)
    
    # def mousePressEvent(self, event):
    #     self.dragPos = event.globalPos()
    #     self.ui.menubar._mousePressEvent(event)
    
    # def moveWindowEvent(self, event):
    #     # MOVE WINDOW
    #     if event.buttons() == Qt.LeftButton:
    #         new_pos: QPoint = self.pos() + event.globalPos() - self.dragPos
    #         # new_pos.setX(max(0, new_pos.x()))
    #         new_pos.setY(max(0, new_pos.y()))
    #         self.move(new_pos)
    #         self.dragPos = event.globalPos()
    #         event.accept()
        
    #     self.ui.menubar._mouseMoveEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())