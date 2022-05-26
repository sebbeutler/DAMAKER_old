# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FunctionParametersWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FunctionParameters(object):
    def setupUi(self, FunctionParameters):
        if not FunctionParameters.objectName():
            FunctionParameters.setObjectName(u"FunctionParameters")
        FunctionParameters.resize(402, 328)
        FunctionParameters.setStyleSheet(u"color: white;\n"
"border-width: 1px;")
        self.verticalLayout = QVBoxLayout(FunctionParameters)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.currentFunction = QLabel(FunctionParameters)
        self.currentFunction.setObjectName(u"currentFunction")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentFunction.sizePolicy().hasHeightForWidth())
        self.currentFunction.setSizePolicy(sizePolicy)
        self.currentFunction.setMaximumSize(QSize(0, 0))
        self.currentFunction.setLineWidth(0)
        self.currentFunction.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.currentFunction)

        self.pipline_settings_top = QFrame(FunctionParameters)
        self.pipline_settings_top.setObjectName(u"pipline_settings_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pipline_settings_top.sizePolicy().hasHeightForWidth())
        self.pipline_settings_top.setSizePolicy(sizePolicy1)
        self.pipline_settings_top.setStyleSheet(u"border: 0px solid rgb(32, 32, 32); margin: 2px;")
        self.pipeline_settings_layout_top_2 = QHBoxLayout(self.pipline_settings_top)
        self.pipeline_settings_layout_top_2.setSpacing(1)
        self.pipeline_settings_layout_top_2.setObjectName(u"pipeline_settings_layout_top_2")
        self.pipeline_settings_layout_top_2.setContentsMargins(0, 0, 0, 0)
        self.edit_operation_name = QLineEdit(self.pipline_settings_top)
        self.edit_operation_name.setObjectName(u"edit_operation_name")
        self.edit_operation_name.setEnabled(True)
        self.edit_operation_name.setStyleSheet(u"")
        self.edit_operation_name.setFrame(True)

        self.pipeline_settings_layout_top_2.addWidget(self.edit_operation_name)

        self.checkbox_enabled = QCheckBox(self.pipline_settings_top)
        self.checkbox_enabled.setObjectName(u"checkbox_enabled")
        self.checkbox_enabled.setIconSize(QSize(16, 16))
        self.checkbox_enabled.setChecked(True)
        self.checkbox_enabled.setTristate(False)

        self.pipeline_settings_layout_top_2.addWidget(self.checkbox_enabled)


        self.verticalLayout.addWidget(self.pipline_settings_top)

        self.frame_settingsForm = QFrame(FunctionParameters)
        self.frame_settingsForm.setObjectName(u"frame_settingsForm")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_settingsForm.sizePolicy().hasHeightForWidth())
        self.frame_settingsForm.setSizePolicy(sizePolicy2)
        self.frame_settingsForm.setStyleSheet(u"QFrame#frame_settingsForm {\n"
"border: 0px solid rgb(32, 32, 32);\n"
"}\n"
"\n"
"QLabel {\n"
"	border-width: 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	border: 1px solid black;\n"
"	padding: 2px;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_settingsForm)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 0, 3, 0)
        self.layout_fnames = QVBoxLayout()
        self.layout_fnames.setObjectName(u"layout_fnames")

        self.horizontalLayout_3.addLayout(self.layout_fnames)

        self.layout_fargs = QVBoxLayout()
        self.layout_fargs.setObjectName(u"layout_fargs")

        self.horizontalLayout_3.addLayout(self.layout_fargs)


        self.verticalLayout.addWidget(self.frame_settingsForm)

        self.frame_outputDir = QFrame(FunctionParameters)
        self.frame_outputDir.setObjectName(u"frame_outputDir")
        sizePolicy1.setHeightForWidth(self.frame_outputDir.sizePolicy().hasHeightForWidth())
        self.frame_outputDir.setSizePolicy(sizePolicy1)
        self.frame_outputDir.setStyleSheet(u"QFrame {\n"
"border: 0px solid rgb(32, 32, 32);\n"
"}\n"
"\n"
"QLabel {\n"
"	border-width: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 1px solid black;\n"
"	padding: 2px;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_outputDir)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout.addWidget(self.frame_outputDir)

        self.btn_modify_operation = QPushButton(FunctionParameters)
        self.btn_modify_operation.setObjectName(u"btn_modify_operation")
        self.btn_modify_operation.setAutoFillBackground(False)
        self.btn_modify_operation.setStyleSheet(u"border-width: 1px 0px 0px 0px;")

        self.verticalLayout.addWidget(self.btn_modify_operation)

        self.btn_add_operation = QPushButton(FunctionParameters)
        self.btn_add_operation.setObjectName(u"btn_add_operation")
        self.btn_add_operation.setStyleSheet(u"color: white; border-width: 1px 0px 0px 0px;")

        self.verticalLayout.addWidget(self.btn_add_operation)


        self.retranslateUi(FunctionParameters)

        QMetaObject.connectSlotsByName(FunctionParameters)
    # setupUi

    def retranslateUi(self, FunctionParameters):
        FunctionParameters.setWindowTitle(QCoreApplication.translate("FunctionParameters", u"Frame", None))
        self.currentFunction.setText(QCoreApplication.translate("FunctionParameters", u"CurrentFunction", None))
        self.edit_operation_name.setInputMask("")
        self.edit_operation_name.setText("")
        self.edit_operation_name.setPlaceholderText(QCoreApplication.translate("FunctionParameters", u"Operation name", None))
        self.checkbox_enabled.setText("")
        self.btn_modify_operation.setText(QCoreApplication.translate("FunctionParameters", u"Apply", None))
        self.btn_add_operation.setText(QCoreApplication.translate("FunctionParameters", u"Add", None))
    # retranslateUi

