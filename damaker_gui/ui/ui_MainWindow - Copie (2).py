# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - Copie (2).ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGraphicsView, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTabWidget, QTextEdit,
    QTreeView, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 768)
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
        font.setFamilies([u"Segoe UI"])
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
"	background-color: rgb(62, 62, 62);\n"
"\n"
"	border-radius: 2px;\n"
"	border: 1px solid rgb(32, 32, 32);\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 0px solid rgb(32, 32, 32);\n"
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
"    background: rgb(62, 62, 62);\n"
"    height: 14px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(32, 32, 32);\n"
"    min-width: 20px;\n"
"	border-radius: 1px\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(62, 62, 62);\n"
"    width: 14px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(32, 32, 32);\n"
"    min-height"
                        ": 25px;\n"
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
"    border:1px solid rgb(32, 32, 32);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(32, 32, 32);\n"
"}\n"
"QCheckBox::in"
                        "dicator:hover {\n"
"    border: 1px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 1px solid rgb(32, 32, 32);\n"
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
""
                        "	border-left-width: 3px;\n"
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
"    border-radius: 4px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(32, 32, 32);\n"
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
"    border-radius: 9px;"
                        "\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(32, 32, 32);\n"
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
"	border: 1px solid rgb(32, 32, 32);\n"
"	border-radius: 1px;	\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(118, 118, 118);\n"
"	border: 1px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(62, 62, 62);\n"
"	border: 1px solid rgb(43, 50, 61);\n"
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
        self.frame_top_layout.setSpacing(1)
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
        self.frame_pageSelect.setStyleSheet(u"QPushButton:checked {\n"
"	\n"
"	background-color: rgb(106, 106, 106);\n"
"}")
        self.layout_pageSelect = QHBoxLayout(self.frame_pageSelect)
        self.layout_pageSelect.setSpacing(1)
        self.layout_pageSelect.setObjectName(u"layout_pageSelect")
        self.layout_pageSelect.setContentsMargins(2, 0, 0, 0)
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
        self.btn_plan.setCheckable(True)

        self.layout_pageSelect.addWidget(self.btn_plan)

        self.btn_visualize = QPushButton(self.frame_pageSelect)
        self.btn_visualize.setObjectName(u"btn_visualize")
        self.btn_visualize.setCheckable(True)

        self.layout_pageSelect.addWidget(self.btn_visualize)

        self.btn_analyse = QPushButton(self.frame_pageSelect)
        self.btn_analyse.setObjectName(u"btn_analyse")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
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
        sizePolicy3.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy4)
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content_layout = QHBoxLayout(self.frame_content)
        self.frame_content_layout.setSpacing(0)
        self.frame_content_layout.setObjectName(u"frame_content_layout")
        self.frame_content_layout.setContentsMargins(0, 0, 0, 0)
        self.left_pannel = QFrame(self.frame_content)
        self.left_pannel.setObjectName(u"left_pannel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.left_pannel.sizePolicy().hasHeightForWidth())
        self.left_pannel.setSizePolicy(sizePolicy5)
        self.left_pannel.setMinimumSize(QSize(200, 0))
        self.left_pannel.setMaximumSize(QSize(200, 16777215))
        self.pannel_left_layout = QVBoxLayout(self.left_pannel)
        self.pannel_left_layout.setSpacing(0)
        self.pannel_left_layout.setObjectName(u"pannel_left_layout")
        self.pannel_left_layout.setContentsMargins(2, 1, 0, 0)
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
        self.treeview_workspace.setStyleSheet(u"color: black;\n"
"border-color: rgb(32, 32, 32);")
        self.treeview_workspace.setDragEnabled(True)
        self.treeview_workspace.setDragDropMode(QAbstractItemView.DragOnly)
        self.treeview_workspace.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

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
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pipeline_settings.sizePolicy().hasHeightForWidth())
        self.pipeline_settings.setSizePolicy(sizePolicy6)
        self.pipeline_settings.setMaximumSize(QSize(16777215, 200))
        self.pipeline_settings.setAcceptDrops(False)
        self.horizontalLayout = QHBoxLayout(self.pipeline_settings)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.previewPipelineView = QGraphicsView(self.previewPipeline)
        self.previewPipelineView.setObjectName(u"previewPipelineView")
        sizePolicy2.setHeightForWidth(self.previewPipelineView.sizePolicy().hasHeightForWidth())
        self.previewPipelineView.setSizePolicy(sizePolicy2)
        self.previewPipelineView.setMinimumSize(QSize(0, 0))
        self.previewPipelineView.setMaximumSize(QSize(300, 300))
        self.previewPipelineView.setMouseTracking(True)
        self.previewPipelineView.setAutoFillBackground(True)
        self.previewPipelineView.setStyleSheet(u"background-color: rgb(32, 32, 32);")
        self.previewPipelineView.setLineWidth(1)
        self.previewPipelineView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.previewPipelineView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        brush15 = QBrush(QColor(32, 32, 32, 255))
        brush15.setStyle(Qt.NoBrush)
        self.previewPipelineView.setBackgroundBrush(brush15)
        self.previewPipelineView.setDragMode(QGraphicsView.NoDrag)

        self.verticalLayout_2.addWidget(self.previewPipelineView)

        self.previewPipelineSlider = QSlider(self.previewPipeline)
        self.previewPipelineSlider.setObjectName(u"previewPipelineSlider")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.previewPipelineSlider.sizePolicy().hasHeightForWidth())
        self.previewPipelineSlider.setSizePolicy(sizePolicy7)
        self.previewPipelineSlider.setStyleSheet(u"padding: 0px;")
        self.previewPipelineSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.previewPipelineSlider)


        self.horizontalLayout.addWidget(self.previewPipeline)

        self.functions_frame = QFrame(self.pipeline_settings)
        self.functions_frame.setObjectName(u"functions_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.functions_frame.sizePolicy().hasHeightForWidth())
        self.functions_frame.setSizePolicy(sizePolicy8)
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

        self.horizontalLayout.addWidget(self.functions_frame)

        self.parameters_container = QFrame(self.pipeline_settings)
        self.parameters_container.setObjectName(u"parameters_container")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.parameters_container.sizePolicy().hasHeightForWidth())
        self.parameters_container.setSizePolicy(sizePolicy9)
        self.parameters_container.setMinimumSize(QSize(300, 0))
        self.parameters_container.setStyleSheet(u"color: white;border-width: 1px;")
        self.parameters_container.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_4 = QVBoxLayout(self.parameters_container)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.currentFunction = QLabel(self.parameters_container)
        self.currentFunction.setObjectName(u"currentFunction")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.currentFunction.sizePolicy().hasHeightForWidth())
        self.currentFunction.setSizePolicy(sizePolicy10)
        self.currentFunction.setMaximumSize(QSize(0, 0))
        self.currentFunction.setLineWidth(0)
        self.currentFunction.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_4.addWidget(self.currentFunction)

        self.pipline_settings_top = QFrame(self.parameters_container)
        self.pipline_settings_top.setObjectName(u"pipline_settings_top")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.pipline_settings_top.sizePolicy().hasHeightForWidth())
        self.pipline_settings_top.setSizePolicy(sizePolicy11)
        self.pipline_settings_top.setStyleSheet(u"border: 0px solid rgb(32, 32, 32); margin: 2px;")
        self.pipeline_settings_layout_top = QHBoxLayout(self.pipline_settings_top)
        self.pipeline_settings_layout_top.setSpacing(1)
        self.pipeline_settings_layout_top.setObjectName(u"pipeline_settings_layout_top")
        self.pipeline_settings_layout_top.setContentsMargins(0, 0, 0, 0)
        self.edit_operation_name = QLineEdit(self.pipline_settings_top)
        self.edit_operation_name.setObjectName(u"edit_operation_name")
        self.edit_operation_name.setEnabled(True)
        self.edit_operation_name.setStyleSheet(u"")
        self.edit_operation_name.setFrame(True)

        self.pipeline_settings_layout_top.addWidget(self.edit_operation_name)

        self.checkbox_enabled = QCheckBox(self.pipline_settings_top)
        self.checkbox_enabled.setObjectName(u"checkbox_enabled")
        self.checkbox_enabled.setIconSize(QSize(16, 16))
        self.checkbox_enabled.setChecked(True)
        self.checkbox_enabled.setTristate(False)

        self.pipeline_settings_layout_top.addWidget(self.checkbox_enabled)


        self.verticalLayout_4.addWidget(self.pipline_settings_top)

        self.frame_settingsForm = QFrame(self.parameters_container)
        self.frame_settingsForm.setObjectName(u"frame_settingsForm")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.frame_settingsForm.sizePolicy().hasHeightForWidth())
        self.frame_settingsForm.setSizePolicy(sizePolicy12)
        self.frame_settingsForm.setStyleSheet(u"border: 0px solid rgb(32, 32, 32);")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_settingsForm)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.layout_fnames = QVBoxLayout()
        self.layout_fnames.setObjectName(u"layout_fnames")

        self.horizontalLayout_2.addLayout(self.layout_fnames)

        self.layout_fargs = QVBoxLayout()
        self.layout_fargs.setObjectName(u"layout_fargs")

        self.horizontalLayout_2.addLayout(self.layout_fargs)


        self.verticalLayout_4.addWidget(self.frame_settingsForm)

        self.frame_outputDir = QFrame(self.parameters_container)
        self.frame_outputDir.setObjectName(u"frame_outputDir")
        sizePolicy11.setHeightForWidth(self.frame_outputDir.sizePolicy().hasHeightForWidth())
        self.frame_outputDir.setSizePolicy(sizePolicy11)
        self.frame_outputDir.setStyleSheet(u"border: 0px solid rgb(32, 32, 32);")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_outputDir)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout_4.addWidget(self.frame_outputDir)

        self.btn_modify_operation = QPushButton(self.parameters_container)
        self.btn_modify_operation.setObjectName(u"btn_modify_operation")
        self.btn_modify_operation.setAutoFillBackground(False)
        self.btn_modify_operation.setStyleSheet(u"border-width: 1px 0px 0px 0px;")

        self.verticalLayout_4.addWidget(self.btn_modify_operation)

        self.btn_add_operation = QPushButton(self.parameters_container)
        self.btn_add_operation.setObjectName(u"btn_add_operation")
        self.btn_add_operation.setStyleSheet(u"color: white; border-width: 1px 0px 0px 0px;")

        self.verticalLayout_4.addWidget(self.btn_add_operation)


        self.horizontalLayout.addWidget(self.parameters_container)


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
        sizePolicy13 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.btn_run_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_run_pipeline.setSizePolicy(sizePolicy13)
        self.btn_run_pipeline.setStyleSheet(u"border: 1px solid rgb(125, 125, 125);")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_run_pipeline.setIcon(icon3)
        self.btn_run_pipeline.setIconSize(QSize(16, 16))

        self.layout_operation_list_btns.addWidget(self.btn_run_pipeline)

        self.btn_save_pipeline = QPushButton(self.operation_list_btns)
        self.btn_save_pipeline.setObjectName(u"btn_save_pipeline")
        sizePolicy13.setHeightForWidth(self.btn_save_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_save_pipeline.setSizePolicy(sizePolicy13)
        self.btn_save_pipeline.setStyleSheet(u"border: 1px solid rgb(125, 125, 125);")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_pipeline.setIcon(icon4)

        self.layout_operation_list_btns.addWidget(self.btn_save_pipeline)

        self.btn_load_pipeline = QPushButton(self.operation_list_btns)
        self.btn_load_pipeline.setObjectName(u"btn_load_pipeline")
        sizePolicy13.setHeightForWidth(self.btn_load_pipeline.sizePolicy().hasHeightForWidth())
        self.btn_load_pipeline.setSizePolicy(sizePolicy13)
        self.btn_load_pipeline.setStyleSheet(u"border: 1px solid rgb(125, 125, 125);\n"
"padding: 3px;")

        self.layout_operation_list_btns.addWidget(self.btn_load_pipeline)

        self.btn_remove_operation = QPushButton(self.operation_list_btns)
        self.btn_remove_operation.setObjectName(u"btn_remove_operation")
        sizePolicy13.setHeightForWidth(self.btn_remove_operation.sizePolicy().hasHeightForWidth())
        self.btn_remove_operation.setSizePolicy(sizePolicy13)
        self.btn_remove_operation.setStyleSheet(u"border: 1px solid rgb(125, 125, 125);\n"
"padding: 3px;")

        self.layout_operation_list_btns.addWidget(self.btn_remove_operation)


        self.verticalLayout.addWidget(self.operation_list_btns)

        self.edit_pipeline_output = QTextEdit(self.pipeline_content)
        self.edit_pipeline_output.setObjectName(u"edit_pipeline_output")
        self.edit_pipeline_output.setMaximumSize(QSize(16777215, 150))
        self.edit_pipeline_output.setStyleSheet(u"QTextEdit {\n"
"    color: rgb(193, 193, 168);\n"
"	background-color: rgb(32, 32, 32);\n"
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
        self.layout_page_visualize.setContentsMargins(0, 1, 1, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.visualize_preview_verticalframe = QFrame(self.page_visualize)
        self.visualize_preview_verticalframe.setObjectName(u"visualize_preview_verticalframe")
        self.verticalLayout_3 = QVBoxLayout(self.visualize_preview_verticalframe)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainView = QGraphicsView(self.visualize_preview_verticalframe)
        self.mainView.setObjectName(u"mainView")
        sizePolicy12.setHeightForWidth(self.mainView.sizePolicy().hasHeightForWidth())
        self.mainView.setSizePolicy(sizePolicy12)
        self.mainView.setMinimumSize(QSize(500, 0))
        self.mainView.setLayoutDirection(Qt.LeftToRight)
        self.mainView.setStyleSheet(u"QGraphicsView {\n"
"	background: rgb(32, 32, 32);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(62, 62, 62);\n"
"    height: 14px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(32, 32, 32);\n"
"    min-width: 20px;\n"
"	border-radius: 1px\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(62, 62, 62);\n"
"    width: 14px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(32, 32, 32);\n"
"    min-height: 25px;\n"
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
" QSc"
                        "rollBar::sub-line:vertical {\n"
"	border: none;\n"
"    height: 0px;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.mainView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.mainView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_3.addWidget(self.mainView)

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

        self.verticalLayout_3.addWidget(self.channelList_frame)


        self.verticalLayout_7.addWidget(self.visualize_preview_verticalframe)

        self.visualize_functionListFrame = QFrame(self.page_visualize)
        self.visualize_functionListFrame.setObjectName(u"visualize_functionListFrame")
        self.visualize_functionListFrame.setMinimumSize(QSize(0, 200))
        self.visualize_functionListFrame.setMaximumSize(QSize(16777215, 200))
        self.visualize_functionListLayout = QHBoxLayout(self.visualize_functionListFrame)
        self.visualize_functionListLayout.setSpacing(1)
        self.visualize_functionListLayout.setObjectName(u"visualize_functionListLayout")
        self.visualize_functionListLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.visualize_functionListFrame)


        self.layout_page_visualize.addLayout(self.verticalLayout_7)

        self.visualize_leftpanel = QFrame(self.page_visualize)
        self.visualize_leftpanel.setObjectName(u"visualize_leftpanel")
        self.visualize_leftpanel.setFrameShape(QFrame.StyledPanel)
        self.visualize_leftpanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.visualize_leftpanel)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.topView = QGraphicsView(self.visualize_leftpanel)
        self.topView.setObjectName(u"topView")
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.topView.sizePolicy().hasHeightForWidth())
        self.topView.setSizePolicy(sizePolicy14)
        self.topView.setMinimumSize(QSize(200, 0))
        self.topView.setStyleSheet(u"QGraphicsView {\n"
"background-color: rgb(32, 32, 32);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"}")

        self.verticalLayout_6.addWidget(self.topView)

        self.leftView = QGraphicsView(self.visualize_leftpanel)
        self.leftView.setObjectName(u"leftView")
        sizePolicy14.setHeightForWidth(self.leftView.sizePolicy().hasHeightForWidth())
        self.leftView.setSizePolicy(sizePolicy14)
        self.leftView.setMinimumSize(QSize(200, 0))
        self.leftView.setStyleSheet(u"QGraphicsView {\n"
"background-color: rgb(32, 32, 32);\n"
"border: 1px solid rgb(132, 132, 132);\n"
"border-width:  0px 1px 1px 1px ;\n"
"}")

        self.verticalLayout_6.addWidget(self.leftView)

        self.tabWidget = QTabWidget(self.visualize_leftpanel)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(2807, 16777215))
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(62, 62, 62);\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"    border: 1px solid black;\n"
"}\n"
"QTabWidget::pane { border: 0; }\n"
"\n"
"QTabBar {\n"
"  background-color: rgb(62, 62, 62);\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"   border: 1px solid black;\n"
"  background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"QTabBar::pane {\n"
"  border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  color: lightgray;\n"
"  background-color: rgb(62, 62, 62);\n"
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
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.tabWidgetPage2.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
"alternate-background-color: rgb(0, 0, 0);")
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
"alternate-background-color: rgb(0, 0, 0);")
        self.tabWidget.addTab(self.tab, "")

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
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-size-grip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_resize_grip.setIcon(icon5)

        self.frame_bottom_layout.addWidget(self.btn_resize_grip)


        self.frame_main_layout.addWidget(self.frame_bottom)


        self.centralwidget_layout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.content_tabs.setCurrentIndex(1)
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
        self.currentFunction.setText(QCoreApplication.translate("MainWindow", u"CurrentFunction", None))
        self.edit_operation_name.setInputMask("")
        self.edit_operation_name.setText("")
        self.edit_operation_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Operation name", None))
        self.checkbox_enabled.setText("")
        self.btn_modify_operation.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.btn_add_operation.setText(QCoreApplication.translate("MainWindow", u"Add", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("MainWindow", u" Brightness Con...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.btn_resize_grip.setText("")
    # retranslateUi

