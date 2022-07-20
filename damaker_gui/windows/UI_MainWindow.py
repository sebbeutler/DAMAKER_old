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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1091, 855)
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
        self.actiontest1 = QAction(MainWindow)
        self.actiontest1.setObjectName(u"actiontest1")
        self.actiontest = QAction(MainWindow)
        self.actiontest.setObjectName(u"actiontest")
        self.actiontest_2 = QAction(MainWindow)
        self.actiontest_2.setObjectName(u"actiontest_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"color: rgb(210, 210, 210);background: transparent;")
        self.centralwidget_layout = QHBoxLayout(self.centralwidget)
        self.centralwidget_layout.setSpacing(0)
        self.centralwidget_layout.setObjectName(u"centralwidget_layout")
        self.centralwidget_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setMinimumSize(QSize(0, 0))
        self.frame_main.setMaximumSize(QSize(16777215, 16777215))
        self.frame_main.setStyleSheet(u"* {\n"
"	outline: 0;\n"
"}\n"
"\n"
"#frame_main {\n"
"	\n"
"	background-color: rgb(72, 75, 75);\n"
"\n"
"	/* border-radius: 2px;\n"
"	border: 1px solid rgb(35, 31, 32);*/\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 0px solid rgb(35, 31, 32);\n"
"}\n"
"\n"
"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 2px;\n"
"	border: 1px solid rgb(27, 29, 35);\n"
"	padding-left: 1px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 1px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 0px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(72, 75, 75);\n"
"    height: 14px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(35, 31, 32);\n"
"    min-width: 20px;\n"
"	border-radius: 1px\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(72, 75, 75);\n"
"    width: 14px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(35, 31, 32);\n"
"    min-h"
                        "eight: 25px;\n"
"	border-radius: 1px\n"
" }\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    width: 0px;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"     height: 0px;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    height: 0px;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border:1px solid rgb(35, 31, 32);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(35, 31, 32);\n"
"}\n"
"QCheckBo"
                        "x::indicator:hover {\n"
"    border: 1px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 1px solid rgb(35, 31, 32);\n"
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
"	border-radius: 2px;\n"
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
"	width: 25px"
                        "; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 1px;\n"
"	border-bottom-right-radius: 1px;	\n"
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
"    border-radius: 4px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(72, 75, 75);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(35, 31, 32);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 2px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(42, 42, 42);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radiu"
                        "s: 9px;\n"
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
"}\n"
"\n"
"/* PUSH BUTTON */\n"
"QPushButton {\n"
"	border: 1px solid rgb(35, 31, 32);\n"
"	border-radius: 1px;	\n"
"	background-color: rgb(72, 75, 75);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(118, 118, 118);\n"
"	border: 1px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(72, 75, 75);\n"
"	border: 1px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* SPIN BOX */\n"
"QSpinBox, QDoubleSpinBox {\n"
"	background-color: rgb(35, 31, 32);\n"
"	\n"
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
        self.frame_top.setMinimumSize(QSize(100, 20))
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top_layout = QHBoxLayout(self.frame_top)
        self.frame_top_layout.setSpacing(0)
        self.frame_top_layout.setObjectName(u"frame_top_layout")
        self.frame_top_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_pageSelect = QFrame(self.frame_top)
        self.frame_pageSelect.setObjectName(u"frame_pageSelect")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_pageSelect.sizePolicy().hasHeightForWidth())
        self.frame_pageSelect.setSizePolicy(sizePolicy1)
        self.frame_pageSelect.setMinimumSize(QSize(189, 0))
        self.frame_pageSelect.setStyleSheet(u"QPushButton {\n"
"	border-width: 0px;\n"
"	background-color: rgb(35, 31, 32);\n"
"}\n"
"QPushButton:checked {\n"
"	\n"
"	background-color: rgb(106, 106, 106);\n"
"}")
        self.layout_pageSelect = QHBoxLayout(self.frame_pageSelect)
        self.layout_pageSelect.setSpacing(0)
        self.layout_pageSelect.setObjectName(u"layout_pageSelect")
        self.layout_pageSelect.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_pageSelect)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setPixmap(QPixmap(u":/20x20/icons/20x20/logo_dmkr.png"))

        self.layout_pageSelect.addWidget(self.label)

        self.btn_plan = QPushButton(self.frame_pageSelect)
        self.btn_plan.setObjectName(u"btn_plan")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_plan.sizePolicy().hasHeightForWidth())
        self.btn_plan.setSizePolicy(sizePolicy3)
        self.btn_plan.setStyleSheet(u"QPushButton {\n"
"	border-width: 1px 0px 0px 0px;\n"
"}")
        self.btn_plan.setCheckable(True)

        self.layout_pageSelect.addWidget(self.btn_plan)

        self.btn_visualize = QPushButton(self.frame_pageSelect)
        self.btn_visualize.setObjectName(u"btn_visualize")
        sizePolicy3.setHeightForWidth(self.btn_visualize.sizePolicy().hasHeightForWidth())
        self.btn_visualize.setSizePolicy(sizePolicy3)
        self.btn_visualize.setStyleSheet(u"")
        self.btn_visualize.setCheckable(True)

        self.layout_pageSelect.addWidget(self.btn_visualize)

        self.btn_analyse = QPushButton(self.frame_pageSelect)
        self.btn_analyse.setObjectName(u"btn_analyse")
        sizePolicy3.setHeightForWidth(self.btn_analyse.sizePolicy().hasHeightForWidth())
        self.btn_analyse.setSizePolicy(sizePolicy3)
        self.btn_analyse.setMinimumSize(QSize(0, 0))
        self.btn_analyse.setMaximumSize(QSize(16777215, 16777215))
        self.btn_analyse.setCheckable(True)

        self.layout_pageSelect.addWidget(self.btn_analyse)


        self.frame_top_layout.addWidget(self.frame_pageSelect)

        self.spring = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.frame_top_layout.addItem(self.spring)

        self.btn_minimize = QPushButton(self.frame_top)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(15, 20))
        self.btn_minimize.setMaximumSize(QSize(60, 60))
        self.btn_minimize.setFocusPolicy(Qt.NoFocus)
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border-radius: 2px;\n"
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
        icon.addFile(u":/16x16/icons/16x16/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.frame_top_layout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_top)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy4)
        self.btn_maximize.setMinimumSize(QSize(15, 20))
        self.btn_maximize.setMaximumSize(QSize(60, 60))
        self.btn_maximize.setFocusPolicy(Qt.NoFocus)
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border-radius: 2px;\n"
"	\n"
"	background-color: rgba(104, 104, 124, 125);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(212, 212, 212, 40);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon1)

        self.frame_top_layout.addWidget(self.btn_maximize)

        self.btn_exit = QPushButton(self.frame_top)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(15, 20))
        self.btn_exit.setMaximumSize(QSize(60, 60))
        self.btn_exit.setFocusPolicy(Qt.NoFocus)
        self.btn_exit.setStyleSheet(u"#btn_exit {\n"
"	border-radius: 2px;\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon2)

        self.frame_top_layout.addWidget(self.btn_exit)


        self.frame_main_layout.addWidget(self.frame_top)

        self.frame_content = QFrame(self.frame_main)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy5)
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content_layout = QHBoxLayout(self.frame_content)
        self.frame_content_layout.setSpacing(0)
        self.frame_content_layout.setObjectName(u"frame_content_layout")
        self.frame_content_layout.setContentsMargins(0, 0, 0, 0)
        self.left_pannel = QFrame(self.frame_content)
        self.left_pannel.setObjectName(u"left_pannel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.left_pannel.sizePolicy().hasHeightForWidth())
        self.left_pannel.setSizePolicy(sizePolicy6)
        self.left_pannel.setMinimumSize(QSize(200, 0))
        self.left_pannel.setMaximumSize(QSize(200, 16777215))
        self.pannel_left_layout = QVBoxLayout(self.left_pannel)
        self.pannel_left_layout.setSpacing(0)
        self.pannel_left_layout.setObjectName(u"pannel_left_layout")
        self.pannel_left_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_importFile = QPushButton(self.left_pannel)
        self.btn_importFile.setObjectName(u"btn_importFile")
        self.btn_importFile.setStyleSheet(u"border-width: 1px 1px 0px 1px;")

        self.pannel_left_layout.addWidget(self.btn_importFile)

        self.btn_importFolder = QPushButton(self.left_pannel)
        self.btn_importFolder.setObjectName(u"btn_importFolder")
        self.btn_importFolder.setStyleSheet(u"border-width: 1px 1px 0px 1px;")

        self.pannel_left_layout.addWidget(self.btn_importFolder)

        self.btn_selectWorkspace = QPushButton(self.left_pannel)
        self.btn_selectWorkspace.setObjectName(u"btn_selectWorkspace")
        self.btn_selectWorkspace.setStyleSheet(u"border-width: 1px 1px 0px 1px;")

        self.pannel_left_layout.addWidget(self.btn_selectWorkspace)

        self.label_fileInfo = QLabel(self.left_pannel)
        self.label_fileInfo.setObjectName(u"label_fileInfo")
        sizePolicy1.setHeightForWidth(self.label_fileInfo.sizePolicy().hasHeightForWidth())
        self.label_fileInfo.setSizePolicy(sizePolicy1)
        self.label_fileInfo.setMinimumSize(QSize(0, 80))
        self.label_fileInfo.setStyleSheet(u"border-style: solid;\n"
" border-width: 1px;\n"
"border-color: #202020;")
        self.label_fileInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.pannel_left_layout.addWidget(self.label_fileInfo)

        self.treeview_workspace = QTreeView(self.left_pannel)
        self.treeview_workspace.setObjectName(u"treeview_workspace")
        self.treeview_workspace.setAcceptDrops(True)
        self.treeview_workspace.setStyleSheet(u"")
        self.treeview_workspace.setDragEnabled(True)
        self.treeview_workspace.setDragDropMode(QAbstractItemView.DragOnly)
        self.treeview_workspace.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.treeview_workspace.setIndentation(15)
        self.treeview_workspace.setWordWrap(True)
        self.treeview_workspace.header().setVisible(False)

        self.pannel_left_layout.addWidget(self.treeview_workspace)


        self.frame_content_layout.addWidget(self.left_pannel)

        self.content_tabs = QStackedWidget(self.frame_content)
        self.content_tabs.setObjectName(u"content_tabs")
        self.content_tabs.setStyleSheet(u"")
        self.page_plan = QWidget()
        self.page_plan.setObjectName(u"page_plan")
        self.page_plan.setStyleSheet(u"")
        self.layout_page_plan = QVBoxLayout(self.page_plan)
        self.layout_page_plan.setSpacing(0)
        self.layout_page_plan.setObjectName(u"layout_page_plan")
        self.layout_page_plan.setContentsMargins(0, 0, 0, 0)
        self.pipeline_settings = QFrame(self.page_plan)
        self.pipeline_settings.setObjectName(u"pipeline_settings")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pipeline_settings.sizePolicy().hasHeightForWidth())
        self.pipeline_settings.setSizePolicy(sizePolicy7)
        self.pipeline_settings.setMinimumSize(QSize(0, 200))
        self.pipeline_settings.setMaximumSize(QSize(16777215, 230))
        self.pipeline_settings.setAcceptDrops(False)
        self.pipeline_settings_layout = QHBoxLayout(self.pipeline_settings)
        self.pipeline_settings_layout.setSpacing(0)
        self.pipeline_settings_layout.setObjectName(u"pipeline_settings_layout")
        self.pipeline_settings_layout.setContentsMargins(0, 0, 0, 0)
        self.previewPipeline = QFrame(self.pipeline_settings)
        self.previewPipeline.setObjectName(u"previewPipeline")
        self.previewPipeline.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.previewPipeline.sizePolicy().hasHeightForWidth())
        self.previewPipeline.setSizePolicy(sizePolicy2)
        self.previewPipeline.setMinimumSize(QSize(200, 200))
        self.previewPipeline.setMaximumSize(QSize(300, 300))
        self.previewPipeline.setAcceptDrops(False)
        self.previewPipeline.setStyleSheet(u"border-width: 1px;")
        self.verticalLayout_2 = QVBoxLayout(self.previewPipeline)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plan_preview = QFrame(self.previewPipeline)
        self.plan_preview.setObjectName(u"plan_preview")
        self.plan_preview.setFrameShape(QFrame.StyledPanel)
        self.plan_preview.setFrameShadow(QFrame.Raised)
        self.plan_layout_preview = QVBoxLayout(self.plan_preview)
        self.plan_layout_preview.setSpacing(0)
        self.plan_layout_preview.setObjectName(u"plan_layout_preview")
        self.plan_layout_preview.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.plan_preview)

        self.previewPipelineSlider = QSlider(self.previewPipeline)
        self.previewPipelineSlider.setObjectName(u"previewPipelineSlider")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.previewPipelineSlider.sizePolicy().hasHeightForWidth())
        self.previewPipelineSlider.setSizePolicy(sizePolicy8)
        self.previewPipelineSlider.setStyleSheet(u"padding: 0px;")
        self.previewPipelineSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.previewPipelineSlider)


        self.pipeline_settings_layout.addWidget(self.previewPipeline)

        self.functions_frame = QFrame(self.pipeline_settings)
        self.functions_frame.setObjectName(u"functions_frame")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.functions_frame.sizePolicy().hasHeightForWidth())
        self.functions_frame.setSizePolicy(sizePolicy9)
        self.functions_frame.setMinimumSize(QSize(250, 0))
        self.functions_frame.setStyleSheet(u"#functions_frame {\n"
"	border-width: 1px 0px 1px 0px;\n"
"	color: white;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: rgb(49,49,49);\n"
"    color: rgb(255,255,255);\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: rgb(42,42,42);\n"
"	padding: 0 100 0 15px;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMenuBar::item::selected {\n"
"    background-color: rgb(30,30,30);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(62,62,62);\n"
"    color: rgb(255,255,255);\n"
"    border: 1px solid #000;           \n"
"}\n"
"\n"
"QMenu::item::selected {\n"
"    background-color: rgb(30,30,30);\n"
"}")
        self.functions_layout = QVBoxLayout(self.functions_frame)
        self.functions_layout.setSpacing(0)
        self.functions_layout.setObjectName(u"functions_layout")
        self.functions_layout.setContentsMargins(0, 0, 0, 0)

        self.pipeline_settings_layout.addWidget(self.functions_frame)


        self.layout_page_plan.addWidget(self.pipeline_settings)

        self.pipeline_content = QFrame(self.page_plan)
        self.pipeline_content.setObjectName(u"pipeline_content")
        self.pipeline_content.setMinimumSize(QSize(0, 100))
        self.pipeline_content.setStyleSheet(u"border-width: 0px 0px 0px 1px;")
        self.verticalLayout = QVBoxLayout(self.pipeline_content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.list_operations = QListWidget(self.pipeline_content)
        self.list_operations.setObjectName(u"list_operations")
        self.list_operations.setStyleSheet(u"color: rgb(218, 218, 218);\n"
"border-width: 1px 0px 0px 0px;")
        self.list_operations.setDragDropMode(QAbstractItemView.InternalMove)

        self.verticalLayout.addWidget(self.list_operations)

        self.operation_list_btns = QFrame(self.pipeline_content)
        self.operation_list_btns.setObjectName(u"operation_list_btns")
        sizePolicy.setHeightForWidth(self.operation_list_btns.sizePolicy().hasHeightForWidth())
        self.operation_list_btns.setSizePolicy(sizePolicy)
        self.operation_list_btns.setMinimumSize(QSize(0, 25))
        self.operation_list_btns.setMaximumSize(QSize(16777215, 40))
        self.operation_list_btns.setStyleSheet(u"color: white;border-width: 1px 0px 0px 0px;")
        self.layout_operation_list_btns = QHBoxLayout(self.operation_list_btns)
        self.layout_operation_list_btns.setSpacing(0)
        self.layout_operation_list_btns.setObjectName(u"layout_operation_list_btns")
        self.layout_operation_list_btns.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_operation_list_btns.addItem(self.horizontalSpacer)

        self.btn_run_pipeline = QPushButton(self.operation_list_btns)
        self.btn_run_pipeline.setObjectName(u"btn_run_pipeline")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.btn_run_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_run_pipeline.setSizePolicy(sizePolicy10)
        self.btn_run_pipeline.setStyleSheet(u"border: 1px solid rgb(125, 125, 125);")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_run_pipeline.setIcon(icon3)
        self.btn_run_pipeline.setIconSize(QSize(16, 16))

        self.layout_operation_list_btns.addWidget(self.btn_run_pipeline)

        self.btn_save_pipeline = QPushButton(self.operation_list_btns)
        self.btn_save_pipeline.setObjectName(u"btn_save_pipeline")
        sizePolicy10.setHeightForWidth(self.btn_save_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_save_pipeline.setSizePolicy(sizePolicy10)
        self.btn_save_pipeline.setStyleSheet(u"border: 1px solid rgb(125, 125, 125);")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_pipeline.setIcon(icon4)

        self.layout_operation_list_btns.addWidget(self.btn_save_pipeline)

        self.btn_load_pipeline = QPushButton(self.operation_list_btns)
        self.btn_load_pipeline.setObjectName(u"btn_load_pipeline")
        sizePolicy10.setHeightForWidth(self.btn_load_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_load_pipeline.setSizePolicy(sizePolicy10)
        self.btn_load_pipeline.setStyleSheet(u"border: 1px solid rgb(125, 125, 125);\n"
"padding: 3px;")

        self.layout_operation_list_btns.addWidget(self.btn_load_pipeline)

        self.btn_remove_operation = QPushButton(self.operation_list_btns)
        self.btn_remove_operation.setObjectName(u"btn_remove_operation")
        sizePolicy10.setHeightForWidth(self.btn_remove_operation.sizePolicy().hasHeightForWidth())
        self.btn_remove_operation.setSizePolicy(sizePolicy10)
        self.btn_remove_operation.setStyleSheet(u"border: 1px solid rgb(125, 125, 125);\n"
"padding: 3px;")

        self.layout_operation_list_btns.addWidget(self.btn_remove_operation)


        self.verticalLayout.addWidget(self.operation_list_btns)

        self.edit_pipeline_output = QTextEdit(self.pipeline_content)
        self.edit_pipeline_output.setObjectName(u"edit_pipeline_output")
        self.edit_pipeline_output.setMaximumSize(QSize(16777215, 150))
        self.edit_pipeline_output.setStyleSheet(u"QTextEdit {\n"
"    color: rgb(193, 193, 168);\n"
"	background-color: rgb(35, 31, 32);\n"
"	border-width: 0px 1px 0px 1px;\n"
"}")
        self.edit_pipeline_output.setUndoRedoEnabled(False)
        self.edit_pipeline_output.setReadOnly(True)
        self.edit_pipeline_output.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.edit_pipeline_output)


        self.layout_page_plan.addWidget(self.pipeline_content)

        self.content_tabs.addWidget(self.page_plan)
        self.page_visualize = QWidget()
        self.page_visualize.setObjectName(u"page_visualize")
        self.layout_page_visualize = QHBoxLayout(self.page_visualize)
        self.layout_page_visualize.setSpacing(0)
        self.layout_page_visualize.setObjectName(u"layout_page_visualize")
        self.layout_page_visualize.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.visualize_preview_verticalframe = QFrame(self.page_visualize)
        self.visualize_preview_verticalframe.setObjectName(u"visualize_preview_verticalframe")
        self.verticalLayout_3 = QVBoxLayout(self.visualize_preview_verticalframe)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.visualize_preview_verticalframe)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget_2.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(72, 75, 75);\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"    border: 1px solid black;\n"
"}\n"
"QTabWidget::pane { border: 0; }\n"
"\n"
"QTabBar {\n"
"  background-color: rgb(72, 75, 75);\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"   border: 1px solid black;\n"
"  background-color: rgb(72, 75, 75);\n"
"}\n"
"\n"
"QTabBar::pane {\n"
"  border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  color: lightgray;\n"
"  background-color: rgb(72, 75, 75);\n"
"  border: 0px solid black; \n"
"padding: 4px;\n"
"} \n"
"\n"
"QTabBar::tab:hover {\n"
"  background-color: rgb(52, 52, 52);\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background-color: rgb(42, 42, 42);\n"
"  margin-bottom: -1px; \n"
"}")
        self.tabWidget_2.setTabPosition(QTabWidget.North)
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tab_2D = QWidget()
        self.tab_2D.setObjectName(u"tab_2D")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2D)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_mainPreview = QFrame(self.tab_2D)
        self.frame_mainPreview.setObjectName(u"frame_mainPreview")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_mainPreview.sizePolicy().hasHeightForWidth())
        self.frame_mainPreview.setSizePolicy(sizePolicy11)
        self.frame_mainPreview.setMinimumSize(QSize(0, 400))
        self.frame_mainPreview.setAcceptDrops(True)
        self.frame_mainPreview.setStyleSheet(u"QFrame#frame_mainPreview {\n"
"background-color: rgb(35, 31, 32);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        self.layout_mainPreview = QVBoxLayout(self.frame_mainPreview)
        self.layout_mainPreview.setSpacing(0)
        self.layout_mainPreview.setObjectName(u"layout_mainPreview")
        self.layout_mainPreview.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_mainPreview)

        self.tabWidget_2.addTab(self.tab_2D, "")
        self.tab_3D = QWidget()
        self.tab_3D.setObjectName(u"tab_3D")
        self.tab_3D.setStyleSheet(u"QFrame#frame_mainPreview {\n"
"background-color: rgb(35, 31, 32);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        self.layout_tap_preview3D = QVBoxLayout(self.tab_3D)
        self.layout_tap_preview3D.setSpacing(0)
        self.layout_tap_preview3D.setObjectName(u"layout_tap_preview3D")
        self.layout_tap_preview3D.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2.addTab(self.tab_3D, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)

        self.slider_frame = QSlider(self.visualize_preview_verticalframe)
        self.slider_frame.setObjectName(u"slider_frame")
        self.slider_frame.setStyleSheet(u"border: 1px solid black;")
        self.slider_frame.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.slider_frame)

        self.slider_timepoint = QSlider(self.visualize_preview_verticalframe)
        self.slider_timepoint.setObjectName(u"slider_timepoint")
        self.slider_timepoint.setStyleSheet(u"border: 1px solid black;\n"
"border-width: 0px 1px 1px 1px;")
        self.slider_timepoint.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.slider_timepoint)

        self.channelList_frame = QFrame(self.visualize_preview_verticalframe)
        self.channelList_frame.setObjectName(u"channelList_frame")
        self.channelList_frame.setMinimumSize(QSize(0, 20))
        self.channelList_frame.setStyleSheet(u"QFrame {\n"
"	border: 1px solid black;\n"
"	border-width: 0px 1px 1px 1px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"	border: 1px solid rgb(52, 59, 72);\n"
"	border-radius: 2px;	\n"
"	background-color: ;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 1px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 1px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(83, 168, 89);\n"
"}\n"
"\n"
"QPushButton:unchecked {\n"
"	background-color: rgb(85, 85, 127);\n"
"}")
        self.channelList_layout = QHBoxLayout(self.channelList_frame)
        self.channelList_layout.setSpacing(0)
        self.channelList_layout.setObjectName(u"channelList_layout")
        self.channelList_layout.setContentsMargins(0, 0, 0, 0)
        self.visualize_layout_channelList = QHBoxLayout()
        self.visualize_layout_channelList.setSpacing(0)
        self.visualize_layout_channelList.setObjectName(u"visualize_layout_channelList")

        self.channelList_layout.addLayout(self.visualize_layout_channelList)

        self.visualize_addChannel = QHBoxLayout()
        self.visualize_addChannel.setSpacing(0)
        self.visualize_addChannel.setObjectName(u"visualize_addChannel")
        self.visualize_btn_addChannel = QPushButton(self.channelList_frame)
        self.visualize_btn_addChannel.setObjectName(u"visualize_btn_addChannel")
        sizePolicy2.setHeightForWidth(self.visualize_btn_addChannel.sizePolicy().hasHeightForWidth())
        self.visualize_btn_addChannel.setSizePolicy(sizePolicy2)
        self.visualize_btn_addChannel.setStyleSheet(u"border: 1px solid black;")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.visualize_btn_addChannel.setIcon(icon5)

        self.visualize_addChannel.addWidget(self.visualize_btn_addChannel)

        self.visualize_space_addChannel = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.visualize_addChannel.addItem(self.visualize_space_addChannel)


        self.channelList_layout.addLayout(self.visualize_addChannel)


        self.verticalLayout_3.addWidget(self.channelList_frame)


        self.verticalLayout_7.addWidget(self.visualize_preview_verticalframe)

        self.visualize_functionListFrame = QFrame(self.page_visualize)
        self.visualize_functionListFrame.setObjectName(u"visualize_functionListFrame")
        self.visualize_functionListFrame.setMinimumSize(QSize(0, 200))
        self.visualize_functionListFrame.setMaximumSize(QSize(16777215, 200))
        self.visualize_functionListLayout = QHBoxLayout(self.visualize_functionListFrame)
        self.visualize_functionListLayout.setSpacing(0)
        self.visualize_functionListLayout.setObjectName(u"visualize_functionListLayout")
        self.visualize_functionListLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.visualize_functionListFrame)


        self.layout_page_visualize.addLayout(self.verticalLayout_7)

        self.visualize_leftpanel = QFrame(self.page_visualize)
        self.visualize_leftpanel.setObjectName(u"visualize_leftpanel")
        self.visualize_leftpanel.setMaximumSize(QSize(350, 16777215))
        self.visualize_leftpanel.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(72, 75, 75);\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"    border: 1px solid black;\n"
