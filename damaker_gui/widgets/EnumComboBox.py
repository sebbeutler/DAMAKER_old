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
    
    def getEnumChoice(self):
        choice = self.currentText()
        for e in self.enum:
            if e.name == choice:
                return e
        