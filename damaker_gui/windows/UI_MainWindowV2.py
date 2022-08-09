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
        self.splitter_horizontal.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #4e4e4e;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 100, 99, 255),stop:1 rgba(89, 89, 89, 255));\n"
"	border: none;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"	background-color: #303030;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(89, 89, 89, 255),stop:1 rgba(66, 66, 66, 255));\n"
"	border: 1px solid #000;\n"
"	"
                        "color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #d3d3d3;\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"    padding-right: 0px;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #91c9f7;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar \n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar \n"
"{\n"
"	border:none;\n"
"	left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab \n"
"{\n"
"	color: #fff;\n"
"	padding-left: 15px; \n"
"	padding-right: 15px; \n"
"	height: 25px;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	border: 1px solid rgb(71, 71, 71); \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!"
                        "selected \n"
"{\n"
"	color: #b1b1b1; \n"
"	border: 1px solid #1b1b1b;\n"
"	background-color: #1b1b1b;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected \n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(101, 101, 101, 255),stop:1 rgba(66, 66, 66, 255));\n"
"	border: 1px solid #414141;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"	color: #fff; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(82, 82, 82, 255),stop:0.995192 rgba(75, 75, 75, 255));\n"
"	color: #fff;\n"
"	border: 1px solid #777777;\n"
"	border-radius: 2px;\n"
"	padding: 2px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: #8b8b8b;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: #7c7c7c;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	background-color: #7c7c7c;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDockWidget----"
                        "-*/\n"
" QDockWidget\n"
"{\n"
"	color : #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::title \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 100, 99, 255),stop:1 rgba(89, 89, 89, 255));\n"
"	border: 1px solid #3a3a3a;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::close-button\n"
"{\n"
"	max-width: 14px;\n"
"	max-height: 14px;\n"
"	margin-top:1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::float-button\n"
"{\n"
"	max-width: 14px;\n"
"	max-height: 14px;\n"
"	margin-top:1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::close-button:hover\n"
"{\n"
"	border: none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::float-button:hover\n"
"{\n"
"	border: none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeWidget\n"
"{\n"
"	show-decoration-selected: 0;\n"
"	selection-background-color: transparent; /* Used on Mac */\n"
"	selection-color: #fff; /* Used on Mac */\n"
"	background-color: #292929;\n"
"	border: 1px soli"
                        "d gray;\n"
"	padding-top : 5px;\n"
"	color: #fff;\n"
"	font: 8pt;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	background-color: #292929;\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"	color:#000;\n"
"	background-color: #91c9f7;\n"
"	border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"	background-color: #8f8f8f;\n"
"	color: #000;\n"
"}\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	color : black;\n"
"	background-color: rgb(157, 157, 157);\n"
"	border: 1px solid darkgray;\n"
"	border-radius : 2px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover \n"
"{\n"
"	background-color: rgb(190, 190, 190);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 0px solid gray;\n"
"	background-color: rgb(27, 27, 27);\n"
"    margin-top: 5.5ex;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 100, 99, 255),stop:1 rgba(89, 89, 89, 255));\n"
"	border: 1px s"
                        "olid #3a3a3a;\n"
"    subcontrol-origin: margin;\n"
"	subcontrol-position: top right 0px;\n"
"	border-radius: 0px;\n"
"    padding: 1px 30px;\n"
"	margin-bottom: 52px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 100, 99, 255),stop:1 rgba(89, 89, 89, 255));\n"
"	border: 1px solid #777777;\n"
"	color: #fff;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:editable \n"
"{\n"
"    background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"	background-color: #252525;\n"
"    border-left-width:1px;\n"
"    border-left-color: #777777;\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on \n"
"{ \n"
"    top: 1px;\n"
"    left: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox Q"
                        "ListView\n"
"{\n"
"	background-color: #292929;\n"
"    border-left-style: solid; \n"
"	selection-background-color: #91c9f7;\n"
"	selection-color: #000;\n"
"	color: #fff;\n"
"	border: 1px solid black;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox-----*/\n"
"QSpinBox \n"
"{\n"
"    border: 1px solid gray;\n"
"	min-height: 12px;\n"
"    border-radius : 2px;\n"
"	color : black;\n"
"    background-color: rgb(157, 157, 157);\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover \n"
"{\n"
"	background-color: rgb(190, 190, 190);\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button \n"
"{\n"
"	border-top-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover \n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed \n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button \n"
"{\n"
"	border-bottom-right-radius:2px;\n"
""
                        "	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:hover \n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed \n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"	color: lightgray;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	margin-top:2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar \n"
"{\n"
"	color: #fff;\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 100, 99, 255),stop:1 rgba(89, 89, 89, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"QStatusBar::item \n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"QSplitter::handle\n"
"{\n"
"	background-color: #777777;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 7"
                        "px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 7px;\n"
"}")
        self.splitter_horizontal.setOrientation(Qt.Horizontal)
        self.splitter_horizontal.setHandleWidth(7)
        self.splitter_vertical1 = QSplitter(self.splitter_horizontal)
        self.splitter_vertical1.setObjectName(u"splitter_vertical1")
        self.splitter_vertical1.setStyleSheet(u"")
        self.splitter_vertical1.setOrientation(Qt.Vertical)
        self.splitter_vertical1.setHandleWidth(7)
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
        self.splitter_vertical2.setHandleWidth(7)
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
    # retranslateUi

