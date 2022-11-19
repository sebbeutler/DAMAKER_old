from typing import Callable

from PySide6.QtWidgets import QListWidget, QAbstractItemView, QAction, QPushButton, QListWidgetItem, QGridLayout
from PySide6.QtCore import QSize, QThread, Signal, Slot, Qt
import damaker

from damaker.pipeline import *
import damaker_gui
import damaker_gui.widgets as widgets

class PipelineWidget(QListWidget, widgets.ITabWidget):
    name: str = "Pipeline"
    icon: str = u":/flat-icons/icons/flat-icons/timeline.svg"

    def __init__(self, parent=None, operations=[]):
        super().__init__(parent)

        self.setSpacing(3)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setVerticalScrollMode(QListWidget.ScrollMode.ScrollPerPixel)

        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        act = QAction("Remove", self)
        act.triggered.connect(self.removeOperation)
        self.addAction(act)

        for op in operations:
            self.addOperation(op)

        self.pipelineThread = PipelineRunnerThread()

    def tabEnterFocus(self):
        damaker_gui.MainWindow.Instance.operationList.connectPipeline(self)

    def tabExitFocus(self):
        damaker_gui.MainWindow.Instance.operationList.disconnectPipeline(self)

    def runPipeline(self):
        self.pipelineThread.setPipeline(self)
        self.pipelineThread.stopped.connect(self.stopPipeline)
        self.pipelineThread.start()
        # self.pipelineThread.run()

    def stopPipeline(self):
        self.pipelineThread.terminate()
        print("(Pipeline ended 🟡)")

    def addOperation(self, op: Operation):
        print(f"Operation '{op.name}' added ✔")
        item = QListWidgetItem(op.name)
        item.op = op.copy()
        self.addItem(item)
        # op_widget = widgets.OperationWidget(op=op, pipeline=self, layoutType=QGridLayout, batchMode=True) 
        # item.setSizeHint(QSize(op_widget.width(), op_widget.height()))

    def addOpfromFunc(self, func: Callable):
        self.addOperation(Operation(func, [], func.__name__))

    def removeOperation(self):
        self.takeItem(self.currentRow())


class PipelineRunnerThread(QThread):
    stopped = Signal()
    def __init__(self, pipeline: PipelineWidget=None):
        super(PipelineRunnerThread, self).__init__()
        self.pipeline = pipeline

    def setPipeline(self, pipeline: PipelineWidget):
        self.pipeline = pipeline

    @Slot()
    def run(self):
        if self.pipeline is None:
            pass
        self.setPriority(QThread.HighPriority)
        operations: list[widgets.OperationWidget] = []
        for i in range(self.pipeline.count()):
            # operations.append(self.pipeline.itemWidget(self.pipeline.item(i)))
            operations.append(self.pipeline.item(i).op)

        print("[Starting Pipeline 🚀]")

        step = 1
        for op in operations:
            if not op.enabled:
                continue
            print(f'-- [{step}] ➡ {op.name} --')
            op.run()
            step += 1

        print("[Pipeline finished 🟢]")
        self.stopped.emit()
