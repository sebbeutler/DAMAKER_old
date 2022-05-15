from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

import PySimpleGUI as sg
sg.theme("DarkTeal2")

def getFilePath(text="Choose a file:"):
    layout = [[sg.T("")], [sg.Text(text), sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Button("Submit")]]
    window = sg.Window('Folder Picker', layout, size=(600,150))
    file = ""
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Submit":
            file = values["-IN-"]
            window.close()
            break
    return file

def getFolderPath(text="Choose a folder:"):
    layout = [[sg.T("")], [sg.Text(text), sg.Input(), sg.FolderBrowse(key="-IN-")],[sg.Button("Submit")]]
    window = sg.Window('Folder Picker', layout, size=(600,150))
    folder = ""
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Submit":
            folder = values["-IN-"]
            print(folder)
            window.close()
            break
    return folder

def getNewFilePath(text="Choose a file:"):
    layout = [[sg.T("")], [sg.Text(text), sg.Input(), sg.FileSaveAs(key="-IN-")],[sg.Button("Submit")]]
    window = sg.Window('Folder Picker', layout, size=(600,150))
    file = ""
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Submit":
            file = values["-IN-"]
            window.close()
            break
    return file

class FilePickerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout = QHBoxLayout()
        self.layout.setMargin(0)
        self.textEdit = QLineEdit()
        self.btnBrowse = QPushButton("Browse")
        self.btnBrowse.clicked.connect(self.changePath)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.btnBrowse)
        self.setLayout(self.layout)
    
    def setText(self, filePath):        
        self.textEdit.setText(filePath)
        self.textEdit.setToolTip(filePath)
    
    def text(self):
        return self.textEdit.text()
    
    def changePath(self):
        filePath = getFilePath()
        self.setText(filePath)

class FolderPickerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout = QHBoxLayout()
        self.layout.setMargin(0)
        self.textEdit = QLineEdit()
        self.btnBrowse = QPushButton("Browse")
        self.btnBrowse.clicked.connect(self.changePath)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.btnBrowse)
        self.setLayout(self.layout)
    
    def setText(self, filePath):        
        self.textEdit.setText(filePath)
        self.textEdit.setToolTip(filePath)
    
    def text(self):
        return self.textEdit.text()
    
    def changePath(self):
        filePath = getFolderPath()
        self.setText(filePath)
        