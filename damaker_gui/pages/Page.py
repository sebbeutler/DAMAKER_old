from abc import ABC, abstractmethod
 
from damaker_gui.windows.UI_MainWindow import Ui_MainWindow
 
class Page:    
    ui: Ui_MainWindow
    
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui