from email import utils
import inspect, enum
import numpy as np
import re
from inspect import getmembers, isfunction, signature   

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from vedo import Mesh

from damaker_gui.widgets.FunctionListWidget import FunctionsListWidget

from .widgets.PreviewWidget import PreviewWidget
from .widgets.FilePickerWidget import FilePickerWidget, FolderPickerWidget
from .widgets.EnumComboBox import EnumComboBox
from .widgets.BatchSelectionWidget import BatchSelectionWidget
 
import damaker.processing
import damaker.utils
from damaker.Channel import Channel, Channels, SingleChannel
from damaker.utils import StrFilePath, StrFolderPath
from damaker.pipeline import BatchParameters, NamedArray, Operation, Pipeline, BatchOperation

from .windows.UI_MainWindow import Ui_MainWindow

def clearLayout(layout):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        widgetToRemove.setParent(None)

class PlanPage:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.preview = PreviewWidget(self.ui.previewPipelineView, self.ui.previewPipelineSlider, [], self.ui.fileInfo)
        self.pipelineThread = None
        
        self.ui.btn_add_operation.clicked.connect(self.addOperation)
        self.ui.btn_modify_operation.clicked.connect(self.modifyOperation)
        
        self.ui.btn_add_operation.setHidden(True)
        self.ui.btn_modify_operation.setHidden(True)
        self.ui.edit_operation_name.setHidden(True)
        self.ui.checkbox_enabled.setHidden(True)
        
        self.selectedOperationItem = None
        
        self.ui.list_operations.itemDoubleClicked.connect(self.operationListClicked)
        self.ui.btn_run_pipeline.clicked.connect(self.runPipeline)
        self.ui.btn_remove_operation.clicked.connect(self.removeOperationFromList)
        self.ui.btn_save_pipeline.clicked.connect(self.savePipeline)
        self.ui.btn_load_pipeline.clicked.connect(self.loadPipeline)
        
        self.pipelineRunning = False
        
        self.outputDir = FolderPickerWidget(self.ui.fileSystemModel.rootPath(), 18, "Output path: ")
        self.outputDir.setHidden(True)
        self.ui.frame_outputDir.layout().addWidget(self.outputDir)
        
        self.functions = FunctionsListWidget()
        self.functions.operationTriggered.connect(lambda name: self.functionListClicked(name))
        self.ui.functions_layout.addWidget(self.functions)
        
        # pr = BatchParameters()
        # pr.folder = "C:/Users/PC/source/DAMAKER/resources/batch"
        # pr.mod1 = "E1;E2"
        # pr.mod2 = ""
        # pr.file = "{1}.tif"
        # self.ui.list_operations.addItem(
        #     ListWidgetOperation(
        #         BatchOperation(damaker.processing.registrationMultiChannel, 
        #                        [pr, "C:/Users/PC/source/DAMAKER/resources/registration/C1-E0.tif", 1, 100, "C:/Users/PC/source/DAMAKER/resources/output/out-reg"], 
        #                        "registration", True, "")))

    def addOperation(self, event):
        func = self.functions.getFunction(self.ui.currentFunction.text())
        if func is None:
            return
        
        name = self.ui.edit_operation_name.text()
        enabled = self.ui.checkbox_enabled.isChecked()
        outputPath = self.outputDir.text()
        
        args = []        
        for i in range(self.ui.layout_fargs.count()):
            widget = self.ui.layout_fargs.itemAt(i).widget()
            
            if type(widget) is QSpinBox:
                args.append(int(widget.value()))
            elif type(widget) is QDoubleSpinBox:
                args.append(float(widget.value()))
            elif type(widget) is EnumComboBox:
                sel = widget.currentText()
                for e in widget.enum:
                    if e.name == sel:
                        args.append(e)
                        break
            elif type(widget) is BatchSelectionWidget:
                args.append(widget.getBatch())
            elif type(widget) in [QLineEdit, FilePickerWidget, FolderPickerWidget]:
                args.append(widget.text())
            elif type(widget) is QCheckBox:
                args.append(widget.isChecked())
            else:
                args.append(None)
        listwidget = ListWidgetOperation(BatchOperation(func, args, name, enabled, outputPath))
        self.ui.list_operations.addItem(listwidget)
        self.ui.list_operations.setCurrentItem(listwidget)
        self.operationListClicked()
    
    def modifyOperation(self, event):
        if self.selectedOperationItem is None:
            return
        
        name = self.ui.edit_operation_name.text()
        enabled = self.ui.checkbox_enabled.isChecked()
        outputPath = self.outputDir.text()
        
        args = []        
        for i in range(self.ui.layout_fargs.count()):
            widget = self.ui.layout_fargs.itemAt(i).widget()
            
            if type(widget) is QSpinBox:
                args.append(int(widget.value()))
            elif type(widget) is QDoubleSpinBox:
                args.append(float(widget.value()))
            elif type(widget) is EnumComboBox:
                sel = widget.currentText()
                for e in widget.enum:
                    if e.name == sel:
                        args.append(e)
                        break
            elif type(widget) is BatchSelectionWidget:
                args.append(widget.getBatch())
            elif type(widget) in [QLineEdit, FilePickerWidget, FolderPickerWidget]:
                args.append(widget.text())
            elif type(widget) is QCheckBox:
                args.append(widget.isChecked())
            else:
                args.append(None)
        self.selectedOperationItem.operation.args = args
        self.selectedOperationItem.operation.name = name
        self.selectedOperationItem.operation.enabled = enabled
        self.selectedOperationItem.operation.outputPath = outputPath
        self.selectedOperationItem.updateText()

    def getOperationFromList(self, name: str):
        for i in range(self.ui.list_operations.count()):
            item = self.ui.list_operations.item(i)
            if item.name == name:
                return item.operation
        return None
    
    def functionListClicked(self, name):        
        clearLayout(self.ui.layout_fnames)
        clearLayout(self.ui.layout_fargs)
        self.ui.edit_operation_name.setHidden(False)
        self.ui.checkbox_enabled.setHidden(False)
        self.ui.btn_add_operation.setHidden(False)
        self.ui.btn_modify_operation.setHidden(True)
        
        func = self.functions.getFunction(name)
        if func == None:
            return
        self.ui.currentFunction.setText(name)
        sign = signature(func)
        self.ui.edit_operation_name.setText(func.__name__)
        self.ui.checkbox_enabled.setChecked(True)
        
        if sign.return_annotation in [Channel, Channels, NamedArray]:
            self.outputDir.setHidden(False)
            self.outputDir.setText("")
        else:
            self.outputDir.setHidden(True)
        
        for name in sign.parameters:
            param = sign.parameters[name]
            if param.annotation == inspect._empty:
                continue
            
            default_arg = None
            if param.default != inspect._empty:
                default_arg = param.default   
            
            label = QLabel(name)
            label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
            label.setFixedHeight(25)
            self.ui.layout_fnames.addWidget(label)
                
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if default_arg != None:
                    spinBox.setValue(int(default_arg))
                else:
                    spinBox.setValue(0)
                self.ui.layout_fargs.addWidget(spinBox)
            if param.annotation is float:
                spinBox = QDoubleSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if default_arg != None:
                    spinBox.setValue(float(default_arg))
                else:
                    spinBox.setValue(0.0)
                self.ui.layout_fargs.addWidget(spinBox)
            elif param.annotation in [Channel, Channels, BatchParameters, Mesh]:
                self.ui.layout_fargs.addWidget(BatchSelectionWidget(self.ui.fileSystemModel.rootPath()))
            elif param.annotation is SingleChannel:
                self.ui.layout_fargs.addWidget(FilePickerWidget(self.ui.fileSystemModel.rootPath()))
            elif param.annotation is StrFilePath:
                self.ui.layout_fargs.addWidget(FilePickerWidget(self.ui.fileSystemModel.rootPath()))
            elif param.annotation is StrFolderPath:
                self.ui.layout_fargs.addWidget(FolderPickerWidget(self.ui.fileSystemModel.rootPath()))
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setFixedHeight(18)
                if default_arg != None:
                    textEdit.setText(default_arg)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.ui.layout_fargs.addWidget(textEdit)
            elif type(param.annotation) is type(enum.Enum):
                self.ui.layout_fargs.addWidget(EnumComboBox(param.annotation))
            elif param.annotation is bool:
                checkBox = QCheckBox("")
                if default_arg != None:
                    checkBox.setChecked(default_arg)
                self.ui.layout_fargs.addWidget(checkBox)
            # else:
            #     label = QLabel("Unknown type")
            #     label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            #     self.ui.layout_fargs.addWidget(label)
    
    def operationListClicked(self):
        clearLayout(self.ui.layout_fnames)
        clearLayout(self.ui.layout_fargs)
        self.ui.edit_operation_name.setHidden(False)
        self.ui.checkbox_enabled.setHidden(False)
        self.ui.btn_add_operation.setHidden(True)
        self.ui.btn_modify_operation.setHidden(False)
        
        operation_items = self.ui.list_operations.selectedItems()
        if len(operation_items) == 0:
            return None
        self.selectedOperationItem = operation_items[0]
        operation: Operation = operation_items[0].operation
        self.ui.edit_operation_name.setText(operation.name)   
        self.ui.checkbox_enabled.setChecked(operation.enabled)
        
        sign = signature(operation.func)
        if sign.return_annotation in [Channel, Channels, NamedArray]:
            self.outputDir.setHidden(False)
            self.outputDir.setText(operation.outputPath)
        else:
            self.outputDir.setHidden(True)
        
        arg_id=0
        for name in sign.parameters:
            param = sign.parameters[name]
            if arg_id >= len(operation.args):
                arg = param.default
            else:                
                arg = operation.args[arg_id]
                      
            label = QLabel(name)
            label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)            
            label.setFixedHeight(25)
            self.ui.layout_fnames.addWidget(label)
            
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setFixedHeight(18)
                spinBox.setRange(-1000, 1000)
                spinBox.setValue(int(arg))
                self.ui.layout_fargs.addWidget(spinBox)
            elif param.annotation is float:
                spinBox = QDoubleSpinBox()
                spinBox.setFixedHeight(18)
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(25)
                spinBox.setValue(float(arg))
                self.ui.layout_fargs.addWidget(spinBox)
            elif param.annotation in [Channel, Channels, BatchParameters, Mesh]:    
                self.ui.layout_fargs.addWidget(BatchSelectionWidget(self.ui.fileSystemModel.rootPath(), arg))
            elif param.annotation is SingleChannel:
                filePicker = FilePickerWidget(self.ui.fileSystemModel.rootPath())
                filePicker.setText(arg)   
                self.ui.layout_fargs.addWidget(filePicker)    
            elif param.annotation is StrFilePath:
                filePicker = FilePickerWidget(self.ui.fileSystemModel.rootPath())
                filePicker.setText(arg)
                self.ui.layout_fargs.addWidget(filePicker)           
            elif param.annotation is StrFolderPath:
                folderPicker = FolderPickerWidget(self.ui.fileSystemModel.rootPath())
                folderPicker.setText(arg)
                self.ui.layout_fargs.addWidget(folderPicker)
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setFixedHeight(18)
                textEdit.setText(arg)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.ui.layout_fargs.addWidget(textEdit)            
            elif type(param.annotation) is type(enum.Enum):
                combBox = EnumComboBox(param.annotation)
                combBox.setCurrentText(arg.name)
                self.ui.layout_fargs.addWidget(combBox)
            elif param.annotation is bool:
                checkBox = QCheckBox("")
                checkBox.setChecked(arg)
                self.ui.layout_fargs.addWidget(checkBox)
            # else:
            #     label = QLabel("Unknown type")
            #     label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            #     self.ui.layout_fargs.addWidget(label)
            arg_id += 1
        
    def newOperationComboBox(self):
        comboBox = QComboBox()
        op_count = self.ui.list_operations.count()
        for i in range(op_count):
            item = self.ui.list_operations.item(i)
            comboBox.addItem(item.name)
        comboBox.addItem("None")
        comboBox.setCurrentText("None")                    
        comboBox.setDuplicatesEnabled(False)
        comboBox.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        comboBox.setFixedHeight(25)
        return comboBox

    def runPipeline(self):
        if self.pipelineRunning:
            self.pipelineStopped()
            return
        
        self.ui.edit_pipeline_output.setText("""
        <html><head><meta name="qrichtext" content="1" />
        </head><body style=" background-color: rgb(32, 32, 32); font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; 
        font-weight:400; font-style:normal;"></body></html>""")
        
        self.pipelineThread = PipelineRunnerThread(self.ui.list_operations)        
        self.pipelineThread.signals.outputReceived.connect(self.pipelineWriteConsole)
        self.pipelineThread.signals.stopped.connect(self.pipelineStopped)        
        self.pipelineThread.start()
        self.ui.btn_run_pipeline.setText("Stop")
        self.pipelineRunning = True
    
    def pipelineWriteConsole(self, text):
        self.ui.edit_pipeline_output.append(str(text))
        self.ui.edit_pipeline_output.moveCursor(QTextCursor.End)
    
    def pipelineStopped(self):
        self.pipelineRunning = False
        self.ui.btn_run_pipeline.setText("Run")
        if self.pipelineThread != None:            
            self.pipelineThread.terminate()
        self.pipelineWriteConsole("(end)")
    
    def removeOperationFromList(self):
        item = self.ui.list_operations.takeItem(self.ui.list_operations.currentRow())
        item = None
    
    def buildPipeline(self):
        p = Pipeline()
        for i in range(self.ui.list_operations.count()):
            p.addOperation(self.ui.list_operations.item(i).operation)
        return p
    
    def savePipeline(self):
        filepath = filePath = QFileDialog.getSaveFileName(None, 'New file', 
         self.ui.fileSystemModel.rootPath(), "Any (*.*)")[0]
        self.buildPipeline().save(filepath)
            
    def loadPipeline(self):
        filePath = QFileDialog.getOpenFileName(None, 'Open file', 
        self.ui.fileSystemModel.rootPath(), "Any (*.*)")[0]
        
        p = Pipeline()
        p.load(filePath, self.functions.functions)
        
        self.ui.list_operations.clear()
        for op in p.operations:
            self.ui.list_operations.addItem(ListWidgetOperation(op))