"}\n"
"QTabWidget::pane { border: 0; }\n"
"\n"
"QTabBar {\n"
"  background-color: rgb(72, 75, 75);\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"   border: 1px solid black;\n"
"  background-color: rgb(72, 75, 75);\n"
"}\n"
"\n"
"QTabBar::pane {\n"
"  border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  color: lightgray;\n"
"  background-color: rgb(72, 75, 75);\n"
"  border: 0px solid black; \n"
"padding: 4px;\n"
"} \n"
"\n"
"QTabBar::tab:hover {\n"
"  background-color: rgb(52, 52, 52);\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background-color: rgb(42, 42, 42);\n"
"  margin-bottom: -1px; \n"
"}")
        self.visualize_leftpanel.setFrameShape(QFrame.StyledPanel)
        self.visualize_leftpanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.visualize_leftpanel)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.visualize_altPreviewsTabs = QTabWidget(self.visualize_leftpanel)
        self.visualize_altPreviewsTabs.setObjectName(u"visualize_altPreviewsTabs")
        self.visualize_altPreviewsTabs.setTabPosition(QTabWidget.North)
        self.visualize_tab_orthogonalPreviews = QWidget()
        self.visualize_tab_orthogonalPreviews.setObjectName(u"visualize_tab_orthogonalPreviews")
        self.verticalLayout_4 = QVBoxLayout(self.visualize_tab_orthogonalPreviews)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topPreview = QFrame(self.visualize_tab_orthogonalPreviews)
        self.topPreview.setObjectName(u"topPreview")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.topPreview.sizePolicy().hasHeightForWidth())
        self.topPreview.setSizePolicy(sizePolicy12)
        self.topPreview.setMinimumSize(QSize(200, 0))
        self.topPreview.setStyleSheet(u"QFrame#topPreview {\n"
"background-color: rgb(35, 31, 32);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")
        self.layout_topPreview = QVBoxLayout(self.topPreview)
        self.layout_topPreview.setSpacing(0)
        self.layout_topPreview.setObjectName(u"layout_topPreview")
        self.layout_topPreview.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.topPreview)

        self.leftPreview = QFrame(self.visualize_tab_orthogonalPreviews)
        self.leftPreview.setObjectName(u"leftPreview")
        sizePolicy12.setHeightForWidth(self.leftPreview.sizePolicy().hasHeightForWidth())
        self.leftPreview.setSizePolicy(sizePolicy12)
        self.leftPreview.setMinimumSize(QSize(200, 0))
        self.leftPreview.setStyleSheet(u"QFrame#leftPreview {\n"
"background-color: rgb(35, 31, 32);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"border-width:  0px 1px 1px 1px ;\n"
"}")
        self.layout_leftPreview = QVBoxLayout(self.leftPreview)
        self.layout_leftPreview.setSpacing(0)
        self.layout_leftPreview.setObjectName(u"layout_leftPreview")
        self.layout_leftPreview.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.leftPreview)

        self.visualize_altPreviewsTabs.addTab(self.visualize_tab_orthogonalPreviews, "")
        self.visualize_tab_annexes = QWidget()
        self.visualize_tab_annexes.setObjectName(u"visualize_tab_annexes")
        self.horizontalLayout = QHBoxLayout(self.visualize_tab_annexes)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.visualize_annexesTabs = QTabWidget(self.visualize_tab_annexes)
        self.visualize_annexesTabs.setObjectName(u"visualize_annexesTabs")
        self.visualize_annexesTabs.setTabPosition(QTabWidget.East)

        self.horizontalLayout.addWidget(self.visualize_annexesTabs)

        self.visualize_altPreviewsTabs.addTab(self.visualize_tab_annexes, "")

        self.verticalLayout_6.addWidget(self.visualize_altPreviewsTabs)

        self.tabWidget = QTabWidget(self.visualize_leftpanel)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy13)
        self.tabWidget.setMinimumSize(QSize(0, 200))
        self.tabWidget.setBaseSize(QSize(0, 330))
        self.tabWidget.setStyleSheet(u"")
        self.tab_views = QWidget()
        self.tab_views.setObjectName(u"tab_views")
        self.tab_views_layout = QVBoxLayout(self.tab_views)
        self.tab_views_layout.setSpacing(3)
        self.tab_views_layout.setObjectName(u"tab_views_layout")
        self.tab_views_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.tab_views_addBtn = QPushButton(self.tab_views)
        self.tab_views_addBtn.setObjectName(u"tab_views_addBtn")

        self.horizontalLayout_2.addWidget(self.tab_views_addBtn)


        self.tab_views_layout.addLayout(self.horizontalLayout_2)

        self.visualize_viewsList = QListWidget(self.tab_views)
        self.visualize_viewsList.setObjectName(u"visualize_viewsList")

        self.tab_views_layout.addWidget(self.visualize_viewsList)

        self.tabWidget.addTab(self.tab_views, "")
        self.tab_brightnesscontrast = QWidget()
        self.tab_brightnesscontrast.setObjectName(u"tab_brightnesscontrast")
        self.tab_brightnesscontrast.setStyleSheet(u"QSlider {\n"
"	border: 1px solid rgb(20, 20, 20);\n"
"    padding: 2px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QSlider::handle {\n"
"    background-color: rgb(35, 31, 32);\n"
"    border: none;\n"
"    height: 5px;\n"
"    width: 20px;\n"
"    margin: 0px;\n"
"	border-radius: 2px;\n"
"}")
        self.tab_brightnesscontrast_layout = QVBoxLayout(self.tab_brightnesscontrast)
        self.tab_brightnesscontrast_layout.setSpacing(10)
        self.tab_brightnesscontrast_layout.setObjectName(u"tab_brightnesscontrast_layout")
        self.tab_brightnesscontrast_layout.setContentsMargins(20, 0, 20, 0)
        self.bc_frame_minmax = QFrame(self.tab_brightnesscontrast)
        self.bc_frame_minmax.setObjectName(u"bc_frame_minmax")
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.bc_frame_minmax.sizePolicy().hasHeightForWidth())
        self.bc_frame_minmax.setSizePolicy(sizePolicy14)
        self.horizontalLayout_5 = QHBoxLayout(self.bc_frame_minmax)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bc_min_label = QLabel(self.bc_frame_minmax)
        self.bc_min_label.setObjectName(u"bc_min_label")

        self.horizontalLayout_5.addWidget(self.bc_min_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.bc_max_label = QLabel(self.bc_frame_minmax)
        self.bc_max_label.setObjectName(u"bc_max_label")

        self.horizontalLayout_5.addWidget(self.bc_max_label)


        self.tab_brightnesscontrast_layout.addWidget(self.bc_frame_minmax)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.tab_brightnesscontrast)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.slider_bc_min = QSlider(self.tab_brightnesscontrast)
        self.slider_bc_min.setObjectName(u"slider_bc_min")
        self.slider_bc_min.setMaximumSize(QSize(16777215, 20))
        self.slider_bc_min.setMaximum(255)
        self.slider_bc_min.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.slider_bc_min)

        self.label_3 = QLabel(self.tab_brightnesscontrast)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.slider_bc_max = QSlider(self.tab_brightnesscontrast)
        self.slider_bc_max.setObjectName(u"slider_bc_max")
        self.slider_bc_max.setMaximum(255)
        self.slider_bc_max.setValue(255)
        self.slider_bc_max.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.slider_bc_max)

        self.label_4 = QLabel(self.tab_brightnesscontrast)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.slider_brightness = QSlider(self.tab_brightnesscontrast)
        self.slider_brightness.setObjectName(u"slider_brightness")
        self.slider_brightness.setMinimum(-127)
        self.slider_brightness.setMaximum(127)
        self.slider_brightness.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.slider_brightness)

        self.label_5 = QLabel(self.tab_brightnesscontrast)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.slider_contrast = QSlider(self.tab_brightnesscontrast)
        self.slider_contrast.setObjectName(u"slider_contrast")
        self.slider_contrast.setMinimum(-127)
        self.slider_contrast.setMaximum(127)
        self.slider_contrast.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.slider_contrast)


        self.tab_brightnesscontrast_layout.addLayout(self.formLayout)

        self.horizontalFrame = QFrame(self.tab_brightnesscontrast)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy14.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy14)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.contrast_reset = QPushButton(self.horizontalFrame)
        self.contrast_reset.setObjectName(u"contrast_reset")

        self.horizontalLayout_3.addWidget(self.contrast_reset)

        self.contrast_apply = QPushButton(self.horizontalFrame)
        self.contrast_apply.setObjectName(u"contrast_apply")

        self.horizontalLayout_3.addWidget(self.contrast_apply)


        self.tab_brightnesscontrast_layout.addWidget(self.horizontalFrame)

        self.tabWidget.addTab(self.tab_brightnesscontrast, "")
        self.tab_LUT = QWidget()
        self.tab_LUT.setObjectName(u"tab_LUT")
        self.tab_LUT.setStyleSheet(u"background-color: rgb(72, 75, 75);\n"
"alternate-background-color: rgb(0, 0, 0);")
        self.layout_tab_LUT = QFormLayout(self.tab_LUT)
        self.layout_tab_LUT.setObjectName(u"layout_tab_LUT")
        self.tabWidget.addTab(self.tab_LUT, "")
        self.tab_record = QWidget()
        self.tab_record.setObjectName(u"tab_record")
        self.tab_record_layout = QVBoxLayout(self.tab_record)
        self.tab_record_layout.setObjectName(u"tab_record_layout")
        self.tabWidget.addTab(self.tab_record, "")

        self.verticalLayout_6.addWidget(self.tabWidget)


        self.layout_page_visualize.addWidget(self.visualize_leftpanel)

        self.content_tabs.addWidget(self.page_visualize)
        self.page_analyse = QWidget()
        self.page_analyse.setObjectName(u"page_analyse")
        self.layout_page_analyse = QVBoxLayout(self.page_analyse)
        self.layout_page_analyse.setSpacing(3)
        self.layout_page_analyse.setObjectName(u"layout_page_analyse")
        self.layout_page_analyse.setContentsMargins(0, 1, 1, 0)
        self.content_tabs.addWidget(self.page_analyse)

        self.frame_content_layout.addWidget(self.content_tabs)


        self.frame_main_layout.addWidget(self.frame_content)

        self.frame_bottom = QFrame(self.frame_main)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(100, 16))
        self.frame_bottom.setMaximumSize(QSize(16777215, 16))
        self.frame_bottom.setStyleSheet(u"border-width: 1 0 0 0px;")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.frame_bottom_layout = QHBoxLayout(self.frame_bottom)
        self.frame_bottom_layout.setObjectName(u"frame_bottom_layout")
        self.frame_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.label_appState = QLabel(self.frame_bottom)
        self.label_appState.setObjectName(u"label_appState")

        self.frame_bottom_layout.addWidget(self.label_appState)

        self.spring_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.frame_bottom_layout.addItem(self.spring_2)

        self.btn_resize_grip = QPushButton(self.frame_bottom)
        self.btn_resize_grip.setObjectName(u"btn_resize_grip")
        sizePolicy2.setHeightForWidth(self.btn_resize_grip.sizePolicy().hasHeightForWidth())
        self.btn_resize_grip.setSizePolicy(sizePolicy2)
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
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-size-grip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_resize_grip.setIcon(icon6)

        self.frame_bottom_layout.addWidget(self.btn_resize_grip)


        self.frame_main_layout.addWidget(self.frame_bottom)


        self.centralwidget_layout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.content_tabs.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        self.visualize_altPreviewsTabs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiontest1.setText(QCoreApplication.translate("MainWindow", u"test1", None))
        self.actiontest.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.actiontest_2.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.label.setText("")
        self.btn_plan.setText(QCoreApplication.translate("MainWindow", u"Plan", None))
        self.btn_visualize.setText(QCoreApplication.translate("MainWindow", u"Visualize", None))
        self.btn_analyse.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_exit.setText("")
        self.btn_importFile.setText(QCoreApplication.translate("MainWindow", u"Import File", None))
        self.btn_importFolder.setText(QCoreApplication.translate("MainWindow", u"Import Folder", None))
        self.btn_selectWorkspace.setText(QCoreApplication.translate("MainWindow", u"Select Workspace", None))
        self.label_fileInfo.setText(QCoreApplication.translate("MainWindow", u"File Info", None))
