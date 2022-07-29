if __name__ == '__main__':
    import os
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_MainWindowV2.py --from-imports ./damaker_gui/windows/MainWindowV2.ui")

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys
from damaker_gui.widgets import ContentFrame
from damaker_gui.widgets.ConsoleWidget import ConsoleWidget
from damaker_gui.widgets.PreviewWidget import PreviewFrame, PreviewWidget
from damaker_gui.widgets.WorkspaceWidget import WorkspaceWidget

from damaker_gui.windows.UI_MainWindowV2 import *



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("ui loaded: ✔")
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.ui.menubar._mouseMoveEvent = self.ui.menubar.mouseMoveEvent
        # self.ui.menubar.mouseMoveEvent = self.moveWindowEvent
        # self.ui.menubar._mousePressEvent = self.ui.menubar.mousePressEvent
        # self.ui.menubar.mousePressEvent = self.mousePressEvent
        
        # self.btn = QPushButton("test", self.ui.menubar)
        self.ui.dock1.addTab(PreviewFrame())
        self.workspace = WorkspaceWidget()
        self.workspace.signalOpen.connect(self.openFile)
        self.ui.dock4.addTab(self.workspace)
        self.ui.dock3.addTab(ConsoleWidget())
        
        
        # self.menu_view = self.ui.menubar.addMenu("View")
        # self.menu_view.addAction("")
        
        self.showMaximized()
    
    def openFile(self, path: str):
        if path.endswith(".tif") or path.endswith(".tiff"):
            self.ui.dock1.addTab(PreviewFrame(path=path))
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

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()