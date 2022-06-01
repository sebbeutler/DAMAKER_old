from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from .FilePickerWidget import FolderPickerWidget

from damaker.pipeline import BatchParameters

from damaker_gui.windows.UI_BatchParametersWidget import Ui_BatchParameters

class BatchSelectionWidget(QFrame):
    def __init__(self, workspace: str, parameters: BatchParameters=None):
        super().__init__()
        self.ui = Ui_BatchParameters()
        self.ui.setupUi(self)
        
        self.ui.btn_deploy.clicked.connect(self.deploy)
    
    def deploy(self):
        self.hideAnimation = QPropertyAnimation(self.ui.form, b'geometry')
        self.hideAnimation.setDuration(2000) # chose the value that fits you
        
        self.hideAnimation.setStartValue(self.ui.form.geometry())
        geo = QRect(self.ui.form.geometry())
        geo.setHeight(200)
        #computing final geometry
        self.hideAnimation.setEndValue(geo)
        print(geo)
        self.hideAnimation.start()
        
    def applyEvent(self, params: BatchParameters):
        self.output = params
    
    def onClick(self):
        if not self.window.isVisible():
            self.window.show()
        else:
            self.window.setFocus()
    
    def getBatch(self):
        return self.output

# class BatchSelectionWidget(QPushButton):
#     def __init__(self, workspace: str, parameters: BatchParameters=None):
#         super().__init__("Batch parameters")
#         self.workspace = workspace
#         self.clicked.connect(self.onClick)
#         self.window = BatchSelectionWindow(self.workspace)
#         if parameters is None:
#             self.output = BatchParameters()    
#         else:
#             self.output = parameters
#         self.window.setText(self.output)
#         self.window.onApply.connect(self.applyEvent)
    
#     def applyEvent(self, params: BatchParameters):
#         self.output = params
    
#     def onClick(self):
#         if not self.window.isVisible():
#             self.window.show()
#         else:
#             self.window.setFocus()
    
#     def getBatch(self):
#         return self.output

class BatchSelectionWindow(QMainWindow):
    onApply = Signal(BatchParameters)
    
    def __init__(self, workspace: str, ):
        super().__init__()
        self.setWindowTitle("Batch Selection")
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        
        self.mainWidget = QWidget(self)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setMargin(5)
        
        self.layoutFolder = QHBoxLayout()
        self.layoutFolder.addWidget(QLabel("Folder: "))
        self.layoutFolder.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.folder = FolderPickerWidget(workspace, 18)
        self.layoutFolder.addWidget(self.folder)
        self.layoutFolder.setMargin(0)      
        self.mainLayout.addLayout(self.layoutFolder)
        
        self.layoutMod1 = QHBoxLayout()
        self.layoutMod1.addWidget(QLabel("Mod {1}: "))
        self.layoutMod1.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.mod1Edit = QLineEdit()
        self.mod1Edit.setFixedHeight(18)
        self.mod1Edit.setMinimumWidth(212)
        self.layoutMod1.addWidget(self.mod1Edit)
        self.layoutMod1.setMargin(0)     
        self.mainLayout.addLayout(self.layoutMod1)
        
        self.layoutMod2 = QHBoxLayout()
        self.layoutMod2.addWidget(QLabel("Mod {2}: "))
        self.layoutMod2.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.mod2Edit = QLineEdit()
        self.mod2Edit.setFixedHeight(18)
        self.mod2Edit.setMinimumWidth(212)
        self.layoutMod2.addWidget(self.mod2Edit)
        self.layoutMod2.setMargin(0)
        self.mainLayout.addLayout(self.layoutMod2)
        
        self.layoutFile = QHBoxLayout()
        self.layoutFile.addWidget(QLabel("File: "))
        self.layoutFile.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.fileEdit = QLineEdit()
        self.fileEdit.setMinimumWidth(212)
        self.fileEdit.setFixedHeight(18)
        self.layoutFile.addWidget(self.fileEdit)
        self.layoutFile.setMargin(0)  
        self.mainLayout.addLayout(self.layoutFile)
        
        self.btnApply = QPushButton("Apply")
        self.btnApply.clicked.connect(self.apply)
        self.mainLayout.addWidget(self.btnApply)
        
        self.workspace = workspace
        
        self.mainWidget.setLayout(self.mainLayout)
        self.mainWidget.setMinimumSize(300, 122)
        self.setMinimumSize(300, 122)
    
    def apply(self):
        param = BatchParameters()
        param.folder = self.folder.text()
        param.mod1 = self.mod1Edit.text()
        param.mod2 = self.mod2Edit.text()
        param.file = self.fileEdit.text()
        self.onApply.emit(param)
        self.close()
    
    def setText(self, param: BatchParameters):
        self.folder.textEdit.setText(param.folder)
        self.mod1Edit.setText(param.mod1)
        self.mod2Edit.setText(param.mod2)
        self.fileEdit.setText(param.file)
