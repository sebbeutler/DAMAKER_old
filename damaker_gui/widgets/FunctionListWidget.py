from inspect import getmembers, isfunction  
import re
from typing import Callable

from PySide2.QtWidgets import QWidget, QSplitter, QVBoxLayout, QSizePolicy, QMenu, QPushButton, QAction, QScrollArea
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal, QSize

import damaker
from damaker.pipeline import Operation
import damaker.processing
import damaker.utils
import damaker_gui.widgets as widgets
from damaker_gui.widgets.OperationWidget import OperationWidget

_menuStyleSheet = """
QMenu {
    background-color: rgb(62,62,62);
    color: rgb(255,255,255);
    border: 1px solid #000;           
}
QMenu::item::selected {
    background-color: rgb(30,30,30);
}"""

class FunctionListWidget(QSplitter, widgets.ITabWidget):
    operationTriggered = Signal(object)
    apply = Signal(Operation)
    name: str= "Operations"
    icon: str = u":/flat-icons/icons/flat-icons/services.svg"
    
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
        
        self.functionEdit = QScrollArea()
        self.addWidget(self.functionEdit)
        
        self.setHandleWidth(4)
        self.categories: dict[str, list[function]] = {}
        self.functions: dict[str, function] = {}
        self.loadFunctions()    
        
        self.operationTriggered.connect(self.editFunction)    
        
        icon = QIcon()
        icon.addFile(u":/flat-icons/icons/flat-icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reloadPlugins = QPushButton(icon, "Refresh Plugins")
        self.btn_reloadPlugins.clicked.connect(self.reload)
        
        icon = QIcon()
        icon.addFile(u":/flat-icons/icons/flat-icons/internal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_apply = QPushButton(icon, "Apply")
        self.btn_apply.clicked.connect(self.onApply)
    
    def editFunction(self, fname: str):
        self.functionEdit.setWidget(OperationWidget(Operation(fname)))        
        
    def getToolbar(self):
        return [self.btn_reloadPlugins, self.btn_apply]
    
    def onApply(self):
        self.apply.emit(self.getOperation())
    
    def reload(self):
        widgets.clearLayout(self.functionListLayout)
        self.menus.clear()
        self.loadFunctions()
        print("Reloaded operations ✔")
    
    def loadFunctions(self):
        damaker.plugins = damaker.importPlugins()
        self.functions = dict(getmembers(damaker.processing, isfunction))        
        self.functions.update(dict(getmembers(damaker.utils, isfunction)))
        self.functions.update(dict(getmembers(damaker.plugins, isfunction)))
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
        widget: OperationWidget = self.functionEdit.widget()
        if issubclass(type(widget), OperationWidget):
            return widget.getOperation()
        return Operation(FunctionListWidget._emptyFunc)