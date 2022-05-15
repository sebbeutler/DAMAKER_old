from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

class FileInfoWidget:
    def __init__(self, label: QLabel):
        self.label = label
        self.preview = None
        self.mx = 0
        self.my = 0
    
    def update(self):
        if self.preview is None:
            pass
        
        text = f'Width: {self.preview.channel.shape[1]} \n'
        text += f'Height: {self.preview.channel.shape[0]} \n'
        text += f'Depth: {self.preview.channel.shape[0]} \n'
        text += f'Position: x:{self.mx} y:{self.my} z:{self.preview.frame_id} \n'
        
        if self.preview.channel.px_sizes != None:
            text += f'Pixel size:'
            text += "x:%.2f " % self.preview.channel.px_sizes.X
            text += "y:%.2f " % self.preview.channel.px_sizes.Y
            text += "z:%.2f " % self.preview.channel.px_sizes.Z
        
        self.label.setText(text)