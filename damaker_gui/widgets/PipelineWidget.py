from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from damaker.pipeline import *
import damaker_gui.widgets as widgets

import inspect
from damaker_gui.widgets.FunctionListWidget import FunctionListWidget
from damaker_gui.widgets.WorkspaceWidget import WorkspaceWidget

class PipelineWidget(QListWidget):
    name: str = "Pipeline"
    icon: str = u":/flat-icons/icons/flat-icons/timeline.svg"
    def __init__(self, parent=None, operations=[]):
        super().__init__(parent)
        
        self.setSpacing(3)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)
        
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        act = QAction("Remove", self)
        act.triggered.connect(self.removeOperation)
        self.addAction(act)
        
        for op in operations:
            self.addOperation(op)
            
        self.pipelineThread = PipelineRunnerThread()
            
        self.btn_run = QPushButton("Run")
        self.btn_run.clicked.connect(self.runPipeline)  
        
        self.btn_stop = QPushButton("Stop")
        self.btn_stop.setEnabled(False)
        self.btn_stop.clicked.connect(self.stopPipeline)      
    
    def getToolbar(self):
        return [self.btn_stop, self.btn_run]
    
    def runPipeline(self):                
        self.pipelineThread.setPipeline(self)        
        self.pipelineThread.stopped.connect(self.stopPipeline)        
        self.pipelineThread.start()
        # self.pipelineThread.run()
        self.btn_run.setEnabled(False)
        self.btn_stop.setEnabled(True)
    
    def stopPipeline(self):
        self.pipelineThread.terminate()
        print("(Pipeline ended 🟡)")
        self.btn_run.setEnabled(True)
        self.btn_stop.setEnabled(False)
    
    def addOperation(self, op: Operation):
        print(f"Operation '{op.name}' added ✔")
        item = QListWidgetItem("")
        # item = QListWidgetItem(op.name)       
        self.addItem(item)
        op_widget = OperationItemWidget(op, self) 
        item.setSizeHint(QSize(op_widget.width(), op_widget.height()))        
        self.setItemWidget(item, op_widget)
    
    def removeOperation(self):
        self.takeItem(self.currentRow())
    
    def connectTo(self, widget: FunctionListWidget):
        widget.operationTriggered.connect(lambda name: self.addOperation(Operation(widget.getFunction(name), [], name)))

class PipelineRunnerThread(QThread):
    stopped = Signal()
    def __init__(self, pipeline: PipelineWidget=None):
        super(PipelineRunnerThread, self).__init__()
        self.pipeline = pipeline

    def setPipeline(self, pipeline: PipelineWidget):
        self.pipeline = pipeline
    
    @Slot()
    def run(self):
        if self.pipeline is None:
            pass
        self.setPriority(QThread.HighPriority)    
        operations: list[OperationItemWidget] = []
        for i in range(self.pipeline.count()):
            operations.append(self.pipeline.itemWidget(self.pipeline.item(i)))
            
        print("[Starting Pipeline 🚀]")
        
        for item in operations:            
            if not item.op.enabled:
                item.setStyleSheet("background-color: rgb(130, 130, 130);")                
            else:     
                item.setStyleSheet("background-color: rgb(230, 230, 230);")
        
        step = 1
        for item in operations:
            if not item.op.enabled:
                continue
            print(f'-- [{step}] ➡ {item.op.name} --')
            item.setStyleSheet("background-color: rgb(244, 255, 189);")
            item.run()
            item.setStyleSheet("background-color: rgb(206, 255, 218);")
            step += 1
        
        print("[Pipeline finished 🟢]")
        self.stopped.emit()

