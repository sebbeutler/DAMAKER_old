from email import utils
import inspect, enum
from math import comb
import numpy as np
import re
from inspect import getmembers, isfunction, signature   

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from vedo import Mesh

from damaker_gui.widgets.FunctionListWidget import FunctionsListWidget
from damaker_gui.widgets.FunctionParametersWidget import FunctionParametersWidget
from damaker_gui.widgets.OperationInputWidget import OperationInputWidget

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
        self.preview = PreviewWidget(slider=self.ui.previewPipelineSlider, fileInfo=self.ui.fileInfo)
        self.ui.plan_layout_preview.addWidget(self.preview)
        self.pipelineThread = None
    
        self.selectedOperationItem = None
        
        self.ui.list_operations.itemDoubleClicked.connect(self.operationListClicked)
        self.ui.btn_run_pipeline.clicked.connect(self.runPipeline)
        self.ui.btn_remove_operation.clicked.connect(self.removeOperationFromList)
        self.ui.btn_save_pipeline.clicked.connect(self.savePipeline)
        self.ui.btn_load_pipeline.clicked.connect(self.loadPipeline)
        
        self.pipelineRunning = False
        
        self.functions = FunctionsListWidget()
        self.functions.operationTriggered.connect(lambda name: self.functionMenuClicked(name))
        self.ui.functions_layout.addWidget(self.functions)
        
        self.functionParameters = FunctionParametersWidget()
        self.functionParameters.ui.btn_batchMode.clicked.connect(self.operationSwitchMode)
        self.ui.pipeline_settings_layout.addWidget(self.functionParameters)
        
        self.functionParameters.ui.btn_add_operation.clicked.connect(self.addOperation)
        self.functionParameters.ui.btn_modify_operation.clicked.connect(self.modifyOperation)        
    
    def functionMenuClicked(self, name):
        self.functionParameters.clearForm()
        self.functionParameters.setHiddenAll(False)
        self.functionParameters.ui.btn_modify_operation.setHidden(True)
        
        func = self.functions.getFunction(name)
        if func == None:
            return
        self.functionParameters.function = func
        self.functionParameters.ui.edit_operation_name.setText(name)
        self.functionParameters.ui.checkbox_enabled.setChecked(True)
        
        sign = signature(func)
        if sign.return_annotation in [Channel, Channels, NamedArray] and self.functionParameters.batchModeEnabled:
            self.functionParameters.outputDir.setHidden(False)
            self.functionParameters.outputDir.setText("")
        else:
            self.functionParameters.outputDir.setHidden(True)
        
        for argName in sign.parameters:
            param = sign.parameters[argName]
            if param.annotation == inspect._empty:
                continue
            
            default_arg = None
            if param.default != inspect._empty:
                default_arg = param.default
            
            formWidget = None
                
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if default_arg != None:
                    spinBox.setValue(int(default_arg))
                else:
                    spinBox.setValue(0)
                formWidget = spinBox
            if param.annotation is float:
                spinBox = QDoubleSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if default_arg != None:
                    spinBox.setValue(float(default_arg))
                else:
                    spinBox.setValue(0.0)
                formWidget = spinBox
            elif param.annotation in [Channel, Channels, BatchParameters, Mesh]:
                if self.functionParameters.batchModeEnabled or param.annotation is BatchParameters:
                    formWidget = BatchSelectionWidget(self.ui.fileSystemModel.rootPath())
                else:
                    formWidget = self.newOperationComboBox()
            elif param.annotation is SingleChannel:
                formWidget = FilePickerWidget(self.ui.fileSystemModel.rootPath())
            elif param.annotation is StrFilePath:
                formWidget = FilePickerWidget(self.ui.fileSystemModel.rootPath())
            elif param.annotation is StrFolderPath:
                formWidget = FolderPickerWidget(self.ui.fileSystemModel.rootPath())
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setFixedHeight(18)
                if default_arg != None:
                    textEdit.setText(default_arg)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                formWidget = textEdit
            elif type(param.annotation) is type(enum.Enum):
                formWidget = EnumComboBox(param.annotation)
            elif param.annotation is bool:
                checkBox = QCheckBox("")
                if default_arg != None:
                    checkBox.setChecked(default_arg)
                formWidget = checkBox
            if formWidget != None:
                self.functionParameters.ui.layout_settingsForm.addRow(argName+":", formWidget)
    
    def operationListClicked(self):
        self.functionParameters.clearForm()
        self.functionParameters.setHiddenAll(False)        
        self.functionParameters.ui.btn_add_operation.setHidden(True)
        
        operation_items = self.ui.list_operations.selectedItems()
        if len(operation_items) == 0:
            return None
        self.selectedOperationItem = operation_items[0]
        operation: Operation = operation_items[0].operation
        self.functionParameters.function = operation.func
        self.functionParameters.ui.edit_operation_name.setText(operation.name)   
        self.functionParameters.ui.checkbox_enabled.setChecked(operation.enabled)
        self.functionParameters.ui.btn_batchMode.setChecked(type(operation) is BatchOperation)
        
        sign = signature(operation.func)
        if type(operation) is BatchOperation and sign.return_annotation in [Channel, Channels, NamedArray]:
                self.functionParameters.outputDir.setHidden(False)
                self.functionParameters.outputDir.setText(operation.outputPath)
        else:
            self.functionParameters.outputDir.setHidden(True)
        
        arg_id=0
        for argName in sign.parameters:
            param = sign.parameters[argName]
            if arg_id >= len(operation.args):
                arg = param.default
            else:                
                arg = operation.args[arg_id]

            formWidget = None
            
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setFixedHeight(18)
                spinBox.setRange(-1000, 1000)
                spinBox.setValue(int(arg))
                formWidget = spinBox
            elif param.annotation is float:
                spinBox = QDoubleSpinBox()
                spinBox.setFixedHeight(18)
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(25)
                spinBox.setValue(float(arg))
                formWidget = spinBox
            elif param.annotation in [Channel, Channels, BatchParameters, Mesh]:
                if self.functionParameters.batchModeEnabled:
                    formWidget = BatchSelectionWidget(self.ui.fileSystemModel.rootPath(), arg)
                else:
                    comboBox = self.newOperationComboBox()
                    if type(arg) is Operation:
                        comboBox.setCurrentText(arg.name)
                    else:
                        comboBox.setCurrentText("None")
                    comboBox.removeItem(comboBox.findText(operation.name))
                    formWidget = comboBox
            elif param.annotation is SingleChannel:
                filePicker = FilePickerWidget(self.ui.fileSystemModel.rootPath())
                filePicker.setText(arg)   
                formWidget = filePicker   
            elif param.annotation is StrFilePath:
                filePicker = FilePickerWidget(self.ui.fileSystemModel.rootPath())
                filePicker.setText(arg)
                formWidget = filePicker         
            elif param.annotation is StrFolderPath:
                folderPicker = FolderPickerWidget(self.ui.fileSystemModel.rootPath())
                folderPicker.setText(arg)
                formWidget = folderPicker
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setFixedHeight(18)
                textEdit.setText(arg)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                formWidget = textEdit         
            elif type(param.annotation) is type(enum.Enum):
                combBox = EnumComboBox(param.annotation)
                combBox.setCurrentText(arg.name)
                formWidget = combBox
            elif param.annotation is bool:
                checkBox = QCheckBox("")
                checkBox.setChecked(arg)
                formWidget = checkBox
            
            if formWidget != None:
                self.functionParameters.ui.layout_settingsForm.addRow(argName+":", formWidget)
            arg_id += 1
    
    def addOperation(self, event):
        func = self.functionParameters.function
        if func is None:
            return
        
        name: str = self.functionParameters.ui.edit_operation_name.text()
        name_counter = 0
        for i in range(self.ui.list_operations.count()):
            item = self.ui.list_operations.item(i)
            if item.name.startswith(name):
                name_counter += 1
        if name_counter > 0:
            name += f'_{name_counter}'

        enabled = self.functionParameters.ui.checkbox_enabled.isChecked()
        outputPath = self.functionParameters.outputDir.text()
        
        args = []
        for i in range(self.functionParameters.ui.layout_settingsForm.rowCount()):
            widget = self.functionParameters.ui.layout_settingsForm.itemAt(i, QFormLayout.ItemRole.FieldRole).widget()
            
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
            elif type(widget) is OperationInputWidget:
                op = self.getOperationFromList(widget.currentText())
                args.append(op)
            elif type(widget) in [QLineEdit, FilePickerWidget, FolderPickerWidget]:
                args.append(widget.text())
            elif type(widget) is QCheckBox:
                args.append(widget.isChecked())
            else:
                args.append(None)
                
        if self.functionParameters.batchModeEnabled:
            listwidget = ListWidgetOperation(BatchOperation(func, args, name, enabled, outputPath))
        else:
            listwidget = ListWidgetOperation(Operation(func, args, name, enabled))
            
        self.ui.list_operations.addItem(listwidget)
        self.ui.list_operations.setCurrentItem(listwidget)
        self.operationListClicked()
    
    def modifyOperation(self, event):
        if self.selectedOperationItem is None:
            return
        
        name = self.functionParameters.ui.edit_operation_name.text()
        enabled = self.functionParameters.ui.checkbox_enabled.isChecked()
        outputPath = self.functionParameters.outputDir.text()
        
        args = []
        for i in range(self.functionParameters.ui.layout_settingsForm.rowCount()):
            widget = self.functionParameters.ui.layout_settingsForm.itemAt(i, QFormLayout.ItemRole.FieldRole).widget()
            
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
            elif type(widget) is OperationInputWidget:
                op = self.getOperationFromList(widget.currentText())
                args.append(op) 
            elif type(widget) in [QLineEdit, FilePickerWidget, FolderPickerWidget]:
                args.append(widget.text())
            elif type(widget) is QCheckBox:
                args.append(widget.isChecked())
            else:
                args.append(None)
        
        if self.functionParameters.batchModeEnabled and type(self.selectedOperationItem.operation) != BatchOperation:
            self.selectedOperationItem.operation = BatchOperation(self.selectedOperationItem.operation.func, args, name, enabled, outputPath)
        elif not self.functionParameters.batchModeEnabled and type(self.selectedOperationItem.operation) == BatchOperation:
            self.selectedOperationItem.operation = Operation(self.selectedOperationItem.operation.func, args, name, enabled)
        else:            
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
    
    #TODO: see if using operation as item data is useful
    def newOperationComboBox(self):
        operations = []
        for i in range(self.ui.list_operations.count()):
            item = self.ui.list_operations.item(i)
            if type(item.operation) != BatchOperation:
                operations.append(item.name)
        return OperationInputWidget(operations)
    
    def operationSwitchMode(self):
        for i in range(self.functionParameters.ui.layout_settingsForm.rowCount()):
            label = self.functionParameters.ui.layout_settingsForm.itemAt(i, QFormLayout.ItemRole.LabelRole).widget().text()
            widget = self.functionParameters.ui.layout_settingsForm.itemAt(i, QFormLayout.ItemRole.FieldRole).widget()
            if type(widget) == OperationInputWidget:
                self.functionParameters.ui.layout_settingsForm.removeRow(i)
                self.functionParameters.ui.layout_settingsForm.insertRow(i, label, BatchSelectionWidget(self.ui.fileSystemModel.rootPath()))
                if signature(self.functionParameters.function).return_annotation in [Channel, Channels, NamedArray]:
                    self.functionParameters.outputDir.setHidden(False)
                else:
                    self.functionParameters.outputDir.setHidden(True)
            elif type(widget) == BatchSelectionWidget:                
                self.functionParameters.ui.layout_settingsForm.removeRow(i)
                self.functionParameters.ui.layout_settingsForm.insertRow(i, label, self.newOperationComboBox())
                self.functionParameters.outputDir.setHidden(True)
            
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
        # self.pipelineThread.run()
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
         self.ui.fileSystemModel.rootPath(), "Any (*.json)")[0]
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