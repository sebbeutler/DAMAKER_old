from PySide2.QtWidgets import QLayout

def clearLayout(layout: QLayout, delete=False):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        if widgetToRemove != None:
            widgetToRemove.setParent(None)
            if delete:
                widgetToRemove.deleteLater()

from .QFrameLayout import *
from .BatchSelectionWidget import *
from .ChannelsSelectorWidget import *
from .EnumComboBox import *
from .FileInfoWidget import *
from .FilePickerWidget import *
from .FunctionListWidget import *
from .ComboChoicesWidget import *
from .Preview3DWidget import *
from .PreviewWidget import *
from .RecordFunctionsWidget import *
from .WorkspaceWidget import *
from .ConsoleWidget import *
from .PipelineViewer import *
from .PipelineWidget import *
from .ITabWidget import *
from .OrthogonalProjectionWidget import *
from .LutSelectorWidget import *
from .PreviewFrame import *
from .AppSettingsWidget import *
from .ContentDock import *
from .DockHandler import *
from .OperationWidget import *
from .ColorAdjustWidget import *