import enum
from PySide2.QtWidgets import QFrame, QFormLayout, QGroupBox, QListWidget, QGridLayout, QLineEdit, QSizePolicy, QWidget, QLabel, QSpinBox, QDoubleSpinBox, QCheckBox
from PySide2.QtCore import *

import damaker_gui
import damaker_gui.widgets as widgets
from damaker.pipeline import *

import inspect

class OperationWidget(QFrame):
    def __init__(self, parent=None, op:Operation=None, pipeline: QListWidget=None, batchMode=False, layoutType=QFormLayout):
        super().__init__(parent)
        print("OPE")
        self.op = op
        self.pipeline = pipeline
        
        self._layout: QFormLayout = layoutType()
        self._layout.setMargin(20)
        self._layout.setSpacing(15)
        self.setLayout(self._layout)
        
        self.setAcceptDrops(False)
        
        # self.funcAlias = QLineEdit()
        # self.funcAlias.setStyleSheet("border-radius: 3px; border: 1px solid rgb(220, 220, 220);")
        # self.funcAlias.setPlaceholderText("Alias")
        # self.funcAlias.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferre
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.parameters = {}
        self.setFixedHeight(len(self.parameters) / 3 + 1 * 200)
        self.setAcceptDrops(False)
    
    
    def updateOperation(self):
        args = []
        for widget in self.parameters.values():
            if hasattr(widget, 'getParameter'):
                args.append(widget.getParameter(widget))
        self.op.args = args
    
    def run(self):
        self.updateOperation()
        self.op.run()
        
    def getOperation(self) -> Operation:        
        self.updateOperation()
        return self.op.copy()
    
    def addEntry(self, name: str, widget: QWidget):
        widgets = len(self.parameters)
        col = (widgets*2) % 6
        row = int(widgets / 3)
        if issubclass(type(self._layout), QGridLayout):
            self._layout.addWidget(QLabel(f"{name}:"), row, col, Qt.AlignmentFlag.AlignRight)
            self._layout.addWidget(widget, row, col+1, Qt.AlignmentFlag.AlignLeft)
        else:
            self._layout.addRow(f"{name}:", widget)
        widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
    
    def initialize(self):
        widgets.clearLayout(self._layout, False)
        
        sign = signature(self.op.func)
        param = None
        formWidget = None
        
        args = list(sign.parameters.keys())
        for i in range(len(args)):
            argName = args[i]
            opArg = None
            if len(self.op.args) > i:
                opArg = self.op.args[i]
            
            param = sign.parameters[argName]
            if param.annotation == inspect._empty:
                continue
            
            # INT
            if param.annotation is int:
                spinBox = QSpinBox()
                spinBox.setRange(-1000, 1000)
                spinBox.setFixedHeight(18)
                if opArg != None:
                    spinBox.setValue(opArg)
                elif param.default != inspect._empty:
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
                
                if opArg != None:
                    spinBox.setValue(opArg)
                elif param.default != inspect._empty:
                    spinBox.setValue(float(param.default))
                else:
                    spinBox.setValue(0.0)                
                spinBox.getParameter = lambda sb: sb.value()
                formWidget = spinBox
            
            # CHANNEL
            if param.annotation in [widgets.Channel, widgets.Channels, widgets.BatchParameters, Mesh]:
                if param.annotation is widgets.BatchParameters:
                    if opArg != None:
                        formWidget = widgets.BatchSelectionWidget(opArg)
                    else:
                        formWidget = widgets.BatchSelectionWidget()
                    formWidget.getParameter = lambda widget: widget.getBatch()
                else:
                    formWidget = widgets.ChannelSelectorWidget()
                    formWidget.getParameter = lambda widget: widget.getChannels()
            elif param.annotation is widgets.SingleChannel or param.annotation is StrFilePath:
                if opArg != None:
                    formWidget = widgets.FilePickerWidget(text=opArg)
                else:
                    formWidget = widgets.FilePickerWidget(widgets.WorkspaceWidget.RootPath)
            elif param.annotation is StrFolderPath:
                if opArg != None:
                    formWidget = widgets.FolderPickerWidget(text=opArg)
                else:
                    formWidget = widgets.FolderPickerWidget(widgets.WorkspaceWidget.RootPath)
                formWidget.getParameter = lambda widget: widget.text()
            
            # TEXT
            elif param.annotation is str:
                textEdit = QLineEdit()
                textEdit.setFixedHeight(18)
                if opArg != None:
                    textEdit.setText(opArg)
                elif param.default != inspect._empty:
                    textEdit.setText(param.default)
                textEdit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                formWidget = textEdit
                formWidget.getParameter = lambda widget: widget.text()
            
            # CHOICES
            elif type(param.annotation) is type(enum.Enum):
                if opArg != None:
                    formWidget = widgets.EnumComboBox(param.annotation, text=str(opArg))
                elif param.default != inspect._empty:
                    formWidget = widgets.EnumComboBox(param.annotation)
                formWidget.getParameter = lambda widget: widget.getEnumChoice()
            
            # BOOLEAN
            elif param.annotation is bool:
                checkBox = QCheckBox("")
                if opArg != None:
                    checkBox.setChecked(opArg)
                elif param.default != inspect._empty:
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

from damaker_gui.windows.UI_FunctionForm import Ui_FunctionForm

class FunctionForm(QGroupBox):
    def __init__(self, op:Operation, pipeline: QListWidget=None, batchMode=False, layoutType=QFormLayout):
        super().__init__(op.func.alias)
        
        self.ui = Ui_FunctionForm()
        self.ui.setupUi(self)