class ListWidgetOperation(QListWidgetItem):
    def __init__(self, operation: Operation):
        self.operation = operation        
        super().__init__(self.operation.name)        
        self.setFont(QFont("Arial", 11))
    
    def updateText(self):
        self.setText(f'{self.operation.name}')
    
    @property
    def name(self):
        return self.operation.name

class PipelineRunnerWorkerSignals(QObject):
    outputReceived = Signal(str)
    stopped = Signal()

class PipelineRunnerThread(QThread):
    def __init__(self, operationWidgetList: QListWidget):
        super(PipelineRunnerThread, self).__init__()
        self.operationWidgetList = operationWidgetList
        self.signals = PipelineRunnerWorkerSignals()

    @Slot()
    def run(self):
        self.setPriority(QThread.HighPriority)    
        operations = []
        for i in range(self.operationWidgetList.count()):
            operations.append(self.operationWidgetList.item(i).operation)
            
        self.signals.outputReceived.emit("[Starting pipeline]")
        
        import builtins
        
        _print = builtins.print
        builtins.print = lambda *args: [self.signals.outputReceived.emit(str(txt)) for txt in args]
        
        step = 1
        for op in operations:
            if not op.enabled:
                continue
            self.signals.outputReceived.emit(f'[{step}] -> {op.name}')
            op.run()
            step += 1           
        
        self.signals.outputReceived.emit("[Pipeline finished]")
        self.signals.stopped.emit()
        builtins.print = _print