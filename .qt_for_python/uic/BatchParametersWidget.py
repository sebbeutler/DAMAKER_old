# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BatchParametersWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_BatchParameters(object):
    def setupUi(self, BatchParameters):
        if not BatchParameters.objectName():
            BatchParameters.setObjectName(u"BatchParameters")
        BatchParameters.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BatchParameters.sizePolicy().hasHeightForWidth())
        BatchParameters.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(BatchParameters)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(BatchParameters)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 25))
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(320, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_deploy = QPushButton(self.topBar)
        self.btn_deploy.setObjectName(u"btn_deploy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_deploy.sizePolicy().hasHeightForWidth())
        self.btn_deploy.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btn_deploy)


        self.verticalLayout.addWidget(self.topBar)

        self.batch_form = QFrame(BatchParameters)
        self.batch_form.setObjectName(u"batch_form")
        sizePolicy.setHeightForWidth(self.batch_form.sizePolicy().hasHeightForWidth())
        self.batch_form.setSizePolicy(sizePolicy)
        self.batch_form.setMinimumSize(QSize(0, 100))
        self.batch_form.setStyleSheet(u"* {\n"
"	color: rgb(170, 170, 170);\n"
"}\n"
"\n"
"QFrame {\n"
"background: rgb(32,32,32);\n"
"border-radius: 2px;\n"
"border: 1px solid rgb(60, 60, 60);\n"
"}\n"
"\n"
"QLabel {\n"
"\n"
"	border-width: 0px;\n"
"}")
        self.batch_form.setFrameShape(QFrame.StyledPanel)
        self.batch_form.setFrameShadow(QFrame.Raised)
        self.batch_form_layout = QFormLayout(self.batch_form)
        self.batch_form_layout.setObjectName(u"batch_form_layout")
        self.batch_form_layout.setLabelAlignment(Qt.AlignCenter)
        self.batch_form_layout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label = QLabel(self.batch_form)
        self.label.setObjectName(u"label")

        self.batch_form_layout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.filename_input = QLineEdit(self.batch_form)
        self.filename_input.setObjectName(u"filename_input")
        self.filename_input.setMaximumSize(QSize(170, 16777215))

        self.batch_form_layout.setWidget(0, QFormLayout.FieldRole, self.filename_input)

        self.label_2 = QLabel(self.batch_form)
        self.label_2.setObjectName(u"label_2")

        self.batch_form_layout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.checkBox_associated = QCheckBox(self.batch_form)
        self.checkBox_associated.setObjectName(u"checkBox_associated")
        self.checkBox_associated.setChecked(True)

        self.batch_form_layout.setWidget(1, QFormLayout.FieldRole, self.checkBox_associated)

        self.label_3 = QLabel(self.batch_form)
        self.label_3.setObjectName(u"label_3")

        self.batch_form_layout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.btn_add_mod = QPushButton(self.batch_form)
        self.btn_add_mod.setObjectName(u"btn_add_mod")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_add_mod.sizePolicy().hasHeightForWidth())
        self.btn_add_mod.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_mod.setIcon(icon)

        self.batch_form_layout.setWidget(2, QFormLayout.FieldRole, self.btn_add_mod)


        self.verticalLayout.addWidget(self.batch_form)


        self.retranslateUi(BatchParameters)

        QMetaObject.connectSlotsByName(BatchParameters)
    # setupUi

    def retranslateUi(self, BatchParameters):
        BatchParameters.setWindowTitle(QCoreApplication.translate("BatchParameters", u"Frame", None))
        self.btn_deploy.setText(QCoreApplication.translate("BatchParameters", u"Deploy", None))
        self.label.setText(QCoreApplication.translate("BatchParameters", u"File name:", None))
        self.filename_input.setText(QCoreApplication.translate("BatchParameters", u"*", None))
        self.label_2.setText(QCoreApplication.translate("BatchParameters", u"Associated:", None))
        self.checkBox_associated.setText("")
        self.label_3.setText(QCoreApplication.translate("BatchParameters", u"Modalities:", None))
        self.btn_add_mod.setText("")
    # retranslateUi

