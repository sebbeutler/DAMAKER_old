import gc
from typing import Callable

from PySide6.QtWidgets import QFrame, QTabWidget, QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy, QLayout, QTabWidget
from PySide6.QtGui import QIcon, QMouseEvent, Qt, QPixmap, QDrag, QCursor, QRegion
from PySide6.QtCore import QSize, QMimeData, QPoint, Signal

import damaker_gui.widgets as widgets
from damaker_gui.widgets.ITabWidget import ITabWidget

class ContentFrame(QFrame):
    def __init__(self, widget: ITabWidget, parent=None):        
        super().__init__(parent)
        self.widget: ITabWidget = widget

        self._layout = QVBoxLayout()
        self._layout.setSpacing(0)
        self._layout.setMargin(0)
        self.setLayout(self._layout)

        self.toolbar = QFrame()
        self.toolbar_layout = QHBoxLayout()
        self.toolbar_layout.setSpacing(0)
        self.toolbar_layout.setMargin(0)
        self.toolbar.setFixedHeight(22)
        self.toolbar.setLayout(self.toolbar_layout)

        self._layout.addWidget(self.toolbar)
        self._layout.addWidget(self.widget)

        if self.widget is None or not issubclass(type(self.widget), ITabWidget):
            return
        self.refreshActions()

    def refreshActions(self):
        self.clearActions()
        for action in self.widget.toolbar:
            self.toolbar_layout.addWidget(action)
        self.toolbar_layout.addStretch()

    def clearActions(self):
        for i in reversed(range(self.toolbar_layout.count())): 
            widgetToRemove = self.toolbar_layout.itemAt(i).widget()
            self.toolbar_layout.removeWidget(widgetToRemove)
            if widgetToRemove != None:
                widgetToRemove.setParent(None)

class ContentDock(QTabWidget):
    tabChangedSignal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMovable(True)
        self.setAcceptDrops(True)
        self._tabBar = self.tabBar()
        self._tabBar.setMouseTracking(True)
        self.dragIndex = None

        # self.toolBar = ToolBar()
        # self._tab.tabCloseRequested.connect(self.closeTab)
        # self._tab.currentChanged.connect(self.tabChanged)
        self.currentChanged.connect(self.tabChanged)

    def tabChanged(self, index: int):
        # WARNING: Following breaks when the widget is not instance of ITabWidget
        widget = self.getWidgetByIndex(index)
        if issubclass(type(widget), ITabWidget):
            widget.tabEnterFocus()

    def addTab(self, widget: ITabWidget, title: str="Untitled", icon: QIcon=None, focus: bool=False):
        if issubclass(type(widget), ITabWidget):
            icon = QIcon()
            icon.addFile(widget.icon, QSize(), QIcon.Normal, QIcon.Off)            
            super().addTab(ContentFrame(widget), icon, widget.name)
            widget.changeTitle.connect(lambda title: self.setTitle(widget, title))
            widget.focus.connect(self.focusTab)
        else:
            if icon is None:
                super().addTab(widget, title)
            else:
                super().addTab(widget, icon, title)
        if focus:
            self.setCurrentIndex(self.count()-1)
        self.tabChangedSignal.emit()

    def focusTab(self, widget: ITabWidget):
        index = self.getWidgetIndex(widget)
        if self.currentIndex() == index:
            self.currentChanged.emit(index)
        else:
            self.setCurrentIndex(self.getWidgetIndex(widget))

    def setTitle(self, widget: QWidget, title: str):
        if issubclass(type(widget), ITabWidget):
            widget.name = title
        index = self.getWidgetIndex(widget)
        if index != -1:
            self.setTabText(index, title)        

    def closeTab(self, index) -> bool:
        if index < 0 or index >= self.tab.count():
            return False
        widget = self.widget(index)
        if issubclass(type(widget.widget), ITabWidget):
            widget.widget.closing()
            widget.widget.deleteLater()
        widget.deleteLater()
        self.removeTab(index)
        gc.collect()
        return True

    def removeTab(self, widget: QWidget):
        index = self.getWidgetIndex(widget)
        if index != -1:
            self.tab.removeTab(index)
            self.tabChangedSignal.emit()

    def getWidgetIndex(self, widget: QWidget) -> int:
        for i in range(self.count()):
            if widget == self.widget(i).widget:
                return i
        return -1 # Not found

    def getWidgetByIndex(self, index) -> QWidget:
        return self.widget(index).widget

    def getTabByName(self, name: str) -> QWidget:
        for i in range(self.count()):
            if self.tabText(i) == name:
                return self.widget(i).widget
        return None

    def getTabsByType(self, _type: type) -> list[QWidget]:
        _widgets = []
        for i in range(self.count()):
            widget = self.widget(i).widget
            if issubclass(type(widget), _type):
                _widgets.append(widget)
        return _widgets

    def connectCurrentChanged(self, func: Callable):
        self.currentChanged.connect(lambda x: func(self.getWidgetByIndex(x)))

    # -Drag & Drop tabs- #
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return

        globalPos = self.mapToGlobal(e.pos())
        posInTab = self._tabBar.mapFromGlobal(globalPos)
        self.dragIndex = self._tabBar.tabAt(e.pos())
        tabRect = self._tabBar.tabRect(self.dragIndex)

        pixmap = QPixmap(tabRect.size())
        self._tabBar.render(pixmap,QPoint(),QRegion(tabRect))
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        cursor = QCursor(Qt.OpenHandCursor)
        drag.setHotSpot(e.pos() - posInTab)
        drag.setDragCursor(cursor.pixmap(),Qt.MoveAction)
        dropAction = drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, e):
        e.accept()
        if e.source() != self:
            return

    def dragLeaveEvent(self,e):
        e.accept()

    def dropEvent(self, e):
        sourceTab: ContentDock = e.source()
        if sourceTab == self or not issubclass(type(sourceTab), ContentDock):
            return

        e.setDropAction(Qt.MoveAction)
        e.accept()

        widget = sourceTab.widget(sourceTab.dragIndex)
        title = sourceTab.tabText(sourceTab.dragIndex)
        icon = QIcon()

        #!Warning: Catch unhandled no attr exception 
        icon.addFile(widget.widget.icon, QSize(), QIcon.Normal, QIcon.Off)

        self.addTab(widget=widget, title=title, icon=icon, focus=True)
