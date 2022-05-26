from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *
from damaker_gui.widgets.FilePickerWidget import FolderPickerWidget
from damaker_gui.windows.UI_FunctionParametersWidget import Ui_FunctionParameters

def clearLayout(layout):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        widgetToRemove.setParent(None)

class FunctionParametersWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FunctionParameters()
        self.ui.setupUi(self)
        
        self.outputDir = FolderPickerWidget("", 18, "Output path: ")
        self.outputDir.setHidden(True)
        self.ui.frame_outputDir.layout().addWidget(self.outputDir)
        
        self.ui.btn_add_operation.setHidden(True)
        self.ui.btn_modify_operation.setHidden(True)
        self.ui.edit_operation_name.setHidden(True)
        self.ui.checkbox_enabled.setHidden(True)
    
    def clearLayouts(self):            
        clearLayout(self.ui.layout_fnames)
        clearLayout(self.ui.layout_fargs)
    
    