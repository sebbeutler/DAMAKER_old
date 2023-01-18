
import damaker_gui.widgets as widgets

class DataViewWidget(widgets.QFrameLayout, widgets.IView):
    name: str = "Data Preview"
    icon: str = u":/flat-icons/icons/flat-icons/database.svg"

    def __init__(self):
        super().__init__()
