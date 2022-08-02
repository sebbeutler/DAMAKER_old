from PySide2.QtWidgets import QWidget

class ITabWidget:
    tabIndex: int = -1
    name: str = "None"
    icon: str = u":/flat-icons/icons/flat-icons/questions.svg"
    
    def tabExitFocus(self):
        pass
    
    def tabEnterFocus(self):
        pass
    
    def closing(self):
        pass
    
    def getToolbar(self) -> list[QWidget]:
        return []