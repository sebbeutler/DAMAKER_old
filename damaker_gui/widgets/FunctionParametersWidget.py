from PySide2.QtWidgets import QFrame
from deprecated import deprecated

from damaker_gui.widgets.FilePickerWidget import FolderPickerWidget
from damaker_gui.windows.UI_FunctionParametersWidget import Ui_FunctionParameters

def clearLayout(layout):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        widgetToRemove.setParent(None)

@deprecated("Widget from V1")
class FunctionParametersWidget(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FunctionParameters()
        self.ui.setupUi(self)
        
        self.outputDir = FolderPickerWidget("", 18, "Output path: ")
        self.ui.frame_outputDir.layout().addWidget(self.outputDir)
        
        self.setHiddenAll(True)
        self.function = None
    
    @property
    def batchModeEnabled(self):
        return self.ui.btn_batchMode.isChecked()
    
    def setHiddenAll(self, hide=True):
        self.outputDir.setHidden(hide)
        self.ui.btn_batchMode.setHidden(hide)
        self.ui.btn_add_operation.setHidden(hide)
        self.ui.btn_modify_operation.setHidden(hide)
        self.ui.edit_operation_name.setHidden(hide)
        self.ui.checkbox_enabled.setHidden(hide)            
    
    def clearForm(self):
        for i in reversed(range(self.ui.layout_settingsForm.rowCount())): 
            self.ui.layout_settingsForm.removeRow(i)
        
    
    