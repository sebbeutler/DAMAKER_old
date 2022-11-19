# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FunctionParametersWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_FunctionParameters(object):
    def setupUi(self, FunctionParameters):
        if not FunctionParameters.objectName():
            FunctionParameters.setObjectName(u"FunctionParameters")
        FunctionParameters.resize(402, 330)
        FunctionParameters.setStyleSheet(u"color: white;\n"
"border-width: 1px;")
        self.verticalLayout = QVBoxLayout(FunctionParameters)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pipline_settings_top = QFrame(FunctionParameters)
        self.pipline_settings_top.setObjectName(u"pipline_settings_top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pipline_settings_top.sizePolicy().hasHeightForWidth())
        self.pipline_settings_top.setSizePolicy(sizePolicy)
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

        self.btn_batchMode = QPushButton(self.pipline_settings_top)
        self.btn_batchMode.setObjectName(u"btn_batchMode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_batchMode.sizePolicy().hasHeightForWidth())
        self.btn_batchMode.setSizePolicy(sizePolicy1)
        self.btn_batchMode.setStyleSheet(u"QPushButton {\n"
"	padding: 2px;\n"
"	border-radius: 2px;\n"
"	background-color: rgb(42, 42, 42);\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   border: 1px solid rgb(90,90,90);\n"
"}\n"
"\n"
"QPushButton:checked {	\n"
"	background-color: rgb(23, 144, 21);\n"
"}")
        self.btn_batchMode.setCheckable(True)

        self.pipeline_settings_layout_top_2.addWidget(self.btn_batchMode)

        self.checkbox_enabled = QCheckBox(self.pipline_settings_top)
        self.checkbox_enabled.setObjectName(u"checkbox_enabled")
        self.checkbox_enabled.setIconSize(QSize(16, 16))
        self.checkbox_enabled.setChecked(True)
        self.checkbox_enabled.setTristate(False)

        self.pipeline_settings_layout_top_2.addWidget(self.checkbox_enabled)


        self.verticalLayout.addWidget(self.pipline_settings_top)

        self.scrollArea = QScrollArea(FunctionParameters)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"\n"
"border: 0px solid rgb(32, 32, 32);")
        self.scrollArea.setWidgetResizable(True)
        self.widget_settingsForm = QWidget()
        self.widget_settingsForm.setObjectName(u"widget_settingsForm")
        self.widget_settingsForm.setGeometry(QRect(0, 0, 402, 257))
        self.widget_settingsForm.setStyleSheet(u"QLabel {\n"
"	border-width: 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	border: 1px solid black;\n"
"	padding: 2px;\n"
"}")
        self.layout_settingsForm = QFormLayout(self.widget_settingsForm)
        self.layout_settingsForm.setObjectName(u"layout_settingsForm")
        self.layout_settingsForm.setContentsMargins(20, 10, 5, 5)
        self.scrollArea.setWidget(self.widget_settingsForm)

        self.verticalLayout.addWidget(self.scrollArea)

        self.frame_outputDir = QFrame(FunctionParameters)
        self.frame_outputDir.setObjectName(u"frame_outputDir")
        sizePolicy.setHeightForWidth(self.frame_outputDir.sizePolicy().hasHeightForWidth())
        self.frame_outputDir.setSizePolicy(sizePolicy)
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
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

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
        self.edit_operation_name.setInputMask("")
        self.edit_operation_name.setText("")
        self.edit_operation_name.setPlaceholderText(QCoreApplication.translate("FunctionParameters", u"Operation name", None))
        self.btn_batchMode.setText(QCoreApplication.translate("FunctionParameters", u"Batch mode", None))
        self.checkbox_enabled.setText("")
        self.btn_modify_operation.setText(QCoreApplication.translate("FunctionParameters", u"Apply", None))
        self.btn_add_operation.setText(QCoreApplication.translate("FunctionParameters", u"Add", None))
    # retranslateUi

