from PySide2.QtWidgets import QFrame, QFormLayout, QLabel

from damaker_gui.widgets.ITabWidget import ITabWidget

class FileInfoWidget(QFrame, ITabWidget):
    name: str = "Info"
    icon: str = u":/flat-icons/icons/flat-icons/fine_print.svg"
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QFormLayout()
        self.setLayout(self._layout)
        
        self._size = (QLabel("Size:"), QLabel())
        self._realSize = (QLabel("Real size:"), QLabel())
        self._pxSize = (QLabel("Pixel size:"), QLabel())
        self._position = (QLabel("Position:"), QLabel())
        self._value = (QLabel("Value:"), QLabel())
        
        self._layout.addRow(self._size[0], self._size[1])
        self._layout.addRow(self._realSize[0], self._realSize[1])
        self._layout.addRow(self._pxSize[0], self._pxSize[1])
        self._layout.addRow(self._position[0], self._position[1])
        self._layout.addRow(self._value[0], self._value[1])
        
        self.preview = None
        self.mx = 0
        self.my = 0
    
    def update(self):
        if self.preview is None or len(self.preview.channels.keys()) == 0:
            return
        mainChannel = list(self.preview.channels.keys())[0]
        self._size[1].setText(f'Size: ({mainChannel.shape[2]}, {mainChannel.shape[1]}, {mainChannel.shape[0]})\n')
        if mainChannel.px_sizes != None:
            self._realSize[1].setText(f'(%.2f, %.2f, %.2f)' % (
                mainChannel.shape[0]*mainChannel.px_sizes.X, 
                mainChannel.shape[1]*mainChannel.px_sizes.Y, 
                mainChannel.shape[2]*mainChannel.px_sizes.Z))
            self._pxSize[1].setText(f'(%.2f, %.2f, %.2f)' % (
                mainChannel.px_sizes.X,
                mainChannel.px_sizes.Y,
                mainChannel.px_sizes.Z))
        self._position[1].setText(f'x:{self.mx} y:{self.my} z:{self.preview.frameId}')
        if self.my < mainChannel.shape[1] and self.mx < mainChannel.shape[2]:
            values = ""
            for channel in self.preview.channels.keys():
                values += f"Ch{channel.id}:{channel.data[self.preview.frameId][self.my][self.mx]}\n"
            self._value[1].setText(values)
        else:
            self._value[1].setText('')