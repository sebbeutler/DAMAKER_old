from typing import Callable

from PySide2.QtWidgets import QListWidget, QAbstractItemView, QAction, QPushButton, QListWidgetItem, QGridLayout
from PySide2.QtCore import QSize, QThread, Signal, Slot, Qt

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
            
        self.btn_run = QPushButton("Run")
        self.btn_run.clicked.connect(self.runPipeline)  
        
        self.btn_stop = QPushButton("Stop")
        self.btn_stop.setEnabled(False)
        self.btn_stop.clicked.connect(self.stopPipeline)      
    
    def getToolbar(self):
        return [self.btn_stop, self.btn_run]

    def tabEnterFocus(self):
        damaker_gui.Window().operationList.connectPipeline(self)

    def tabExitFocus(self):
        damaker_gui.Window().operationList.disconnectPipeline(self)
    
    def runPipeline(self):                
        self.pipelineThread.setPipeline(self)        
        self.pipelineThread.stopped.connect(self.stopPipeline)        
        self.pipelineThread.start()
        # self.pipelineThread.run()
        self.btn_run.setEnabled(False)
        self.btn_stop.setEnabled(True)
    
    def stopPipeline(self):
        self.pipelineThread.terminate()
        print("(Pipeline ended 🟡)")
        self.btn_run.setEnabled(True)
        self.btn_stop.setEnabled(False)
    
    def addOperation(self, op: Operation):
        print(f"Operation '{op.name}' added ✔")
        item = QListWidgetItem("")
        # item = QListWidgetItem(op.name)       
        self.addItem(item)
        op_widget = widgets.OperationWidget(op=op, pipeline=self, layoutType=QGridLayout, batchMode=True) 
        item.setSizeHint(QSize(op_widget.width(), op_widget.height()))        
        self.setItemWidget(item, op_widget)
    
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
            operations.append(self.pipeline.itemWidget(self.pipeline.item(i)))
            
        print("[Starting Pipeline 🚀]")
        
        for item in operations:            
            if not item.op.enabled:
                item.setStyleSheet("background-color: rgb(130, 130, 130);")                
            else:     
                item.setStyleSheet("background-color: rgb(230, 230, 230);")
        
        step = 1
        for item in operations:
            if not item.op.enabled:
                continue
            print(f'-- [{step}] ➡ {item.op.name} --')
            item.setStyleSheet("background-color: rgb(244, 255, 189);")
            item.run()
            item.setStyleSheet("background-color: rgb(206, 255, 218);")
            step += 1
        
        print("[Pipeline finished 🟢]")
        self.stopped.emit()
                      