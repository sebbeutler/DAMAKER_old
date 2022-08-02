from PySide2.QtWidgets import QFrame, QHBoxLayout, QWidget, QSizePolicy, QLayout, QTabWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize

from damaker_gui.widgets.ITabWidget import ITabWidget

class ToolBar(QFrame):
    def __init__(self, parent=None):        
        super().__init__(parent)
        self._layout = QHBoxLayout()
        self._layout.setSpacing(0)
        self._layout.setMargin(0)
        self.setMinimumHeight(22)
        self.setLayout(self._layout)
    
    def newAction(self, widget: QWidget):
        widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        widget.setFixedHeight(22)
        self._layout.insertWidget(0, widget)
    
    def newActions(self, widgets: list[QWidget]):
        for widget in widgets:
            self.newAction(widget)
    
    def clearActions(self):
        for i in reversed(range(self._layout.count())): 
            widgetToRemove = self._layout.itemAt(i).widget()
            self._layout.removeWidget(widgetToRemove)
            if widgetToRemove != None:
                widgetToRemove.setParent(None)        
        self._layout.addStretch()

class ContentFrame(QFrame):
    def __init__(self, parent=None):
        if issubclass(type(parent), QLayout):
            super().__init__()
            parent.addWidget(self)
        else:
            super().__init__(parent)
        self._tab: QTabWidget = None        
        self.toolBar = ToolBar()
        
    @property
    def tab(self) -> QTabWidget:
        if self._tab is None:
            self.setStyleSheet("QFrame#" + self.objectName() + "{ background-color: rgb(172, 187, 205); border-radius: 3px; border: 1px solid rgb(205, 205, 205); }")
            self._tab: QTabWidget = self.findChild(QTabWidget)
            self._tab.setMovable(True)
            self._tab.tabCloseRequested.connect(self.tabClose)
            self._tab.currentChanged.connect(self.tabChanged)
            self.layout().insertWidget(0, self.toolBar)
        return self._tab
    
    def tabChanged(self, index: int):
        widget = self.tab.widget(index)
        self.toolBar.clearActions()
        if issubclass(type(widget), ITabWidget):
            self.toolBar.newActions(widget.getToolbar())
    
    def addTab(self, widget: QWidget, name: str="None"):
        if issubclass(type(widget), ITabWidget):
            name = widget.name
            icon = QIcon()
            icon.addFile(widget.icon, QSize(), QIcon.Normal, QIcon.Off)
            self.tab.addTab(widget, icon, name)
        else:
            self.tab.addTab(widget, name)
        self.tab.setCurrentIndex(self.tab.count()-1)
    
    def tabClose(self, index):
        import gc
        widget = self._tab.widget(index)
        if issubclass(widget, ITabWidget):
            widget.closing()
        widget.deleteLater()
        self._tab.removeTab(index)
        gc.collect()
        
        