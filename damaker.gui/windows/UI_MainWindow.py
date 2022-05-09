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

from  . import files_rc
from  . import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(888, 645)
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
        self.frame_top.setMinimumSize(QSize(100, 30))
        self.frame_top.setMaximumSize(QSize(16777215, 30))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top_layout = QHBoxLayout(self.frame_top)
        self.frame_top_layout.setSpacing(1)
        self.frame_top_layout.setObjectName(u"frame_top_layout")
        self.frame_top_layout.setContentsMargins(0, 0, 0, 0)
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
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy)
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content_layout = QHBoxLayout(self.frame_content)
        self.frame_content_layout.setObjectName(u"frame_content_layout")
        self.left_pannel = QFrame(self.frame_content)
        self.left_pannel.setObjectName(u"left_pannel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_pannel.sizePolicy().hasHeightForWidth())
        self.left_pannel.setSizePolicy(sizePolicy1)
        self.left_pannel.setMinimumSize(QSize(200, 0))
        self.left_pannel.setMaximumSize(QSize(200, 16777215))
        self.pannel_left_layout = QVBoxLayout(self.left_pannel)
        self.pannel_left_layout.setObjectName(u"pannel_left_layout")
        self.pushButton = QPushButton(self.left_pannel)
        self.pushButton.setObjectName(u"pushButton")

        self.pannel_left_layout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.left_pannel)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.pannel_left_layout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.left_pannel)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.pannel_left_layout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.left_pannel)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.pannel_left_layout.addWidget(self.pushButton_4)

        self.label = QLabel(self.left_pannel)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 80))
        self.label.setStyleSheet(u"border-style: solid;\n"
" border-width: 1px;\n"
"border-color: rgb(130, 135, 144);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.pannel_left_layout.addWidget(self.label)

        self.treeview_workspace = QTreeView(self.left_pannel)
        self.treeview_workspace.setObjectName(u"treeview_workspace")
        self.treeview_workspace.setStyleSheet(u"color: black;")

        self.pannel_left_layout.addWidget(self.treeview_workspace)


        self.frame_content_layout.addWidget(self.left_pannel)

        self.content_tabs = QTabWidget(self.frame_content)
        self.content_tabs.setObjectName(u"content_tabs")
        self.content_tabs.setStyleSheet(u"color: black;")
        self.content_tabs.setTabShape(QTabWidget.Rounded)
        self.content_tabs.setElideMode(Qt.ElideNone)
        self.content_tabs.setUsesScrollButtons(False)
        self.content_tabs.setDocumentMode(True)
        self.tab_plan = QWidget()
        self.tab_plan.setObjectName(u"tab_plan")
        self.tab_plan.setAutoFillBackground(False)
        self.tab_plan_layout = QVBoxLayout(self.tab_plan)
        self.tab_plan_layout.setObjectName(u"tab_plan_layout")
        self.pipeline_settings = QFrame(self.tab_plan)
        self.pipeline_settings.setObjectName(u"pipeline_settings")
        self.horizontalLayout = QHBoxLayout(self.pipeline_settings)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalFrame = QFrame(self.pipeline_settings)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView = QGraphicsView(self.verticalFrame)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy3.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.horizontalSlider = QSlider(self.verticalFrame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)


        self.horizontalLayout.addWidget(self.verticalFrame)


        self.tab_plan_layout.addWidget(self.pipeline_settings)

        self.pipeline_content = QFrame(self.tab_plan)
        self.pipeline_content.setObjectName(u"pipeline_content")
        self.verticalLayout = QVBoxLayout(self.pipeline_content)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.tab_plan_layout.addWidget(self.pipeline_content)

        self.content_tabs.addTab(self.tab_plan, "")
        self.tab_visualize = QWidget()
        self.tab_visualize.setObjectName(u"tab_visualize")
        self.content_tabs.addTab(self.tab_visualize, "")
        self.tab_analyse = QWidget()
        self.tab_analyse.setObjectName(u"tab_analyse")
        self.content_tabs.addTab(self.tab_analyse, "")

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_resize_grip.sizePolicy().hasHeightForWidth())
        self.btn_resize_grip.setSizePolicy(sizePolicy4)
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
        self.btn_minimize.setText("")
        self.btn_exit.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Import File", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Import Folder", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Create Workspace", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Select Workspace", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File Info", None))
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.tab_plan), QCoreApplication.translate("MainWindow", u"Plan", None))
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.tab_visualize), QCoreApplication.translate("MainWindow", u"Visualize", None))
        self.content_tabs.setTabText(self.content_tabs.indexOf(self.tab_analyse), QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.btn_resize_grip.setText("")
    # retranslateUi

