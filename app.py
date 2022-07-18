if __name__ == '__main__':
    import os
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_MainWindow.py --from-imports ./damaker_gui/windows/MainWindow.ui")
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_FunctionParametersWidget.py --from-imports ./damaker_gui/windows/FunctionParametersWidget.ui")
    os.system("pyside2-uic -o ./damaker_gui/windows/UI_BatchParametersWidget.py --from-imports ./damaker_gui/windows/BatchParametersWidget.ui")

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import *

from damaker_gui.widgets.FileInfoWidget import FileInfoWidget
from damaker_gui.PlanPage import PlanPage
from damaker_gui.VisualizePage import VisualizePage
from damaker_gui.AnalyzePage import AnalyzePage

import numpy as np

from damaker.Channel import Channel
from damaker_gui.windows.UI_MainWindow import *

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()        
        self.setupUi()
        
        self.show()

    def setupUi(self):
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)
        
        self.ui.frame_top.mouseMoveEvent = self.evt_moveWindow
        self.ui.btn_exit.clicked.connect(lambda e : self.close())
        self.ui.btn_minimize.clicked.connect(lambda e : self.showMinimized())
        self.ui.btn_maximize.clicked.connect(lambda e : self.showNormal() if self.isMaximized() else self.showMaximized())
        
        self.sizegrip = QSizeGrip(self.ui.btn_resize_grip)
        
        # ------------------------------------------------------------------------------------------------
        
        # -Top bar-
        self.ui.btn_plan.clicked.connect(lambda e : self.switchTab(0))
        self.ui.btn_visualize.clicked.connect(lambda e : self.switchTab(1))
        self.ui.btn_analyse.clicked.connect(lambda e : self.switchTab(2))
        
        # -Left bar-
        self.ui.fileInfo = FileInfoWidget(self.ui.label_fileInfo)
        
        self.ui.fileSystemModel = QFileSystemModel(self.ui.treeview_workspace)
        self.ui.fileSystemModel.setReadOnly(False)        
        root = self.ui.fileSystemModel.setRootPath("/")
        
        self.ui.treeview_workspace.setModel(self.ui.fileSystemModel)
        self.ui.treeview_workspace.setRootIndex(root)
        
        self.ui.treeview_workspace.setColumnHidden(1, True)
        self.ui.treeview_workspace.setColumnHidden(2, True)
        self.ui.treeview_workspace.setColumnHidden(3, True)
        
        self.ui.btn_selectWorkspace.clicked.connect(self.selectWorkspace)
        
        self.planPage = PlanPage(self.ui)
        self.visualizePage = VisualizePage(self.ui)  
        self.analyzePage = AnalyzePage(self.ui)
        # self.switchTab(0)
        self.setFocus()
    
    def switchTab(self, index):
        self.ui.content_tabs.setCurrentIndex(index)
        tabs_btn = [self.ui.btn_plan, self.ui.btn_visualize, self.ui.btn_analyse]
        for btn in tabs_btn:
            btn.setChecked(False)
        tabs_btn[index].setChecked(True)

    def keyPressEvent(self, event):
        # print(f"Key: {str(event.key())} Text Press: {str(event.text())}")
        if event.key() == Qt.Key_Escape:
            self.close()
        return super(AppWindow, self).keyPressEvent(event)
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        return super(AppWindow, self).mousePressEvent(event)
    
    def evt_moveWindow(self, event):
        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            new_pos: QPoint = self.pos() + event.globalPos() - self.dragPos
            # new_pos.setX(max(0, new_pos.x()))
            new_pos.setY(max(0, new_pos.y()))
            self.move(new_pos)
            self.dragPos = event.globalPos()
            event.accept()
    
    def selectWorkspace(self, event):
        path = QFileDialog.getExistingDirectory(None, 'Open folder', self.ui.fileSystemModel.rootPath())
        root = self.ui.fileSystemModel.setRootPath(path)
        self.ui.treeview_workspace.setRootIndex(root)

if __name__ == '__main__':
    import sys, os
    os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-18.0.1.1"
    # os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-11.0.13"
    
    app = QApplication(sys.argv)
    window = AppWindow()    
    sys.exit(app.exec_())
    
    from damaker.processing import *
    from damaker.utils import *
    from damaker.pipeline import *
    import SimpleITK as sitk
    
    # a = BatchParameters()
    # a.folder = "C:/Users/PC/source/DAMAKER/resources/output/segmentation"
    # a.associated = True
    # a.load()
    
    # a = BatchParameters()
    # a.folder = "C:/Users/PC/source/DAMAKER/resources/output/segmentation"
    # a.mods.append("1;2;3;4")
    # a.mods.append("1;2")
    # a.mods.append("1;3;4")
    # a.file = "User{1}C{2}E{3}.tif"
    # a.associated = False
    # a.load()
    
    # load = loadChannelsFromDir("resources/output/registration")
    # ref = loadChannelsFromFile("resources/batch/User1C2E1.tif")[0]
    # ref2 = resliceTop(ref)
    # plotChannel(ref)
    # plotChannel(ref2)
    
    # out = segmentation(ref, "C:/Users/PC/source/DAMAKER/resources/segmentation/CU4.model")
    # out.save("4.tif")
    # out = segmentation(ref, "C:/Users/PC/source/DAMAKER/resources/segmentation/CU2.model")
    # out.save("2.tif")
    #         "C:/Users/PC/source/DAMAKER/damaker/weka/bin/weka_segmentation_gateway.jar")
    # for chn in load:
    # channelSave(out, "resources/out-reg/")
    
    # p = Pipeline()
    # l = p.add(loadChannelsFromDir, "resources/out-reg/", "")
    # out = p.add(wekaSegmentation, l, "C:/Users/PC/source/DAMAKER/resources/segmentation/CU1.model",
    #         "C:/Users/PC/source/DAMAKER/damaker/weka/bin/weka_segmentation_gateway.jar")
    # p.add(channelSave, out, "C:/Users/PC/source/DAMAKER/resources/out-seg/")
    # p.run()
    # for chn in out:
    #     plotChannelRGB(chn, None, ref)