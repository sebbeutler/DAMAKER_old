# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowV2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from damaker_gui.widgets.ContentDock import ContentDock

from  . import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1112, 758)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/damaker.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.splitter_horizontal = QSplitter(MainWindow)
        self.splitter_horizontal.setObjectName(u"splitter_horizontal")
        self.splitter_horizontal.setStyleSheet(u"")
        self.splitter_horizontal.setOrientation(Qt.Vertical)
        self.splitter_horizontal.setHandleWidth(7)
        self.splitter_vertical1 = QSplitter(self.splitter_horizontal)
        self.splitter_vertical1.setObjectName(u"splitter_vertical1")
        self.splitter_vertical1.setStyleSheet(u"")
        self.splitter_vertical1.setOrientation(Qt.Horizontal)
        self.splitter_vertical1.setHandleWidth(7)
        self.dock1_1 = ContentDock(self.splitter_vertical1)
        self.dock1_1.setObjectName(u"dock1_1")
        sizePolicy.setHeightForWidth(self.dock1_1.sizePolicy().hasHeightForWidth())
        self.dock1_1.setSizePolicy(sizePolicy)
        self.dock1_1.setStyleSheet(u"")
        self.splitter_vertical1.addWidget(self.dock1_1)
        self.dock1_2 = ContentDock(self.splitter_vertical1)
        self.dock1_2.setObjectName(u"dock1_2")
        sizePolicy.setHeightForWidth(self.dock1_2.sizePolicy().hasHeightForWidth())
        self.dock1_2.setSizePolicy(sizePolicy)
        self.dock1_2.setStyleSheet(u"")
        self.splitter_vertical1.addWidget(self.dock1_2)
        self.splitter_horizontal.addWidget(self.splitter_vertical1)
        self.splitter_vertical2 = QSplitter(self.splitter_horizontal)
        self.splitter_vertical2.setObjectName(u"splitter_vertical2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter_vertical2.sizePolicy().hasHeightForWidth())
        self.splitter_vertical2.setSizePolicy(sizePolicy1)
        self.splitter_vertical2.setOrientation(Qt.Horizontal)
        self.splitter_vertical2.setOpaqueResize(True)
        self.splitter_vertical2.setHandleWidth(7)
        self.dock2_1 = ContentDock(self.splitter_vertical2)
        self.dock2_1.setObjectName(u"dock2_1")
        sizePolicy.setHeightForWidth(self.dock2_1.sizePolicy().hasHeightForWidth())
        self.dock2_1.setSizePolicy(sizePolicy)
        self.dock2_1.setStyleSheet(u"")
        self.splitter_vertical2.addWidget(self.dock2_1)
        self.dock2_2 = ContentDock(self.splitter_vertical2)
        self.dock2_2.setObjectName(u"dock2_2")
        sizePolicy.setHeightForWidth(self.dock2_2.sizePolicy().hasHeightForWidth())
        self.dock2_2.setSizePolicy(sizePolicy)
        self.dock2_2.setStyleSheet(u"")
        self.splitter_vertical2.addWidget(self.dock2_2)
        self.dock2_3 = ContentDock(self.splitter_vertical2)
        self.dock2_3.setObjectName(u"dock2_3")
        sizePolicy.setHeightForWidth(self.dock2_3.sizePolicy().hasHeightForWidth())
        self.dock2_3.setSizePolicy(sizePolicy)
        self.dock2_3.setStyleSheet(u"")
        self.splitter_vertical2.addWidget(self.dock2_3)
        self.splitter_horizontal.addWidget(self.splitter_vertical2)
        MainWindow.setCentralWidget(self.splitter_horizontal)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1112, 21))
        self.menubar.setStyleSheet(u"")
        self.menubar.setDefaultUp(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DAMAKER", None))
    # retranslateUi

