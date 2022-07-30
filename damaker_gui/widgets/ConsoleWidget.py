from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

class ConsoleWidget(QTextEdit):
    name: str = "Output"
    # icon: str = u":/flat-icons/icons/flat-icons/command_line.svg"
    icon: str = u":/flat-icons/icons/flat-icons/about.svg"
    
    signalStreamOut = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setUndoRedoEnabled(False)
        self.setReadOnly(True)
        
        import builtins
        
        self._print = builtins.print
        builtins.print = lambda *args: [self.signalStreamOut.emit(str(txt)) for txt in args]
        
        self.signalStreamOut.connect(self.addText)
        
        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.clear)
        
    def addText(self, text):        
        self.append(str(text))
        self.moveCursor(QTextCursor.End)
    
    def getToolbar(self):
        return [self.btn_clear]