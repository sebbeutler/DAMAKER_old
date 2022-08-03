from inspect import getmembers, isfunction  
import re

from PySide2.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QMenu, QPushButton, QAction
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal, QSize

import damaker
import damaker.processing
import damaker.utils
import damaker_gui.widgets as widgets

_menuStyleSheet = """
QMenu {
    background-color: rgb(62,62,62);
    color: rgb(255,255,255);
    border: 1px solid #000;           
}
QMenu::item::selected {
    background-color: rgb(30,30,30);
}"""

class FunctionListWidget(QWidget, widgets.ITabWidget):
    operationTriggered = Signal(str)
    name: str= "Operations"
    # icon: str = u":/flat-icons/icons/flat-icons/engineering.svg"
    icon: str = u":/flat-icons/icons/flat-icons/services.svg"
    
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
        
        
        icon = QIcon()
        icon.addFile(u":/flat-icons/icons/flat-icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reloadPlugins = QPushButton(icon, "Refresh Plugins")
        self.btn_reloadPlugins.clicked.connect(self.reload)
        
    def getToolbar(self):
        return [self.btn_reloadPlugins]
    
    def reload(self):
        widgets.clearLayout(self._layout)
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
                # action.setToolTip(func.__doc__)
            menu.triggered.connect(lambda action: self.operationTriggered.emit(action.text()))
            btn = QPushButton(cat)
            btn.setMinimumHeight(15)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
            # btn.setStyleSheet("color: white;")
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
                     
        
        