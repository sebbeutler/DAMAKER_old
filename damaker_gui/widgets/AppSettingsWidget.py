from PySide2.QtWidgets import QWidget

import damaker_gui.widgets as widgets

class AppSettingsWidget(QWidget, widgets.ITabWidget):
    name: str = 'Settings'
    icon: str = u":/flat-icons/icons/flat-icons/settings.svg"
    
    def __init__(self, parent=None):
        super().__init__(parent)
        pass