#if QT_CONFIG(tooltip)
        self.btn_run_pipeline.setToolTip(QCoreApplication.translate("MainWindow", u"Run", None))
#endif // QT_CONFIG(tooltip)
        self.btn_run_pipeline.setText("")
#if QT_CONFIG(tooltip)
        self.btn_save_pipeline.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_pipeline.setText("")
#if QT_CONFIG(statustip)
        self.btn_load_pipeline.setStatusTip(QCoreApplication.translate("MainWindow", u"Load pipeline", None))
#endif // QT_CONFIG(statustip)
        self.btn_load_pipeline.setText(QCoreApplication.translate("MainWindow", u"Load pipeline", None))
        self.btn_remove_operation.setText(QCoreApplication.translate("MainWindow", u"Delete operation", None))
        self.edit_pipeline_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#202020\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#202020;\"><br /></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2D), QCoreApplication.translate("MainWindow", u"2D", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3D), QCoreApplication.translate("MainWindow", u"3D", None))
        self.visualize_btn_addChannel.setText("")
        self.visualize_altPreviewsTabs.setTabText(self.visualize_altPreviewsTabs.indexOf(self.visualize_tab_orthogonalPreviews), QCoreApplication.translate("MainWindow", u"Orthogonal View", None))
        self.visualize_altPreviewsTabs.setTabText(self.visualize_altPreviewsTabs.indexOf(self.visualize_tab_annexes), QCoreApplication.translate("MainWindow", u"Annexes", None))
        self.tab_views_addBtn.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_views), QCoreApplication.translate("MainWindow", u"Views", None))
        self.bc_min_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bc_max_label.setText(QCoreApplication.translate("MainWindow", u"255", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Min :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Max :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Brightness :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cointrast :", None))
        self.contrast_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.contrast_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_brightnesscontrast), QCoreApplication.translate("MainWindow", u" Brightness/Contrast", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_LUT), QCoreApplication.translate("MainWindow", u"LUT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_record), QCoreApplication.translate("MainWindow", u"Record", None))
        self.label_appState.setText("")
        self.btn_resize_grip.setText("")
    # retranslateUi

