from PySide6.QtWidgets import QTextEdit, QSizePolicy
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Signal

import damaker_gui
from damaker_gui.widgets.ITabWidget import ActionButton, ITabWidget

class ConsoleWidget(QTextEdit, ITabWidget):
    name: str = "Console"
    icon: str = u":/flat-icons/icons/flat-icons/command_line.svg"
    # icon: str = u":/flat-icons/icons/flat-icons/about.svg"
    
    signalStreamOut = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setUndoRedoEnabled(False)
        self.setReadOnly(True)
        
        import builtins
        
        self._print = builtins.print
        builtins.print = self.logger
        
        self.signalStreamOut.connect(self.addText)
        self.signalStreamOut.connect(damaker_gui.setStatusMessage)
    
    def logger(self, *args):
        for msg in args:
            self.signalStreamOut.emit(str(msg)) 
    
    @property
    def toolbar(self) -> list[ActionButton]:        
        return [ActionButton(self.clear, "Clear")]
        
    def addText(self, text):        
        self.append(str(text))
        self.moveCursor(QTextCursor.End)