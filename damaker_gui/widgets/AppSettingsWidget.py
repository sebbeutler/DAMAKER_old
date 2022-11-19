from PySide6.QtWidgets import QWidget, QFormLayout, QComboBox, QSizePolicy
from PySide6.QtCore import QFile, QIODevice, QTextStream

import damaker_gui
import damaker_gui.widgets as widgets

class AppSettingsWidget(QWidget, widgets.ITabWidget):
    name: str = 'Settings'
    icon: str = u":/flat-icons/icons/flat-icons/settings.svg"

    def __init__(self, parent=None):
        super().__init__(parent)

        self._layout = QFormLayout()
        self.setLayout(self._layout)

        self.theme = ThemeComboBox()
        self._layout.addRow("Theme: ", self.theme)

class ThemeComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.themes = {
            "Dark": QFile(u":/themes/styles/Eclippy.qss"),
            "Light": QFile(u":/themes/styles/theme.qss"),
            "Office": QFile(u":/themes/styles/ExcelOffice.qss"),
            "Integrid": QFile(u":/themes/styles/Integrid.qss"),
        }

        self.addItems(list(self.themes.keys()))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.currentTextChanged.connect(self.setTheme)

    def setTheme(self, theme: str):
        file = self.themes[theme]

        if file.open(QIODevice.ReadOnly | QFile.Text):
            text = QTextStream(file).readAll()
            damaker_gui.MainWindow.Instance.setStyleSheet(text)
            file.close()
