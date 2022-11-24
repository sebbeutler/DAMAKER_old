from PySide2.QtWidgets import QComboBox, QSizePolicy

class ComboChoicesWidget(QComboBox):
    def __init__(self, items: list[str]):
        super().__init__()
        for item in items:
            self.addItem(item)
        self.addItem("None")
        self.setCurrentText("None")                    
        self.setDuplicatesEnabled(False)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.setFixedHeight(22)