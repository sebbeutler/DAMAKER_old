from PySide2.QtWidgets import QTreeView, QFileSystemModel, QAbstractItemView, QPushButton, QFileDialog, QWidget
from PySide2.QtCore import Signal

import os, shutil

class WorkspaceWidget(QTreeView):
    name: str = "Workspace"
    icon: str = u":/flat-icons/icons/flat-icons/globe.svg"
    
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
        
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setIndentation(15)
        self.setWordWrap(True)
        self.setHeaderHidden(False)
        
        self.file_buffer = ""
        
        self.btn_copy = QPushButton("Copy")
        self.btn_copy.clicked.connect(self.copy)
        
        self.btn_paste = QPushButton("Paste")
        self.btn_paste.clicked.connect(self.paste)
        
        self.btn_delete = QPushButton("Delete")
        self.btn_delete.clicked.connect(self.delete)
        
        self.btn_selectWorkspace = QPushButton("Select Workspace")
        self.btn_selectWorkspace.clicked.connect(self.selectWorkspace)
        
        self.btn_open = QPushButton('Open')
        self.btn_open.clicked.connect(self.open)
    
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
        
    def getToolbar(self) -> list[QWidget]:        
        return reversed([self.btn_selectWorkspace, self.btn_open, self.btn_copy, self.btn_paste, self.btn_delete])