from damaker_gui.widgets import ITabWidget, PreviewWidget, PreviewFrame, QGraphicsSceneMouseEvent
from PySide2.QtWidgets import QSplitter
from PySide2.QtCore import Qt, QPointF
import damaker_gui

class OrthogonalProjectionWidget(QSplitter, ITabWidget):
    name: str = "Orthogonal Projection"
    
    def __init__(self, parent=None, origin: PreviewWidget=None):
        super().__init__(parent)

        self.origin = origin
        
        self.projX = PreviewWidget()
        self.projY = PreviewWidget()
        self.addWidget(self.projX)
        self.addWidget(self.projY)
        
    def connectTo(self, widget: PreviewFrame):
        self.projX.reset(widget.projX)
        self.projY.reset(widget.projY)        
        
        widget.view.mouseMoved.connect(self.moveCrosshair)
        
        try: self.origin.mouseMoved.disconnect(self.moveCrosshair)
        except Exception: pass
        damaker_gui.Window().addTab(2, self)
        
        self.origin = widget        
        self.projX.updateFramePercentage(widget.idProj[0])
        self.projY.updateFramePercentage(widget.idProj[1])
    
    def disconnect(self, widget: PreviewFrame):
        try: widget.view.mouseMoved.disconnect(self.moveCrosshair)
        except Exception: pass
        if self.origin == widget:      
            self.projX.clear()
            self.projY.clear()
            damaker_gui.Window().ui.dock2.removeTab(self)
            self.origin = None
    
    def moveCrosshair(self, event: QGraphicsSceneMouseEvent, pos: QPointF):
        if event.buttons() == Qt.RightButton:
            self.origin.view.hLine.setPos(pos.y())
            self.origin.view.vLine.setPos(pos.x())
            
            pX = pos.x()/self.origin.view.shape[2]
            pY = pos.y()/self.origin.view.shape[1]
            
            self.origin.idProj = (pX, pY)
            
            self.projY.updateFramePercentage(pY)
            self.projX.updateFramePercentage(pX)
        