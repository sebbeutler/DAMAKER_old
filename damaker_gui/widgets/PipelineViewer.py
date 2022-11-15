
from PySide2.QtWidgets import QListWidget, QAbstractItemView, QAction, QPushButton, QListWidgetItem, QGridLayout, QSplitter
from PySide2.QtCore import QSize, QThread, Signal, Slot, Qt
import damaker
from damaker.pipeline import Operation
import damaker_gui.widgets as widgets
import damaker_gui
from damaker_gui.widgets.ITabWidget import ActionButton

class PipelineViewer(QSplitter, widgets.ITabWidget):
    name: str = "Pipeline"
    icon: str = u":/flat-icons/icons/flat-icons/timeline.svg"

    @property
    def toolbar(self) -> list[ActionButton]:
        return [ActionButton(self.pipeline.runPipeline, "Run"),
                ActionButton(self.pipeline.stopPipeline, "Stop"),]

    def __init__(self, parent=None, operations=[]):
        super().__init__(parent)

        self.pipeline = widgets.PipelineWidget(None, operations)
        self.addWidget(self.pipeline)

        self.functionForm = widgets.FunctionForm(None)
        self.addWidget(self.functionForm)

        self.pipeline.currentItemChanged.connect(self.onItemChanged)

    def getToolbar(self):
        return [self.pipeline.btn_stop, self.pipeline.btn_run]

    # Note: current is none when deleting the last item in the list so we cant use current.text() in the else statement
    def onItemChanged(self, current: QListWidgetItem, previous: QListWidgetItem):
        if hasattr(current, 'op'):
            self.editOperation(current.op)
        else:
            print(f'WARNING: OPERATION {current} doesnt have an "op" attribute')

    def editOperation(self, op: Operation):
        self.functionForm.fromOperation(op)

    def addOperation(self, op: Operation):
        return self.pipeline.addOperation(op)

    def tabEnterFocus(self):
        damaker_gui.MainWindow.Instance.operationList.connectPipeline(self)

    def tabExitFocus(self):
        damaker_gui.MainWindow.Instance.operationList.disconnectPipeline(self)