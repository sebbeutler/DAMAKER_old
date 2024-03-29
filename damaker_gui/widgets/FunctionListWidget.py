# type: ignore

from inspect import getmembers, isfunction  
import re, typing
import traceback
from typing import Callable

from PySide2.QtWidgets import QWidget, QSplitter, QVBoxLayout, QSizePolicy, QMenu, QPushButton, QAction, QScrollArea
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal, QSize

import damaker
from damaker.pipeline import Operation
import damaker.processing
import damaker.stream

import damaker_gui
import damaker_gui.widgets as widgets

import rpy2.robjects as robjects

# TODO: test scroll for long parametters and connect it to the view
class FunctionListWidget(QSplitter, widgets.ITabWidget):
    name: str= "Operations"
    icon: str = u":/flat-icons/icons/flat-icons/services.svg"

    operationTriggered = Signal(object)
    apply = Signal(Operation)

    @property
    def toolbar(self) -> list[widgets.ActionButton]:
        return [widgets.ActionButton(self.reload, "Refresh Plugins", u":/flat-icons/icons/flat-icons/refresh.svg"),]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.menus = []

        # -Function list widget-
        self.functionList = QWidget()
        self.functionListLayout = QVBoxLayout()
        self.functionListLayout.setMargin(0)
        self.functionListLayout.setSpacing(0)
        self.setMinimumWidth(150)
        self.functionList.setLayout(self.functionListLayout)

        self.addWidget(self.functionList)

        self.functionEdit = QWidget()
        self.functionEditLayout = QVBoxLayout()
        self.functionEdit.setLayout(self.functionEditLayout)
        self.addWidget(self.functionEdit)

        self.setHandleWidth(4)
        self.categories: dict[str, list[function]] = {}
        self.functions: dict[str, function] = {}
        self.loadFunctions()

        self.operationTriggered.connect(self.editFunction)
        self.pipeline: widgets.PipelineWidget = None

    def editFunction(self, func: Callable):
        widgets.clearLayout(self.functionEditLayout, delete=True)
        self.functionEditLayout.addWidget(widgets.FunctionForm(Operation(func), self.onApply, self.addToPipeline))

    def onApply(self):
        op = self.getOperation()

        print(f"🟢 Running operation: {op.name}")
        try:
            op.run()
        except Exception as e:
            print(f"🛑 Operation runtime error")
            print(traceback.format_exc())

        # self.apply.emit(self.getOperation())
        for preview in damaker_gui.MainWindow.Instance.getTabsByType(widgets.PreviewFrame):
            preview.view.updateFrame()
        print("✅ Operation finished.")

    def addToPipeline(self):
        op = self.getOperation()
        if self.pipeline != None:
            self.pipeline.addOperation(op.copy())
            print("Added operation to pipeline ✔")

    def reload(self):
        widgets.clearLayout(self.functionListLayout)
        self.menus.clear()
        self.loadFunctions()
        print("Reloaded operations ✔")

    def convert_func_rpy2py(self, name, funcR):
        funcPy = FunctionListWidget._emptyFunc

    def loadFunctions(self):
        damaker.plugins = damaker.importPlugins()
        self.functions = dict(getmembers(damaker.processing, isfunction))        
        self.functions.update(dict(getmembers(damaker.stream, isfunction)))
        self.functions.update(dict(getmembers(damaker.plugins, isfunction)))

        # print(dict(getmembers(damaker.plugins, lambda obj: isinstance(obj, robjects.functions.Function))))

        self.categories = {"Plugins": []}

        for func in self.functions.values():
            if func.__name__[0] == '_':
                continue
            name = re.findall('Name:\s*(.*)\n', str(func.__doc__))
            if len(name) > 0:                
                func.alias = name[0]
            else:
                func.alias = func.__name__

            category = re.findall('Category:\s*(.*)\n', str(func.__doc__))
            if len(category) > 0:
                if not category[0] in self.categories.keys():
                    self.categories[category[0]] = []
                self.categories[category[0]].append(func)
            else:
                self.categories["Plugins"].append(func)

        for cat, funcs in self.categories.items():
            if len(funcs) == 0:
                continue
            menu = QMenu(cat)
            menu.setToolTipsVisible(True)
            # menu.setStyleSheet(_menuStyleSheet)
            for func in funcs:
                action: QAction = menu.addAction(func.alias)
                action.setToolTip(func.__doc__)
            menu.triggered.connect(lambda action: self.operationTriggered.emit(self.getFunction(action.text())))
            btn = QPushButton(cat)
            btn.setMinimumHeight(15)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
            # btn.setStyleSheet("color: white;")
            btn.setMenu(menu)
            btn.clicked.connect(btn.showMenu)
            self.functionListLayout.addWidget(btn)

            # retain widgets in memory
            self.menus.append([menu, btn])

        # self.functionListLayout.addStretch()

    def _emptyFunc():
        pass

    def getFunction(self, alias) -> Callable:
        for functions in self.categories.values():
            for func in functions:
                if func.alias == alias:
                    return func
        return FunctionListWidget._emptyFunc

    def getOperation(self) -> Operation:
        form: widgets.FunctionForm = self.functionEditLayout.itemAt(0).widget()
        widget: widgets.OperationWidget = form.operationWidget
        if issubclass(type(widget), widgets.OperationWidget):
            return widget.getOperation()
        print("No operation")
        return Operation(FunctionListWidget._emptyFunc)

    def connectPipeline(self, widget):
        if issubclass(type(widget), widgets.PipelineWidget) or issubclass(type(widget), widgets.PipelineViewer):
            self.pipeline = widget

    def disconnectPipeline(self, widget):
        if self.pipeline == widget:
            self.pipeline = None