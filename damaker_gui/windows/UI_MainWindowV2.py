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

from damaker_gui.widgets.ContentFrame import ContentFrame

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
        self.splitter_horizontal.setStyleSheet(u"QFrame {\n"
"	border: 0px;\n"
"}\n"
"\n"
"/* ----  TAB WIDGET ---- */\n"
"\n"
"QTabWidget {\n"
"	background-color: rgb(218, 219, 221);\n"
"	padding: 15px;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QTabBar {\n"
"	background-color: rgb(0, 0, 0);\n"
"	padding: 15px;\n"
"	margin: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QTabBar::pane {\n"
"  border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: black;  \n"
"	background-color: rgb(220, 220, 220);\n"
"    border: 1px solid rgb(235, 235, 235); \n"
"    padding: 4px 10px 4px 10px;\n"
"   border-radius: 2px;\n"
"} \n"
"\n"
"QTabBar::tab:hover {\n"
"  background-color: rgb(227, 241, 240);\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: rgb(222, 237, 255);\n"
"}\n"
"\n"
"/* ---- SLIDER ---- */\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 4px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(72, 75, 75);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(35, 31, 32);\n"
"    border: none;\n"
"    hei"
                        "ght: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 2px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(42, 42, 42);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(35, 31, 32);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 2px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(42, 42, 42);\n"
"}")
        self.splitter_horizontal.setOrientation(Qt.Horizontal)
        self.splitter_vertical1 = QSplitter(self.splitter_horizontal)
        self.splitter_vertical1.setObjectName(u"splitter_vertical1")
        self.splitter_vertical1.setStyleSheet(u"")
        self.splitter_vertical1.setOrientation(Qt.Vertical)
        self.dock1 = ContentFrame(self.splitter_vertical1)
        self.dock1.setObjectName(u"dock1")
        sizePolicy.setHeightForWidth(self.dock1.sizePolicy().hasHeightForWidth())
        self.dock1.setSizePolicy(sizePolicy)
        self.dock1.setStyleSheet(u"")
        self.layout_dock1 = QVBoxLayout(self.dock1)
        self.layout_dock1.setSpacing(0)
        self.layout_dock1.setObjectName(u"layout_dock1")
        self.layout_dock1.setContentsMargins(0, 0, 0, 0)
        self.dock1_tab = QTabWidget(self.dock1)
        self.dock1_tab.setObjectName(u"dock1_tab")
        self.dock1_tab.setStyleSheet(u"")
        self.dock1_tab.setTabsClosable(True)
        self.dock1_tabPage1 = QFrame()
        self.dock1_tabPage1.setObjectName(u"dock1_tabPage1")
        self.dock1_tabPage1.setStyleSheet(u"background-color: rgb(244, 248, 249);\n"
"margin: 0px;")
        self.gridLayout = QGridLayout(self.dock1_tabPage1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSlider = QSlider(self.dock1_tabPage1)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 2, 0, 1, 1)

        self.listView = QListView(self.dock1_tabPage1)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.dock1_tabPage1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 738, 309))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u":/flat-icons/icons/flat-icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dock1_tab.addTab(self.dock1_tabPage1, icon1, "")

        self.layout_dock1.addWidget(self.dock1_tab)

        self.splitter_vertical1.addWidget(self.dock1)
        self.dock3 = ContentFrame(self.splitter_vertical1)
        self.dock3.setObjectName(u"dock3")
        sizePolicy.setHeightForWidth(self.dock3.sizePolicy().hasHeightForWidth())
        self.dock3.setSizePolicy(sizePolicy)
        self.dock3.setStyleSheet(u"")
        self.layout_dock3 = QVBoxLayout(self.dock3)
        self.layout_dock3.setSpacing(0)
        self.layout_dock3.setObjectName(u"layout_dock3")
        self.layout_dock3.setContentsMargins(0, 0, 0, 0)
        self.dock3_tab = QTabWidget(self.dock3)
        self.dock3_tab.setObjectName(u"dock3_tab")

        self.layout_dock3.addWidget(self.dock3_tab)

        self.splitter_vertical1.addWidget(self.dock3)
        self.splitter_horizontal.addWidget(self.splitter_vertical1)
        self.splitter_vertical2 = QSplitter(self.splitter_horizontal)
        self.splitter_vertical2.setObjectName(u"splitter_vertical2")
        self.splitter_vertical2.setOrientation(Qt.Vertical)
        self.dock2 = ContentFrame(self.splitter_vertical2)
        self.dock2.setObjectName(u"dock2")
        sizePolicy.setHeightForWidth(self.dock2.sizePolicy().hasHeightForWidth())
        self.dock2.setSizePolicy(sizePolicy)
        self.dock2.setStyleSheet(u"")
        self.layout_dock2 = QVBoxLayout(self.dock2)
        self.layout_dock2.setSpacing(0)
        self.layout_dock2.setObjectName(u"layout_dock2")
        self.layout_dock2.setContentsMargins(0, 0, 0, 0)
        self.dock2_tab = QTabWidget(self.dock2)
        self.dock2_tab.setObjectName(u"dock2_tab")

        self.layout_dock2.addWidget(self.dock2_tab)

        self.splitter_vertical2.addWidget(self.dock2)
        self.dock4 = ContentFrame(self.splitter_vertical2)
        self.dock4.setObjectName(u"dock4")
        sizePolicy.setHeightForWidth(self.dock4.sizePolicy().hasHeightForWidth())
        self.dock4.setSizePolicy(sizePolicy)
        self.dock4.setStyleSheet(u"")
        self.layout_dock4 = QVBoxLayout(self.dock4)
        self.layout_dock4.setSpacing(0)
        self.layout_dock4.setObjectName(u"layout_dock4")
        self.layout_dock4.setContentsMargins(0, 0, 0, 0)
        self.dock4_tab = QTabWidget(self.dock4)
        self.dock4_tab.setObjectName(u"dock4_tab")
        self.dock4_tab.setTabShape(QTabWidget.Rounded)

        self.layout_dock4.addWidget(self.dock4_tab)

        self.splitter_vertical2.addWidget(self.dock4)
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
        self.dock1_tab.setTabText(self.dock1_tab.indexOf(self.dock1_tabPage1), QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi

