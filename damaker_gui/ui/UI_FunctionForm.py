# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sdv/m1isdd/sbeutler/Bureau/DAMAKER/damaker_gui/ui/FunctionForm.ui',
# licensing of '/home/sdv/m1isdd/sbeutler/Bureau/DAMAKER/damaker_gui/ui/FunctionForm.ui' applies.
#
# Created: Mon Nov  7 14:50:43 2022
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FunctionForm(object):
    def setupUi(self, FunctionForm):
        FunctionForm.setObjectName("FunctionForm")
        FunctionForm.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(FunctionForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.function_description = QtWidgets.QLabel(FunctionForm)
        self.function_description.setText("")
        self.function_description.setMargin(15)
        self.function_description.setObjectName("function_description")
        self.verticalLayout.addWidget(self.function_description)
        self.function_settings = OperationWidget(FunctionForm)
        self.function_settings.setMinimumSize(QtCore.QSize(0, 100))
        self.function_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_settings.setObjectName("function_settings")
        self.verticalLayout.addWidget(self.function_settings)
        self.button_list = QtWidgets.QFrame(FunctionForm)
        self.button_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_list.setObjectName("button_list")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_list)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_addToPipeline = QtWidgets.QPushButton(self.button_list)
        self.btn_addToPipeline.setObjectName("btn_addToPipeline")
        self.horizontalLayout.addWidget(self.btn_addToPipeline)
        self.btn_run = QtWidgets.QPushButton(self.button_list)
        self.btn_run.setObjectName("btn_run")
        self.horizontalLayout.addWidget(self.btn_run)
        self.btn_apply = QtWidgets.QPushButton(self.button_list)
        self.btn_apply.setObjectName("btn_apply")
        self.horizontalLayout.addWidget(self.btn_apply)
        self.verticalLayout.addWidget(self.button_list)

        self.retranslateUi(FunctionForm)
        QtCore.QMetaObject.connectSlotsByName(FunctionForm)
