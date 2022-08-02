
import os
_filedir = os.path.dirname(__file__)
os.system(f"pyside2-uic -o {_filedir}/windows/UI_MainWindowV2.py --from-imports {_filedir}/windows/MainWindowV2.ui")
os.system(f"pyside2-uic -o {_filedir}/windows/UI_BatchParametersWidget.py --from-imports {_filedir}/windows/BatchParametersWidget.ui")

from PySide2.QtWidgets import QApplication
from damaker_gui.MainWindow import MainWindow

def run() -> MainWindow:
    # TODO: Splash screen
    import sys
    print(sys.argv)
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    return window