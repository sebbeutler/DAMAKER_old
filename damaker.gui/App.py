from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

if __name__ == '__main__':
    import os
    os.system(".\scripts\generate-ui.bat")

from windows.UI_MainWindow import *

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()        
        self.setupUi()
        
        self.show()

    def setupUi(self):
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)
        
        self.ui.frame_top.mouseMoveEvent = self.evt_moveWindow
        self.ui.btn_exit.mouseReleaseEvent = lambda e : super(AppWindow, self).mouseReleaseEvent(e) if self.close() or 1 else None
        self.ui.btn_minimize.mouseReleaseEvent = lambda e : super(AppWindow, self).mouseReleaseEvent(e) if self.showMinimized() or 1 else None
        
        self.sizegrip = QSizeGrip(self.ui.btn_resize_grip)
        
        # ------------------------------------------------------------------------------------------------
        
        self.fileSystemModel = QFileSystemModel(self.ui.treeview_workspace)
        self.fileSystemModel.setReadOnly(False)        
        root = self.fileSystemModel.setRootPath("/")
        
        self.ui.treeview_workspace.setModel(self.fileSystemModel)
        self.ui.treeview_workspace.setRootIndex(root)
        
        self.ui.treeview_workspace.setColumnHidden(1, True)
        self.ui.treeview_workspace.setColumnHidden(2, True)
        self.ui.treeview_workspace.setColumnHidden(3, True)
        
        
        self.setFocus()

    def keyPressEvent(self, event):
        print(f"Key: {str(event.key())} Text Press: {str(event.text())}")
        if event.key() == Qt.Key_Escape:
            self.close()
        return super(AppWindow, self).keyPressEvent(event)
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        return super(AppWindow, self).mousePressEvent(event)
    
    def evt_moveWindow(self, event):
        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == '__main__':
    import sys    
    app = QApplication(sys.argv)
    window = AppWindow()
    
    sys.exit(app.exec_())
