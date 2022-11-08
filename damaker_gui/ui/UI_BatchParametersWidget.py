# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sdv/m1isdd/sbeutler/Bureau/DAMAKER/damaker_gui/ui/BatchParametersWidget.ui',
# licensing of '/home/sdv/m1isdd/sbeutler/Bureau/DAMAKER/damaker_gui/ui/BatchParametersWidget.ui' applies.
#
# Created: Mon Nov  7 14:50:43 2022
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_BatchParameters(object):
    def setupUi(self, BatchParameters):
        BatchParameters.setObjectName("BatchParameters")
        BatchParameters.resize(309, 134)
        BatchParameters.setMinimumSize(QtCore.QSize(309, 0))
        BatchParameters.setStyleSheet("QScrollArea {\n"
" border-radius: 3px;\n"
"border: 1px solid rgb(60, 60, 60);\n"
"background-color: rgb(238, 248, 255);\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:9px;\n"
"    padding-bottom:9px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,25%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,50%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/image/3.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/image/1.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/image/4.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/image/2.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
"{\n"
"    background:rgba(0,0,0,10%);\n"
"    border-radius:4px;\n"
"}")
        BatchParameters.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        BatchParameters.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        BatchParameters.setWidgetResizable(True)
        self.BatchParametersContent = QtWidgets.QFrame()
        self.BatchParametersContent.setGeometry(QtCore.QRect(0, 0, 307, 132))
        self.BatchParametersContent.setStyleSheet("")
        self.BatchParametersContent.setObjectName("BatchParametersContent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.BatchParametersContent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topBar = QtWidgets.QFrame(self.BatchParametersContent)
        self.topBar.setEnabled(True)
        self.topBar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.topBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topBar.setObjectName("topBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(320, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_deploy = QtWidgets.QPushButton(self.topBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_deploy.sizePolicy().hasHeightForWidth())
        self.btn_deploy.setSizePolicy(sizePolicy)
        self.btn_deploy.setObjectName("btn_deploy")
        self.horizontalLayout.addWidget(self.btn_deploy)
        self.verticalLayout.addWidget(self.topBar)
        self.batch_form = QtWidgets.QFrame(self.BatchParametersContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch_form.sizePolicy().hasHeightForWidth())
        self.batch_form.setSizePolicy(sizePolicy)
        self.batch_form.setMinimumSize(QtCore.QSize(0, 100))
        self.batch_form.setStyleSheet("")
        self.batch_form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.batch_form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.batch_form.setObjectName("batch_form")
        self.batch_form_layout = QtWidgets.QFormLayout(self.batch_form)
        self.batch_form_layout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.batch_form_layout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.batch_form_layout.setObjectName("batch_form_layout")
        self.label = QtWidgets.QLabel(self.batch_form)
        self.label.setObjectName("label")
        self.batch_form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.filename_input = QtWidgets.QLineEdit(self.batch_form)
        self.filename_input.setMaximumSize(QtCore.QSize(170, 16777215))
        self.filename_input.setObjectName("filename_input")
        self.batch_form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filename_input)
        self.label_2 = QtWidgets.QLabel(self.batch_form)
        self.label_2.setObjectName("label_2")
        self.batch_form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.checkBox_associated = QtWidgets.QCheckBox(self.batch_form)
        self.checkBox_associated.setText("")
        self.checkBox_associated.setChecked(True)
        self.checkBox_associated.setObjectName("checkBox_associated")
        self.batch_form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox_associated)
        self.label_3 = QtWidgets.QLabel(self.batch_form)
        self.label_3.setObjectName("label_3")
        self.batch_form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.btn_add_mod = QtWidgets.QPushButton(self.batch_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_mod.sizePolicy().hasHeightForWidth())
        self.btn_add_mod.setSizePolicy(sizePolicy)
        self.btn_add_mod.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_mod.setIcon(icon)
        self.btn_add_mod.setObjectName("btn_add_mod")
        self.batch_form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_add_mod)
        self.verticalLayout.addWidget(self.batch_form)
        BatchParameters.setWidget(self.BatchParametersContent)

        self.retranslateUi(BatchParameters)
        QtCore.QMetaObject.connectSlotsByName(BatchParameters)
