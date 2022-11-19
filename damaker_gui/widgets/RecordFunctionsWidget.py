from PySide6.QtWidgets import QVBoxLayout, QListWidget, QHBoxLayout, QPushButton, QListWidgetItem

from damaker.pipeline import Operation

class RecordFunctionsWidget:
    def __init__(self, parentLayout: QVBoxLayout):
        self.layout = parentLayout
        self.funcList = QListWidget()
        self.layout.addWidget(self.funcList)
        
        self.btn_layout = QHBoxLayout()
        self.btn_start = QPushButton("Start")
        self.btn_start.setCheckable(True)
        self.btn_start.setStyleSheet("QPushButton:checked { background-color: rgb(235, 64, 52);}")
        self.btn_start.clicked.connect(self.record)
        self.btn_layout.addWidget(self.btn_start)
        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.funcList.clear)
        self.btn_layout.addWidget(self.btn_clear)
        self.layout.addLayout(self.btn_layout)

        self.isRecording = False
    
    def record(self):
        self.isRecording = not self.isRecording
        
        if self.isRecording:
            self.btn_start.setText("Stop")
        else:
            self.btn_start.setText("Start")
            
    def addOperation(self, op: Operation):
        if self.isRecording is False:
            return

        item = QListWidgetItem(op.name)
        item.operation = op
        self.funcList.addItem(item)