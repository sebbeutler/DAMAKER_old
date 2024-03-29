from PySide2.QtWidgets import QFrame, QFormLayout, QLabel
from PySide2.QtGui import QFont

import damaker_gui
import damaker_gui.widgets as widgets

class FileInfoWidget(QFrame, widgets.ITabWidget):
    name: str = "Info"
    icon: str = u":/flat-icons/icons/flat-icons/fine_print.svg"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QFormLayout()
        self.setLayout(self._layout)

        self._size = (widgets.QLabelFont("Size: "), widgets.QLabelFont())
        self._realSize = (widgets.QLabelFont("Real size: "), widgets.QLabelFont())
        self._pxSize = (widgets.QLabelFont("Pixel size: "), widgets.QLabelFont())
        self._position = (widgets.QLabelFont("Position: "), widgets.QLabelFont())
        self._value = (widgets.QLabelFont("Value: "), widgets.QLabelFont())

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
        self._size[1].setText(f'({mainChannel.shape[2]}, {mainChannel.shape[1]}, {mainChannel.shape[0]})')
        if mainChannel.px_sizes != None:
            self._realSize[1].setText(f'(%.2f, %.2f, %.2f)' % (
                mainChannel.shape[0]*mainChannel.px_sizes.X,
                mainChannel.shape[1]*mainChannel.px_sizes.Y,
                mainChannel.shape[2]*mainChannel.px_sizes.Z))
            self._pxSize[1].setText(f'(%.2f, %.2f, %.2f)' % (
                mainChannel.px_sizes.X,
                mainChannel.px_sizes.Y,
                mainChannel.px_sizes.Z))
        self._position[1].setText(
            f'x: {self.mx} y: {self.my} z: {self.preview.frameId}')
        if self.my < mainChannel.shape[1] and self.mx < mainChannel.shape[2]:
            values = ""
            for channel in self.preview.channels.keys():
                values += f"Ch{channel.id}: {channel.data[self.preview.frameId][self.my][self.mx]} "
            self._value[1].setText(values)
        else:
            self._value[1].setText('')

        status = f"\
{self._size[0].text()} {self._size[1].text()} \
{self._position[0].text()} {self._position[1].text()} \
{self._value[0].text()} {self._value[1].text()} \
"
        damaker_gui.setStatusMessage(status, 15000)
