from inspect import getmembers, isfunction, signature  
import re

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *
from yaml import load

import damaker.processing
import damaker.utils

_menuStyleSheet = """
QMenu {
    background-color: rgb(62,62,62);
    color: rgb(255,255,255);
    border: 1px solid #000;           
}
QMenu::item::selected {
    background-color: rgb(30,30,30);
}"""

class FunctionsListWidget(QWidget):
    operationTriggered = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.menus = []
        self._layout = QVBoxLayout()
        self._layout.setMargin(0)
        self._layout.setSpacing(0)
        self.setMinimumWidth(150)
        self.setLayout(self._layout)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        
        self.categories = {}
        self.functions = {}
        self.loadFunctions()
        
    
    def loadFunctions(self):
        self.functions = dict(getmembers(damaker.processing, isfunction))        
        self.functions.update(dict(getmembers(damaker.utils, isfunction)))
        self.categories = {"Other": []}
        
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
                self.categories["Other"].append(func)
        
        for cat, funcs in self.categories.items():
            if len(funcs) == 0:
                continue
            menu = QMenu(cat)
            menu.setToolTipsVisible(True)
            menu.setStyleSheet(_menuStyleSheet)
            for func in funcs:
                action: QAction = menu.addAction(func.alias)
                # action.setToolTip(func.__doc__)
            menu.triggered.connect(lambda action: self.operationTriggered.emit(action.text()))
            btn = QPushButton(cat)
            btn.setMinimumHeight(15)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
            btn.setStyleSheet("color: white;")
            btn.setMenu(menu)
            btn.clicked.connect(btn.showMenu)
            self._layout.addWidget(btn)
            
            # retain widgets in memory
            self.menus.append([menu, btn])
            
        # self._layout.addStretch()
    
    def getFunction(self, alias):
        for functions in self.categories.values():
            for func in functions:
                if func.alias == alias:
                    return func
        return None
                     
        
        