class OperationItemWidget(QGroupBox):
    def __init__(self, op:Operation, pipeline: QListWidget=None):
        super().__init__(op.func.alias)
        self.op = op
        self.pipeline = pipeline
        
        self._layout: QGridLayout = QGridLayout()
        self._layout.setMargin(5)
        self.setLayout(self._layout)
        
        self.setAcceptDrops(False)
        
        self.setStyleSheet("QGroupBox { border-radius: 3px; border: 1px solid rgb(72, 72, 72); }")
        
        self.funcAlias = QLineEdit()
        self.funcAlias.setStyleSheet("border-radius: 3px; border: 1px solid rgb(220, 220, 220);")
        self.funcAlias.setPlaceholderText("Alias")
        self.funcAlias.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.parameters = {}
        self.initialize()
        self.setFixedHeight(len(self.parameters) / 3 + 1 * 200)
        self.setAcceptDrops(False)
    
    def run(self):
        args = []
        for widget in self.parameters.values():
            if hasattr(widget, 'getParameter'):
                args.append(widget.getParameter(widget))
        self.op.args = args
        self.op.run()
    
    def addEntry(self, name: str, widget: QWidget):
        widgets = len(self.parameters)
        col = (widgets*2) % 6 + 1
        row = int(widgets / 3)
        self._layout.addWidget(QLabel(f"{name}:"), row, col, Qt.AlignmentFlag.AlignRight)
        self._layout.addWidget(widget, row, col+1, Qt.AlignmentFlag.AlignLeft)
        widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
    
    def initialize(self):
        widgets.clearLayout(self._layout, False)
        
        self._layout.addWidget(self.funcAlias, 0, 0, Qt.AlignmentFlag.AlignCenter)
        
        sign = signature(self.op.func)
        param = None
        formWidget = None
        
        for argName in sign.parameters:
            param = sign.parameters[argName]
            if param.annotation == inspect._empty:
                continue
            
            # INT
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if param.default != inspect._empty:
                    spinBox.setValue(int(param.default))
                else:
                    spinBox.setValue(0)
                spinBox.getParameter = lambda sb: sb.value()
                formWidget = spinBox

            # FLOAT
            if param.annotation is float:
                spinBox = QDoubleSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if param.default != inspect._empty:
                    spinBox.setValue(float(param.default))
                else:
                    spinBox.setValue(0.0)                
                spinBox.getParameter = lambda sb: sb.value()
                formWidget = spinBox
            
            # CHANNEL
            if param.annotation in [widgets.Channel, widgets.Channels, widgets.BatchParameters, Mesh]:
                if param.annotation is widgets.BatchParameters or 1:
                    formWidget = widgets.BatchSelectionWidget()
                    formWidget.getParameter = lambda widget: widget.getBatch()
                else:
                    formWidget = self.newOperationComboBox()
            elif param.annotation is widgets.SingleChannel:
                formWidget = widgets.FilePickerWidget(WorkspaceWidget.RootPath)
                formWidget.getParameter = lambda widget: widget.text()
            elif param.annotation is StrFilePath:
                formWidget = widgets.FilePickerWidget(WorkspaceWidget.RootPath)
                formWidget.getParameter = lambda widget: widget.text()
            elif param.annotation is StrFolderPath:
                formWidget = widgets.FolderPickerWidget(WorkspaceWidget.RootPath)
                formWidget.getParameter = lambda widget: widget.text()
            
            # TEXT
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setFixedHeight(18)
                if param.default != inspect._empty:
                    textEdit.setText(param.default)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                formWidget = textEdit
                formWidget.getParameter = lambda widget: widget.text()
            
            # CHOICES
            elif type(param.annotation) is type(enum.Enum):
                formWidget = widgets.EnumComboBox(param.annotation)
                formWidget.getParameter = lambda widget: widget.curerentText()
            
            # BOOLEAN
            elif param.annotation is bool:
                checkBox = QCheckBox("")
                if param.default != inspect._empty:
                    checkBox.setChecked(param.default)
                formWidget = checkBox
                formWidget.getParameter = lambda widget: widget.isChecked()
                
            if formWidget != None:
                self.addEntry(argName, formWidget)
                self.parameters[argName] = formWidget
    
    def newOperationComboBox(self):
        operations = []
        for i in range(self.pipeline.count()):
            widget = self.pipeline.itemWidget(self.pipeline.item(i))
            # if type(item.operation) != widgets.BatchOperation:
            #     operations.append(item.name)
            # print(widget)
        return widgets.OperationInputWidget(operations)              