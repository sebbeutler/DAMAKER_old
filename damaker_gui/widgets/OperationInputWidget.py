from PySide2.QtWidgets import QComboBox, QSizePolicy

from damaker_gui.widgets.ITabWidget import ITabWidget

class OperationInputWidget(QComboBox, ITabWidget):
    def __init__(self, operations: list[str]):
        super().__init__()
        for op in operations:
            self.addItem(op)
        self.addItem("None")
        self.setCurrentText("None")                    
        self.setDuplicatesEnabled(False)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.setFixedHeight(22)