from PySide2.QtWidgets import QTextEdit, QSizePolicy
from PySide2.QtGui import QTextCursor
from PySide2.QtCore import Signal

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
        builtins.print = lambda *args: [self.signalStreamOut.emit(str(txt)) for txt in args]
        
        self.signalStreamOut.connect(self.addText)
    
    @property
    def toolbar(self) -> list[ActionButton]:        
        return [ActionButton(self.clear, "Clear")]
        
    def addText(self, text):        
        self.append(str(text))
        self.moveCursor(QTextCursor.End)