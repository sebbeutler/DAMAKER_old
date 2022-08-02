from PySide2.QtWidgets import QWidget

class ITabWidget:
    name: str = "None"
    icon: str = u":/flat-icons/icons/flat-icons/questions.svg"
    
    def closing(self):
        pass
    
    def getToolbar(self) -> list[QWidget]:
        return []