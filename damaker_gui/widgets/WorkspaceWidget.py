from PySide2.QtWidgets import QTreeView, QFileSystemModel, QAbstractItemView, QPushButton, QFileDialog, QWidget, QSizePolicy
from PySide2.QtCore import Signal

import os, shutil

from damaker_gui.widgets.ITabWidget import ActionButton, ITabWidget

class WorkspaceWidget(QTreeView, ITabWidget):
    name: str = "Workspace"
    icon: str = u":/flat-icons/icons/flat-icons/globe.svg"

    @property
    def toolbar(self) -> list[ActionButton]:
        return [ActionButton(self.selectWorkspace, "Select Workspace"),
                ActionButton(self.open, "Open"),
                ActionButton(self.copy, "Copy"),
                ActionButton(self.paste, "Paste"),
                ActionButton(self.delete, "Delete")]

    signalOpen = Signal(str)
    RootPath = os.getcwd()
    def __init__(self, parent=None, path="/", signalOpen=None):
        super().__init__(parent)

        if signalOpen != None:
            self.signalOpen.connect(signalOpen)

        self.explorer = QFileSystemModel(self)
        self.explorer.setReadOnly(False)        
        root = self.explorer.setRootPath(WorkspaceWidget.RootPath)

        self.setModel(self.explorer)
        self.setRootIndex(root)

        # self.setColumnHidden(1, True)
        # self.setColumnHidden(2, True)
        # self.setColumnHidden(3, True)

        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setIndentation(15)
        self.setDragEnabled(True)
        self.setWordWrap(True)
        self.setHeaderHidden(False)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.file_buffer = ""

    def copy(self) -> bool:
        target = self.explorer.filePath(self.currentIndex())
        if os.path.isfile(target):
            self.file_buffer = self.explorer.filePath(self.currentIndex())
            print(f"Copied '{self.file_buffer}' ✔")
            self.update()
            return True
        return False

    def paste(self):
        target = self.explorer.filePath(self.currentIndex())
        if not os.path.isdir(target):
            target = os.path.dirname(target)

        shutil.copy2(self.file_buffer, target)
        print(f"Pasted '{self.file_buffer}' ✔")
        self.update()

    def delete(self) -> bool:
        target = self.explorer.filePath(self.currentIndex())
        if os.path.isfile(target):
            os.remove(target)
            print(f"Removed '{target}' ✔")
            self.update()
            return True
        return False

    def selectWorkspace(self):
        path = QFileDialog.getExistingDirectory(None, 'Open folder', self.explorer.rootPath())
        if path == "":
            return
        root = self.explorer.setRootPath(path)
        WorkspaceWidget.RootPath = path        
        print("Workspace🌐:", WorkspaceWidget.RootPath)
        self.setRootIndex(root)

    def open(self):
        self.signalOpen.emit(self.explorer.filePath(self.currentIndex()))
