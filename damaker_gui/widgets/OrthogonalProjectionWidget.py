from damaker_gui.widgets import ITabWidget, StackView, PreviewFrame, QGraphicsSceneMouseEvent
from PySide2.QtWidgets import QSplitter
from PySide2.QtCore import Qt, QPointF
import damaker_gui

class OrthogonalProjectionWidget(QSplitter, ITabWidget):
    name: str = "Orthogonal Projection"
    
    def __init__(self, parent=None, target: PreviewFrame=None):
        super().__init__(parent)

        self.target: PreviewFrame = target
        
        self.projX = StackView()
        self.projY = StackView()
        self.addWidget(self.projX)
        self.addWidget(self.projY)
        
    def connectTo(self, widget: PreviewFrame):
        self.projX.reset(widget.projX)
        self.projY.reset(widget.projY)        
        
        widget.view.mouseMoved.connect(self.moveCrosshair)
        
        try: self.target.mouseMoved.disconnect(self.moveCrosshair)
        except Exception: pass
        damaker_gui.MainWindow.Instance.addTab(2, self)
        
        self.target = widget        
        self.projX.updateFramePercentage(widget.idProj[0])
        self.projY.updateFramePercentage(widget.idProj[1])
    
    def disconnect(self, widget: PreviewFrame):
        try: widget.view.mouseMoved.disconnect(self.moveCrosshair)
        except Exception: pass
        if self.target == widget:      
            self.projX.clear()
            self.projY.clear()
            damaker_gui.MainWindow.Instance.ui.dock2.removeTab(self)
            self.target = None
    
    def moveCrosshair(self, event: QGraphicsSceneMouseEvent, pos: QPointF):
        if event.buttons() == Qt.RightButton:
            self.target.view.hLine.setPos(pos.y())
            self.target.view.vLine.setPos(pos.x())
            
            pX = pos.x()/self.target.view.shape[2]
            pY = pos.y()/self.target.view.shape[1]
            
            self.target.idProj = (pX, pY)
            
            self.projY.updateFramePercentage(pY)
            self.projX.updateFramePercentage(pX)
    
    def updateFrames(self):
        if self.projX is None or self.projY is None: return
        self.projX.updateFrame()
        self.projY.updateFrame()
    
    def setColorMap(self, widget, id: int, lut):
        if widget != self.target: return
        for chn, img in self.projX.channels.items() | self.projY.channels.items():
            if chn.id == id:
                img.setColorMap(lut)
                chn.lut = lut
        