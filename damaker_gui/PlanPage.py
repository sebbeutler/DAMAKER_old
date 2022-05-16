from multiprocessing import Pipe
from pathlib import Path
import builtins 
from unittest import addModuleCleanup
from webbrowser import Opera
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *
from matplotlib.pyplot import text

import numpy as np

from .widgets.PreviewWidget import PreviewWidget
from .widgets.FilePickerWidget import FilePickerWidget, FolderPickerWidget, getFilePath, getNewFilePath

from damaker.Channel import Channel, Channels
from inspect import getmembers, isfunction, signature        
import damaker.processing
import damaker.utils
from damaker.utils import StrFilePath, StrFolderPath
from damaker.pipeline import Operation, Pipeline

from .windows.UI_MainWindow import Ui_MainWindow

import time
import re
import json

def clearLayout(layout):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        widgetToRemove.setParent(None)

class PlanPage:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.preview = PreviewWidget(self.ui.mainPreview, self.ui.slide_mainPreview, [Channel("", np.zeros((100, 100, 100), np.uint8))], self.ui.fileInfo)
        self.pipelineThread = None
        
        self.functions = dict(getmembers(damaker.processing, isfunction))
        self.functions.update(dict(getmembers(damaker.utils, isfunction)))
        for fname in self.functions.keys():
            if fname[0] == '_':
                continue
            item = QListWidgetItem(fname)            
            item.setToolTip(re.sub(' {2,}', '', str(self.functions[fname].__doc__)))
            self.ui.list_functions.addItem(item)
        
        self.ui.list_functions.itemSelectionChanged.connect(self.functionListClicked)
        self.ui.list_operations.itemDoubleClicked.connect(self.operationListClicked)
        
        self.ui.btn_add_operation.clicked.connect(self.addOperation)
        self.ui.btn_modify_operation.clicked.connect(self.modifyOperation)
        
        self.ui.btn_add_operation.setHidden(True)
        self.ui.btn_modify_operation.setHidden(True)
        self.ui.edit_operation_name.setHidden(True)
        self.ui.checkbox_enabled.setHidden(True)
        
        self.selectedOperationItem = None
        
        self.ui.btn_run_pipeline.clicked.connect(self.runPipeline)
        self.ui.btn_remove_operation.clicked.connect(self.removeOperationFromList)
        self.ui.btn_save_pipeline.clicked.connect(self.savePipeline)
        self.ui.btn_load_pipeline.clicked.connect(self.loadPipeline)
        
        self.pipelineRunning = False
    
    def addOperation(self, event):
        func = self.getSelectedFunction()
        if func is None:
            return
        
        name = self.ui.edit_operation_name.text()
        enabled = self.ui.checkbox_enabled.isChecked()
        
        args = []        
        for i in range(self.ui.layout_fargs.count()):
            widget = self.ui.layout_fargs.itemAt(i).widget()
            
            if type(widget) is QSpinBox:
                args.append(widget.value())
            elif type(widget) is QComboBox:
                op = self.getOperationFromList(widget.currentText())
                args.append(op)
            elif type(widget) in [QLineEdit, FilePickerWidget, FolderPickerWidget]:
                args.append(widget.text())
            else:
                args.append(None)
        self.ui.list_operations.addItem(ListWidgetOperation(Operation(func, args, name, enabled)))
    
    def modifyOperation(self, event):
        if self.selectedOperationItem is None:
            return
        
        name = self.ui.edit_operation_name.text()
        enabled = self.ui.checkbox_enabled.isChecked()
        
        args = []        
        for i in range(self.ui.layout_fargs.count()):
            widget = self.ui.layout_fargs.itemAt(i).widget()
            
            if type(widget) is QSpinBox:
                args.append(widget.value())
            elif type(widget) is QComboBox:
                op = self.getOperationFromList(widget.currentText())
                args.append(op)
            elif type(widget) in [QLineEdit, FilePickerWidget, FolderPickerWidget]:
                args.append(widget.text())
            else:
                args.append(None)
        self.selectedOperationItem.operation.args = args
        self.selectedOperationItem.operation.name = name
        self.selectedOperationItem.operation.enabled = enabled
        self.selectedOperationItem.updateText()

    def getOperationFromList(self, name: str):
        for i in range(self.ui.list_operations.count()):
            item = self.ui.list_operations.item(i)
            if item.name == name:
                return item.operation
        return None
    
    def getSelectedFunction(self):
        function_items = self.ui.list_functions.selectedItems()
        if len(function_items) == 0:
            return None
        func_name = function_items[0].text()
        return self.functions[func_name]
    
    def functionListClicked(self, isOp=False):        
        clearLayout(self.ui.layout_fnames)
        clearLayout(self.ui.layout_fargs)
        self.ui.edit_operation_name.setHidden(False)
        self.ui.checkbox_enabled.setHidden(False)
        self.ui.btn_add_operation.setHidden(False)
        self.ui.btn_modify_operation.setHidden(True)
        
        func = self.getSelectedFunction()
        self.ui.edit_operation_name.setText(func.__name__)
        self.ui.checkbox_enabled.setChecked(True)
        
        sign = signature(func)
        for name in sign.parameters:
            param = sign.parameters[name]            
            label = QLabel(name)
            label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
            self.ui.layout_fnames.addWidget(label)
                
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setRange(-1000, 1000)
                self.ui.layout_fargs.addWidget(spinBox)
            elif param.annotation in [Channel, Channels]:
                self.ui.layout_fargs.addWidget(self.newOperationComboBox())
            elif param.annotation is StrFilePath:
                self.ui.layout_fargs.addWidget(FilePickerWidget())
            elif param.annotation is StrFolderPath:
                self.ui.layout_fargs.addWidget(FolderPickerWidget())
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.ui.layout_fargs.addWidget(textEdit)
            else:
                label = QLabel("Unknown type")
                label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.ui.layout_fargs.addWidget(label)
    
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
        
        arg_id=0
        sign = signature(operation.func)
        for name in sign.parameters:
            param = sign.parameters[name]  
            arg = operation.args[arg_id]
                      
            label = QLabel(name)
            label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
            self.ui.layout_fnames.addWidget(label)
                
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setValue(arg)
                spinBox.setRange(-1000, 1000)
                self.ui.layout_fargs.addWidget(spinBox)
            elif param.annotation in [Channel, Channels]:
                comboBox = self.newOperationComboBox()
                if type(arg) is Operation:
                    comboBox.setCurrentText(arg.name)
                else:
                    comboBox.setCurrentText("None")
                comboBox.removeItem(comboBox.findText(operation.name))
                self.ui.layout_fargs.addWidget(comboBox)            
            elif param.annotation is StrFilePath:
                filePicker = FilePickerWidget()
                filePicker.setText(arg)
                self.ui.layout_fargs.addWidget(filePicker)           
            elif param.annotation is StrFolderPath:
                folderPicker = FolderPickerWidget()
                folderPicker.setText(arg)
                self.ui.layout_fargs.addWidget(folderPicker)
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setText(arg)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.ui.layout_fargs.addWidget(textEdit)
            else:
                label = QLabel("Unknown type")
                label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.ui.layout_fargs.addWidget(label)
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
    
    _print = builtins.print
    def runPipeline(self):
        if self.pipelineRunning:
            self.pipelineStopped()
        
        self.ui.edit_pipeline_output.clear()
        builtins._print = PlanPage._print
        builtins.print = self.pipelineWriteConsole
        
        self.pipelineThread = PipelineRunnerThread(self.ui.list_operations)        
        self.pipelineThread.signals.outputReceived.connect(self.pipelineWriteConsole)
        self.pipelineThread.signals.stopped.connect(self.pipelineStopped)        
        self.pipelineThread.start()
        self.ui.btn_run_pipeline.setText("Stop")
        self.pipelineRunning = True
    
    def pipelineWriteConsole(self, *args):
        for arg in args:
            self.ui.edit_pipeline_output.append(' ' + str(arg))
        PlanPage._print(*args)
        self.ui.edit_pipeline_output.moveCursor(QTextCursor.End)
    
    def pipelineStopped(self):
        self.pipelineRunning = False
        builtins.print = PlanPage._print
        self.ui.btn_run_pipeline.setText("Run")
        # if self.pipelineThread != None:            
        #     self.pipelineThread.terminate()
    
    def removeOperationFromList(self):
        item = self.ui.list_operations.takeItem(self.ui.list_operations.currentRow())
        item = None
    
    def buildPipeline(self):
        p = Pipeline()
        for i in range(self.ui.list_operations.count()):
            p.addOperation(self.ui.list_operations.item(i).operation)
        return p
    
    def savePipeline(self):
        filepath = getNewFilePath()
        self.buildPipeline().save(filepath)
            
    def loadPipeline(self):
        filePath = getFilePath()
        p = Pipeline()
        p.load(filePath, self.functions)
        
        for op in p.operations:
            self.ui.list_operations.addItem(ListWidgetOperation(op))

class ListWidgetOperation(QListWidgetItem):
    def __init__(self, operation: Operation):
        self.operation = operation   
        
        super().__init__(self.getDisplayText())
        
        self.setFont(QFont("Arial", 11))
    
    def getDisplayText(self):
        display_text =  f'{self.operation.name} :     '
        sign = signature(self.operation.func)
        i = 0
        for param in sign.parameters:
            arg = str(self.operation.args[i])
            if len(arg) > 40:
                arg = ".." + arg[-20:]
            display_text += f'{param}={arg} '
            i += 1
        return display_text
    
    def updateText(self):
        self.setText(self.getDisplayText())
    
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
        self.signals.outputReceived.emit("[Building pipeline]")
    
        operations = []
        for i in range(self.operationWidgetList.count()):
            operations.append(self.operationWidgetList.item(i).operation)
        
        self.signals.outputReceived.emit(f'Operations count: {len(operations)}')
        self.signals.outputReceived.emit("[Starting pipeline]")
        
        step = 1
        for op in operations:
            if not op.enabled:
                continue
            self.signals.outputReceived.emit(f'[{step}] -> {op.name}')
            op.run()
            step += 1           
        
        self.signals.outputReceived.emit("[Pipeline finished]")
        self.signals.stopped.emit()