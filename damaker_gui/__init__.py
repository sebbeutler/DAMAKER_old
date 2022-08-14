
import os, sys
# from __future__ import annotations

_filedir = os.path.dirname(__file__)
os.system(f"pyside2-uic -o {_filedir}/windows/UI_MainWindowV2.py --from-imports {_filedir}/windows/MainWindowV2.ui")
os.system(f"pyside2-uic -o {_filedir}/windows/UI_BatchParametersWidget.py --from-imports {_filedir}/windows/BatchParametersWidget.ui")

from PySide2.QtWidgets import QApplication
App = QApplication(sys.argv)

from damaker_gui.MainWindow import MainWindow

def Window() -> MainWindow:
    if not hasattr(App, 'Window'):
        App.Window = None
    return App.Window

def run(exit=True):
    MainWindow(App)
    # TODO: Splash screen
    print(sys.argv)
    if exit:
        sys.exit(App.exec_())
    else:
        App.exec_()
