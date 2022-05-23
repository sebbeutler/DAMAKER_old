from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

class FilePickerWidget(QWidget):
    def __init__(self, workspace: str, height: int=20):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout = QHBoxLayout()
        self.layout.setMargin(0)
        self.textEdit = QLineEdit()
        self.textEdit.setFixedHeight(height)
        self.btnBrowse = QPushButton("Browse")
        self.btnBrowse.setFixedHeight(height)
        self.btnBrowse.clicked.connect(self.changePath)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.btnBrowse)
        self.setLayout(self.layout)
        self.setFixedHeight(height)
        self.workspace = workspace
    
    def setText(self, filePath):        
        self.textEdit.setText(filePath)
        self.textEdit.setToolTip(filePath)
    
    def text(self):
        return self.textEdit.text()
    
    def changePath(self):
        filePath = QFileDialog.getOpenFileName(None, 'Open file', 
         self.workspace,"Any (*.*)")[0]
        self.setText(filePath)

class FolderPickerWidget(QWidget):
    def __init__(self, workspace: str, height: int=20, label: str=""):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout = QHBoxLayout()
        self.layout.setMargin(0)        
        if label != "":
            self.layout.addWidget(QLabel(label))
        self.textEdit = QLineEdit()
        self.textEdit.setFixedHeight(height)
        self.btnBrowse = QPushButton("Browse")
        self.btnBrowse.setFixedHeight(height)
        self.btnBrowse.clicked.connect(self.changePath)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.btnBrowse)
        self.setLayout(self.layout)
        self.setFixedHeight(height)
        self.workspace = workspace
    
    def setText(self, filePath):        
        self.textEdit.setText(filePath)
        self.textEdit.setToolTip(filePath)
    
    def text(self):
        return self.textEdit.text()
    
    def changePath(self):
        filePath = QFileDialog.getExistingDirectory(None, 'Open Folder', 
         self.workspace)
        self.setText(filePath)
        