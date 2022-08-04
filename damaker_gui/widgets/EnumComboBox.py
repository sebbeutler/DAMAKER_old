from PySide2.QtWidgets import QComboBox, QSizePolicy

import enum

class EnumComboBox(QComboBox):
    def __init__(self, enum_: enum.EnumMeta, text=""):
        super().__init__()
        self.enum = enum_
        for e in self.enum:
            self.addItem(e.name)
        self.setFixedHeight(25)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        if text != "":
            self.setCurrentText(text)