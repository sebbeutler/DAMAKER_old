if __name__ == '__main__':
    import os
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_MainWindowV2.py --from-imports ./damaker_gui/windows/MainWindowV2.ui")
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_BatchParametersWidget.py --from-imports ./damaker_gui/windows/BatchParametersWidget.ui")

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *
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
        
        # -Console-
        self.ui.dock3.addTab(widgets.ConsoleWidget())
        
        # -FileInfo-
        self.fileInfo = widgets.FileInfoWidget()
        self.ui.dock2.addTab(self.fileInfo)
        
        # -Workspace-
        self.workspace = widgets.WorkspaceWidget()
        self.workspace.signalOpen.connect(self.openFile)        
        self.ui.dock4.addTab(self.workspace)
        
        # -Preview Z-Stack-
        self.ui.dock1.addTab(widgets.PreviewFrame(fileInfo=self.fileInfo))
        self.pipeline = widgets.PipelineWidget()
        self.ui.dock1.addTab(self.pipeline)
        
        # -Operations-
        self.fl = widgets.FunctionListWidget()
        self.pipeline.connectTo(self.fl)
        self.ui.dock2.addTab(self.fl)
        
        # self.ortho = Q
        
        # self.menu_view = self.ui.menubar.addMenu("View")
        # self.menu_view.addAction("")
        
        self.showMaximized()
    
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