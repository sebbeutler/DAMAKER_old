from PySide2.QtWidgets import QApplication
import sys
from damaker_gui.MainWindow import MainWindow

def run() -> MainWindow:    
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    return window