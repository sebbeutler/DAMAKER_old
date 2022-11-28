from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QFont

class QLabelFont(QLabel):
    def __init__(self, text="[Empty]", size=7, font="Arial"):
        super().__init__(text)
        self.setFont(QFont(font, size))
