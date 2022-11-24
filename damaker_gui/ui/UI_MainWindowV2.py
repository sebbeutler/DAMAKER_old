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
        MainWindow.resize(889, 576)
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
        self.splitter_horizontal.setOrientation(Qt.Horizontal)
        self.splitter_horizontal.setHandleWidth(7)
        self.splitter_vertical1 = QSplitter(self.splitter_horizontal)
        self.splitter_vertical1.setObjectName(u"splitter_vertical1")
        self.splitter_vertical1.setBaseSize(QSize(0, 900))
        self.splitter_vertical1.setStyleSheet(u"")
        self.splitter_vertical1.setOrientation(Qt.Vertical)
        self.splitter_vertical1.setHandleWidth(7)
        self.dock1 = ContentDock(self.splitter_vertical1)
        self.dock1.setObjectName(u"dock1")
        sizePolicy.setHeightForWidth(self.dock1.sizePolicy().hasHeightForWidth())
        self.dock1.setSizePolicy(sizePolicy)
        self.dock1.setStyleSheet(u"")
        self.splitter_vertical1.addWidget(self.dock1)
        self.splitter_vertical1_1 = QSplitter(self.splitter_vertical1)
        self.splitter_vertical1_1.setObjectName(u"splitter_vertical1_1")
        self.splitter_vertical1_1.setBaseSize(QSize(0, 900))
        self.splitter_vertical1_1.setStyleSheet(u"")
        self.splitter_vertical1_1.setOrientation(Qt.Horizontal)
        self.splitter_vertical1_1.setHandleWidth(7)
        self.dock3 = ContentDock(self.splitter_vertical1_1)
        self.dock3.setObjectName(u"dock3")
        sizePolicy.setHeightForWidth(self.dock3.sizePolicy().hasHeightForWidth())
        self.dock3.setSizePolicy(sizePolicy)
        self.dock3.setStyleSheet(u"")
        self.splitter_vertical1_1.addWidget(self.dock3)
        self.splitter_vertical1.addWidget(self.splitter_vertical1_1)
        self.splitter_horizontal.addWidget(self.splitter_vertical1)
        self.splitter_vertical2 = QSplitter(self.splitter_horizontal)
        self.splitter_vertical2.setObjectName(u"splitter_vertical2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter_vertical2.sizePolicy().hasHeightForWidth())
        self.splitter_vertical2.setSizePolicy(sizePolicy1)
        self.splitter_vertical2.setOrientation(Qt.Vertical)
        self.splitter_vertical2.setOpaqueResize(True)
        self.splitter_vertical2.setHandleWidth(7)
        self.dock2 = ContentDock(self.splitter_vertical2)
        self.dock2.setObjectName(u"dock2")
        sizePolicy.setHeightForWidth(self.dock2.sizePolicy().hasHeightForWidth())
        self.dock2.setSizePolicy(sizePolicy)
        self.dock2.setStyleSheet(u"")
        self.splitter_vertical2.addWidget(self.dock2)
        self.splitter_horizontal2 = QSplitter(self.splitter_vertical2)
        self.splitter_horizontal2.setObjectName(u"splitter_horizontal2")
        sizePolicy1.setHeightForWidth(self.splitter_horizontal2.sizePolicy().hasHeightForWidth())
        self.splitter_horizontal2.setSizePolicy(sizePolicy1)
        self.splitter_horizontal2.setOrientation(Qt.Horizontal)
        self.splitter_horizontal2.setOpaqueResize(True)
        self.splitter_horizontal2.setHandleWidth(7)
        self.dock4 = ContentDock(self.splitter_horizontal2)
        self.dock4.setObjectName(u"dock4")
        sizePolicy.setHeightForWidth(self.dock4.sizePolicy().hasHeightForWidth())
        self.dock4.setSizePolicy(sizePolicy)
        self.dock4.setStyleSheet(u"")
        self.splitter_horizontal2.addWidget(self.dock4)
        self.splitter_vertical2.addWidget(self.splitter_horizontal2)
        self.splitter_horizontal.addWidget(self.splitter_vertical2)
        MainWindow.setCentralWidget(self.splitter_horizontal)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 889, 21))
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

