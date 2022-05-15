# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1101, 871)
        MainWindow.setMinimumSize(QSize(500, 200))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.centralwidget_layout = QHBoxLayout(self.centralwidget)
        self.centralwidget_layout.setSpacing(0)
        self.centralwidget_layout.setObjectName(u"centralwidget_layout")
        self.centralwidget_layout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setMinimumSize(QSize(0, 0))
        self.frame_main.setMaximumSize(QSize(16777215, 16777215))
        self.frame_main.setStyleSheet(u"* {\n"
"	outline: 0;\n"
"}\n"
"\n"
"*:focus\n"
"{\n"
"	border-color: rgb(68, 170, 94);\n"
"}\n"
"\n"
"#frame_main {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.47995, y2:1, stop:0 rgba(105, 106, 130, 240), stop:1 rgba(47, 47, 47, 255));\n"
"\n"
"	border-radius: 12px;\n"
"	border: 1px solid rgb(27, 29, 35);\n"
"}\n"
"\n"
"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
""
                        "    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBa"
                        "r::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
""
                        "QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
""
                        "	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSl"
                        "ider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid r"
                        "gb(43, 50, 61);\n"
"}")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_main_layout = QVBoxLayout(self.frame_main)
        self.frame_main_layout.setSpacing(0)
        self.frame_main_layout.setObjectName(u"frame_main_layout")
        self.frame_main_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_main_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setMinimumSize(QSize(100, 30))
        self.frame_top.setMaximumSize(QSize(16777215, 30))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top_layout = QHBoxLayout(self.frame_top)
        self.frame_top_layout.setSpacing(1)
        self.frame_top_layout.setObjectName(u"frame_top_layout")
        self.frame_top_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame = QFrame(self.frame_top)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy1)
        self.horizontalFrame.setMinimumSize(QSize(189, 0))
        self.layout_pageSelect = QHBoxLayout(self.horizontalFrame)
        self.layout_pageSelect.setSpacing(3)
        self.layout_pageSelect.setObjectName(u"layout_pageSelect")
        self.layout_pageSelect.setContentsMargins(5, 0, 0, 0)
        self.btn_plan = QPushButton(self.horizontalFrame)
        self.btn_plan.setObjectName(u"btn_plan")

        self.layout_pageSelect.addWidget(self.btn_plan)

        self.btn_visualize = QPushButton(self.horizontalFrame)
        self.btn_visualize.setObjectName(u"btn_visualize")

        self.layout_pageSelect.addWidget(self.btn_visualize)

        self.btn_analyse = QPushButton(self.horizontalFrame)
        self.btn_analyse.setObjectName(u"btn_analyse")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_analyse.sizePolicy().hasHeightForWidth())
        self.btn_analyse.setSizePolicy(sizePolicy2)
        self.btn_analyse.setMinimumSize(QSize(0, 0))
        self.btn_analyse.setMaximumSize(QSize(16777215, 16777215))

        self.layout_pageSelect.addWidget(self.btn_analyse)


        self.frame_top_layout.addWidget(self.horizontalFrame)

        self.spring = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.frame_top_layout.addItem(self.spring)

        self.btn_minimize = QPushButton(self.frame_top)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(30, 20))
        self.btn_minimize.setMaximumSize(QSize(60, 60))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgba(104, 104, 124, 125);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(212, 212, 212, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(109, 109, 109);\n"
"}\n"
"\n"
"QPushButton:focus \n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-arrow-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.frame_top_layout.addWidget(self.btn_minimize)

        self.btn_exit = QPushButton(self.frame_top)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(30, 20))
        self.btn_exit.setMaximumSize(QSize(60, 60))
        self.btn_exit.setStyleSheet(u"#btn_exit {\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(217, 69, 64);\n"
"}\n"
"\n"
"#btn_exit:hover {\n"
"	background-color: rgb(255, 115, 110);\n"
"}\n"
"\n"
"#btn_exit:pressed {\n"
"	background-color: rgb(170, 47, 47)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon1)

        self.frame_top_layout.addWidget(self.btn_exit)


        self.frame_main_layout.addWidget(self.frame_top)

        self.frame_content = QFrame(self.frame_main)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy3)
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content_layout = QHBoxLayout(self.frame_content)
        self.frame_content_layout.setObjectName(u"frame_content_layout")
        self.frame_content_layout.setContentsMargins(-1, 0, -1, -1)
        self.left_pannel = QFrame(self.frame_content)
        self.left_pannel.setObjectName(u"left_pannel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.left_pannel.sizePolicy().hasHeightForWidth())
        self.left_pannel.setSizePolicy(sizePolicy4)
        self.left_pannel.setMinimumSize(QSize(200, 0))
        self.left_pannel.setMaximumSize(QSize(200, 16777215))
        self.pannel_left_layout = QVBoxLayout(self.left_pannel)
        self.pannel_left_layout.setObjectName(u"pannel_left_layout")
        self.pannel_left_layout.setContentsMargins(-1, 1, -1, -1)
        self.btn_importFile = QPushButton(self.left_pannel)
        self.btn_importFile.setObjectName(u"btn_importFile")

        self.pannel_left_layout.addWidget(self.btn_importFile)

        self.btn_importFolder = QPushButton(self.left_pannel)
        self.btn_importFolder.setObjectName(u"btn_importFolder")

        self.pannel_left_layout.addWidget(self.btn_importFolder)

        self.btn_selectWorkspace = QPushButton(self.left_pannel)
        self.btn_selectWorkspace.setObjectName(u"btn_selectWorkspace")

        self.pannel_left_layout.addWidget(self.btn_selectWorkspace)

        self.label_fileInfo = QLabel(self.left_pannel)
        self.label_fileInfo.setObjectName(u"label_fileInfo")
        sizePolicy1.setHeightForWidth(self.label_fileInfo.sizePolicy().hasHeightForWidth())
        self.label_fileInfo.setSizePolicy(sizePolicy1)
        self.label_fileInfo.setMinimumSize(QSize(0, 80))
        self.label_fileInfo.setStyleSheet(u"border-style: solid;\n"
" border-width: 1px;\n"
"border-color: rgb(130, 135, 144);")
        self.label_fileInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.pannel_left_layout.addWidget(self.label_fileInfo)

        self.treeview_workspace = QTreeView(self.left_pannel)
        self.treeview_workspace.setObjectName(u"treeview_workspace")
        self.treeview_workspace.setAcceptDrops(True)
        self.treeview_workspace.setStyleSheet(u"color: black;")
        self.treeview_workspace.setDragEnabled(True)
        self.treeview_workspace.setDragDropMode(QAbstractItemView.DragOnly)
        self.treeview_workspace.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.pannel_left_layout.addWidget(self.treeview_workspace)


        self.frame_content_layout.addWidget(self.left_pannel)

        self.content_tabs = QStackedWidget(self.frame_content)
        self.content_tabs.setObjectName(u"content_tabs")
        self.content_tabs.setStyleSheet(u"color: black;")
        self.page_plan = QWidget()
        self.page_plan.setObjectName(u"page_plan")
        self.layout_page_plan = QVBoxLayout(self.page_plan)
        self.layout_page_plan.setObjectName(u"layout_page_plan")
        self.pipeline_settings = QFrame(self.page_plan)
        self.pipeline_settings.setObjectName(u"pipeline_settings")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pipeline_settings.sizePolicy().hasHeightForWidth())
        self.pipeline_settings.setSizePolicy(sizePolicy5)
        self.pipeline_settings.setMaximumSize(QSize(16777215, 200))
        self.pipeline_settings.setAcceptDrops(False)
        self.horizontalLayout = QHBoxLayout(self.pipeline_settings)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.pipeline_settings)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy6)
        self.verticalFrame.setMaximumSize(QSize(200, 200))
        self.verticalFrame.setAcceptDrops(False)
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.view_channel = QGraphicsView(self.verticalFrame)
        self.view_channel.setObjectName(u"view_channel")
        sizePolicy6.setHeightForWidth(self.view_channel.sizePolicy().hasHeightForWidth())
        self.view_channel.setSizePolicy(sizePolicy6)
        self.view_channel.setMinimumSize(QSize(0, 0))
        self.view_channel.setMaximumSize(QSize(300, 300))
        self.view_channel.setMouseTracking(True)
        self.view_channel.setAutoFillBackground(True)
        self.view_channel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view_channel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view_channel.setDragMode(QGraphicsView.NoDrag)

        self.verticalLayout_2.addWidget(self.view_channel)

        self.slider_channel = QSlider(self.verticalFrame)
        self.slider_channel.setObjectName(u"slider_channel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.slider_channel.sizePolicy().hasHeightForWidth())
        self.slider_channel.setSizePolicy(sizePolicy7)
        self.slider_channel.setStyleSheet(u"padding: 3px;")
        self.slider_channel.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_channel)


        self.horizontalLayout.addWidget(self.verticalFrame)

        self.list_functions = QListWidget(self.pipeline_settings)
        self.list_functions.setObjectName(u"list_functions")
        self.list_functions.setStyleSheet(u"QToolTip {\n"
"background-color: rgb(246, 255, 220);\n"
"border: 1px solid;\n"
"color: black;\n"
"padding: 0;\n"
"opacity: 130;\n"
"}")

        self.horizontalLayout.addWidget(self.list_functions)

        self.parameters_container = QFrame(self.pipeline_settings)
        self.parameters_container.setObjectName(u"parameters_container")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.parameters_container.sizePolicy().hasHeightForWidth())
        self.parameters_container.setSizePolicy(sizePolicy8)
        self.parameters_container.setMinimumSize(QSize(300, 0))
        self.parameters_container.setStyleSheet(u"color: white;")
        self.parameters_container.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_4 = QVBoxLayout(self.parameters_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.edit_operation_name = QLineEdit(self.parameters_container)
        self.edit_operation_name.setObjectName(u"edit_operation_name")
        self.edit_operation_name.setEnabled(True)
        self.edit_operation_name.setFrame(True)

        self.verticalLayout_4.addWidget(self.edit_operation_name)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.layout_fnames = QVBoxLayout()
        self.layout_fnames.setObjectName(u"layout_fnames")

        self.horizontalLayout_2.addLayout(self.layout_fnames)

        self.layout_fargs = QVBoxLayout()
        self.layout_fargs.setObjectName(u"layout_fargs")

        self.horizontalLayout_2.addLayout(self.layout_fargs)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.btn_modify_operation = QPushButton(self.parameters_container)
        self.btn_modify_operation.setObjectName(u"btn_modify_operation")

        self.verticalLayout_4.addWidget(self.btn_modify_operation)

        self.btn_add_operation = QPushButton(self.parameters_container)
        self.btn_add_operation.setObjectName(u"btn_add_operation")
        self.btn_add_operation.setStyleSheet(u"color: white;")

        self.verticalLayout_4.addWidget(self.btn_add_operation)


        self.horizontalLayout.addWidget(self.parameters_container)


        self.layout_page_plan.addWidget(self.pipeline_settings)

        self.pipeline_content = QFrame(self.page_plan)
        self.pipeline_content.setObjectName(u"pipeline_content")
        self.pipeline_content.setMinimumSize(QSize(0, 100))
        self.verticalLayout = QVBoxLayout(self.pipeline_content)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.operation_list_btns = QFrame(self.pipeline_content)
        self.operation_list_btns.setObjectName(u"operation_list_btns")
        sizePolicy.setHeightForWidth(self.operation_list_btns.sizePolicy().hasHeightForWidth())
        self.operation_list_btns.setSizePolicy(sizePolicy)
        self.operation_list_btns.setMinimumSize(QSize(0, 25))
        self.operation_list_btns.setMaximumSize(QSize(16777215, 40))
        self.operation_list_btns.setStyleSheet(u"color: white;")
        self.layout_operation_list_btns = QHBoxLayout(self.operation_list_btns)
        self.layout_operation_list_btns.setObjectName(u"layout_operation_list_btns")
        self.btn_run_pipeline = QPushButton(self.operation_list_btns)
        self.btn_run_pipeline.setObjectName(u"btn_run_pipeline")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.btn_run_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_run_pipeline.setSizePolicy(sizePolicy9)

        self.layout_operation_list_btns.addWidget(self.btn_run_pipeline)

        self.btn_load_pipeline = QPushButton(self.operation_list_btns)
        self.btn_load_pipeline.setObjectName(u"btn_load_pipeline")
        sizePolicy9.setHeightForWidth(self.btn_load_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_load_pipeline.setSizePolicy(sizePolicy9)

        self.layout_operation_list_btns.addWidget(self.btn_load_pipeline)

        self.btn_save_pipeline = QPushButton(self.operation_list_btns)
        self.btn_save_pipeline.setObjectName(u"btn_save_pipeline")
        sizePolicy9.setHeightForWidth(self.btn_save_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_save_pipeline.setSizePolicy(sizePolicy9)

        self.layout_operation_list_btns.addWidget(self.btn_save_pipeline)

        self.btn_remove_operation = QPushButton(self.operation_list_btns)
        self.btn_remove_operation.setObjectName(u"btn_remove_operation")
        sizePolicy9.setHeightForWidth(self.btn_remove_operation.sizePolicy().hasHeightForWidth())
        self.btn_remove_operation.setSizePolicy(sizePolicy9)

        self.layout_operation_list_btns.addWidget(self.btn_remove_operation)


        self.verticalLayout.addWidget(self.operation_list_btns)

        self.list_operations = QListWidget(self.pipeline_content)
        self.list_operations.setObjectName(u"list_operations")
        self.list_operations.setStyleSheet(u"color: white;")
        self.list_operations.setDragDropMode(QAbstractItemView.InternalMove)

        self.verticalLayout.addWidget(self.list_operations)

        self.edit_pipeline_output = QTextEdit(self.pipeline_content)
        self.edit_pipeline_output.setObjectName(u"edit_pipeline_output")
        self.edit_pipeline_output.setMaximumSize(QSize(16777215, 150))
        self.edit_pipeline_output.setStyleSheet(u"color: black;")
        self.edit_pipeline_output.setUndoRedoEnabled(False)
        self.edit_pipeline_output.setReadOnly(True)

        self.verticalLayout.addWidget(self.edit_pipeline_output)


        self.layout_page_plan.addWidget(self.pipeline_content)

        self.content_tabs.addWidget(self.page_plan)
        self.page_visualize = QWidget()
        self.page_visualize.setObjectName(u"page_visualize")
        self.layout_page_visualize = QVBoxLayout(self.page_visualize)
        self.layout_page_visualize.setObjectName(u"layout_page_visualize")
        self.mainPreview_frame = QFrame(self.page_visualize)
        self.mainPreview_frame.setObjectName(u"mainPreview_frame")
        sizePolicy6.setHeightForWidth(self.mainPreview_frame.sizePolicy().hasHeightForWidth())
        self.mainPreview_frame.setSizePolicy(sizePolicy6)
        self.verticalLayout_3 = QVBoxLayout(self.mainPreview_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mainPreview = QGraphicsView(self.mainPreview_frame)
        self.mainPreview.setObjectName(u"mainPreview")
        sizePolicy6.setHeightForWidth(self.mainPreview.sizePolicy().hasHeightForWidth())
        self.mainPreview.setSizePolicy(sizePolicy6)

        self.verticalLayout_3.addWidget(self.mainPreview)

        self.slide_mainPreview = QSlider(self.mainPreview_frame)
        self.slide_mainPreview.setObjectName(u"slide_mainPreview")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.slide_mainPreview.sizePolicy().hasHeightForWidth())
        self.slide_mainPreview.setSizePolicy(sizePolicy10)
        self.slide_mainPreview.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.slide_mainPreview)


        self.layout_page_visualize.addWidget(self.mainPreview_frame)

        self.content_tabs.addWidget(self.page_visualize)
        self.page_analyse = QWidget()
        self.page_analyse.setObjectName(u"page_analyse")
        self.layout_page_analyse = QVBoxLayout(self.page_analyse)
        self.layout_page_analyse.setObjectName(u"layout_page_analyse")
        self.content_tabs.addWidget(self.page_analyse)

        self.frame_content_layout.addWidget(self.content_tabs)


        self.frame_main_layout.addWidget(self.frame_content)

        self.frame_bottom = QFrame(self.frame_main)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(100, 16))
        self.frame_bottom.setMaximumSize(QSize(16777215, 16))
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.frame_bottom_layout = QHBoxLayout(self.frame_bottom)
        self.frame_bottom_layout.setObjectName(u"frame_bottom_layout")
        self.frame_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.spring_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.frame_bottom_layout.addItem(self.spring_2)

        self.btn_resize_grip = QPushButton(self.frame_bottom)
        self.btn_resize_grip.setObjectName(u"btn_resize_grip")
        sizePolicy6.setHeightForWidth(self.btn_resize_grip.sizePolicy().hasHeightForWidth())
        self.btn_resize_grip.setSizePolicy(sizePolicy6)
        self.btn_resize_grip.setMinimumSize(QSize(16, 16))
        self.btn_resize_grip.setMaximumSize(QSize(16, 16))
        self.btn_resize_grip.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.btn_resize_grip.setFocusPolicy(Qt.NoFocus)
        self.btn_resize_grip.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(222, 222, 222);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-size-grip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_resize_grip.setIcon(icon2)

        self.frame_bottom_layout.addWidget(self.btn_resize_grip)


        self.frame_main_layout.addWidget(self.frame_bottom)


        self.centralwidget_layout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.content_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_plan.setText(QCoreApplication.translate("MainWindow", u"Plan", None))
        self.btn_visualize.setText(QCoreApplication.translate("MainWindow", u"Visualize", None))
        self.btn_analyse.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.btn_minimize.setText("")
        self.btn_exit.setText("")
        self.btn_importFile.setText(QCoreApplication.translate("MainWindow", u"Import File", None))
        self.btn_importFolder.setText(QCoreApplication.translate("MainWindow", u"Import Folder", None))
        self.btn_selectWorkspace.setText(QCoreApplication.translate("MainWindow", u"Select Workspace", None))
        self.label_fileInfo.setText(QCoreApplication.translate("MainWindow", u"File Info", None))
#if QT_CONFIG(tooltip)
        self.list_functions.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edit_operation_name.setInputMask("")
        self.edit_operation_name.setText("")
        self.edit_operation_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Operation name", None))
        self.btn_modify_operation.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.btn_add_operation.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_run_pipeline.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.btn_load_pipeline.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.btn_save_pipeline.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_remove_operation.setText(QCoreApplication.translate("MainWindow", u"Remove operation", None))
        self.btn_resize_grip.setText("")
    # retranslateUi

