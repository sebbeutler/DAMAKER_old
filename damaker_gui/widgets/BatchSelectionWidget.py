from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from damaker_gui.widgets.WorkspaceWidget import WorkspaceWidget

from .FilePickerWidget import FolderPickerWidget

from damaker.pipeline import BatchParameters
from damaker_gui import widgets

from damaker_gui.windows.UI_BatchParametersWidget import Ui_BatchParameters

class BatchSelectionWidget(QScrollArea):
    def __init__(self, parameters: BatchParameters=None):
        super().__init__()
        self.ui = Ui_BatchParameters()
        self.ui.setupUi(self)
        
        self.inputPath = FolderPickerWidget(WorkspaceWidget.RootPath)
        self.ui.batch_form_layout.insertRow(0, "Input folder: ", self.inputPath)
        
        self.ui.topBar.setHidden(True)
        
        self.ui.btn_deploy.clicked.connect(self.deploy)
        self.ui.btn_add_mod.clicked.connect(self.addMod)
        
        self.modCounter = 0
        
        if parameters != None:
            self.setParameters(parameters)
        
        # self.deploy()
    
    def getBatch(self):
        params = BatchParameters()
        params.folder = self.inputPath.text()
        params.file = self.ui.filename_input.text()
        params.associated = self.ui.checkBox_associated.isChecked()
        params.mods = []
        for i in range(4, self.ui.batch_form_layout.rowCount()):
            mod: QLineEdit = self.ui.batch_form_layout.itemAt(i, QFormLayout.ItemRole.FieldRole).widget()
            params.mods.append(mod.text())
        return params            
    
    def addMod(self):
        self.modCounter += 1
        self.ui.batch_form_layout.addRow("Mod {%d}: " % self.modCounter, QLineEdit())
        self.ui.batch_form.adjustSize()
        self.ui.BatchParametersContent.adjustSize()
        self.adjustSize()
        
    def setParameters(self, params: BatchParameters):
        self.inputPath.setText(params.folder)
        self.ui.filename_input.setText(params.file)
        self.ui.checkBox_associated.setChecked(params.associated)
        for mod in params.mods:
            self.modCounter += 1
            modEdit =  QLineEdit()
            modEdit.setText(mod)
            self.ui.batch_form_layout.addRow("Mod {%d}: " % self.modCounter, modEdit)            
    
    def deploy(self):
        # self.hideAnimation = QPropertyAnimation(self.ui.form, b'geometry')
        # self.hideAnimation.setDuration(2000) # chose the value that fits you
        
        # self.hideAnimation.setStartValue(self.ui.form.geometry())
        # geo = QRect(self.ui.form.geometry())
        # geo.setHeight(200)
        # #computing final geometry
        # self.hideAnimation.setEndValue(geo)
        # self.hideAnimation.start()
        self.ui.batch_form.setHidden(not self.ui.batch_form.isHidden())
        if self.ui.batch_form.isHidden():
            self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.adjustSize()