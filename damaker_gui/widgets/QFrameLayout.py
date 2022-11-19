from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout, QLayout
from PySide6.QtCore import Qt
import enum
from typing import Self

class LayoutTypes(enum.Enum):
    Vertical = QVBoxLayout
    Horizontal = QHBoxLayout
    Form = QFormLayout
    Grid = QGridLayout

class QFrameLayout(QFrame):
    def __init__(self, parent=None, _type: LayoutTypes=LayoutTypes.Vertical, spacing: int=4, margin: int=4) -> Self:
        super().__init__(parent)

        layout = _type.value()
        self.setLayout(layout)        
        self.layout: QLayout = layout
        self.layout.setSpacing(spacing)
        self.layout.setMargin(margin)
        return self

    def addWidget(self, *args) -> Self:
        self.addWidget(*args)
        return self