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
            return
        if self.preview.channel is None:
            return
        chn = self.preview.channel
        text = f'Size: ({chn.shape[2]}, {chn.shape[1]}, {chn.shape[0]})\n'  
        if chn.px_sizes != None:
            text += f'Real size: (%.2f, %.2f, %.2f)\n' % (
                chn.shape[0]*chn.px_sizes.X, 
                chn.shape[1]*chn.px_sizes.Y, 
                chn.shape[2]*chn.px_sizes.Z)  
            text += f'Pixel size: '
            text += "x:%.2f " % chn.px_sizes.X
            text += "y:%.2f " % chn.px_sizes.Y
            text += "z:%.2f\n" % chn.px_sizes.Z
        text += f'Position: x:{self.mx} y:{self.my} z:{self.preview.frame_id} \n'
        if self.my < chn.shape[1] and self.mx < chn.shape[2]:
            text += f'Value: {chn.data[self.preview.frame_id][self.my][self.mx]}\n'
        
        self.label.setText(text)