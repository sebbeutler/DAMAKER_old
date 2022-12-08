# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FunctionForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from damaker_gui.widgets.OperationWidget import OperationWidget


class Ui_FunctionForm(object):
    def setupUi(self, FunctionForm):
        if not FunctionForm.objectName():
            FunctionForm.setObjectName(u"FunctionForm")
        FunctionForm.resize(400, 300)
        self.verticalLayout = QVBoxLayout(FunctionForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.function_description = QLabel(FunctionForm)
        self.function_description.setObjectName(u"function_description")
        self.function_description.setMargin(15)

        self.verticalLayout.addWidget(self.function_description)

        self.function_settings = OperationWidget(FunctionForm)
        self.function_settings.setObjectName(u"function_settings")
        self.function_settings.setMinimumSize(QSize(0, 100))
        self.function_settings.setFrameShape(QFrame.StyledPanel)
        self.function_settings.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.function_settings)

        self.button_list = QFrame(FunctionForm)
        self.button_list.setObjectName(u"button_list")
        self.button_list.setFrameShape(QFrame.StyledPanel)
        self.button_list.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.button_list)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_addToPipeline = QPushButton(self.button_list)
        self.btn_addToPipeline.setObjectName(u"btn_addToPipeline")

        self.horizontalLayout.addWidget(self.btn_addToPipeline)

        self.btn_apply = QPushButton(self.button_list)
        self.btn_apply.setObjectName(u"btn_apply")

        self.horizontalLayout.addWidget(self.btn_apply)


        self.verticalLayout.addWidget(self.button_list)


        self.retranslateUi(FunctionForm)

        QMetaObject.connectSlotsByName(FunctionForm)
    # setupUi

    def retranslateUi(self, FunctionForm):
        FunctionForm.setWindowTitle(QCoreApplication.translate("FunctionForm", u"GroupBox", None))
        FunctionForm.setTitle(QCoreApplication.translate("FunctionForm", u"Function name", None))
        self.function_description.setText("")
        self.btn_addToPipeline.setText(QCoreApplication.translate("FunctionForm", u"Add to Pipeline", None))
        self.btn_apply.setText(QCoreApplication.translate("FunctionForm", u"Apply", None))
    # retranslateUi

