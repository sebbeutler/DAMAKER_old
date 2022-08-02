from .BatchSelectionWidget import *
from .ChannelsSelectorWidget import *
from .EnumComboBox import *
from .FileInfoWidget import *
from .FilePickerWidget import *
from .FunctionListWidget import *
from .FunctionParametersWidget import *
from .OperationInputWidget import *
from .Preview3DWidget import *
from .PreviewWidget import *
from .RecordFunctionsWidget import *
from .ContentFrame import *
from .WorkspaceWidget import *
from .ConsoleWidget import *
from .PipelineWidget import *
from .OperationWidget import *
from .ITabWidget import *
from .OrthogonalProjectionWidget import *

def clearLayout(layout: QLayout, delete=False):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        if widgetToRemove != None:
            widgetToRemove.setParent(None)
            if delete:
                widgetToRemove.deleteLater()