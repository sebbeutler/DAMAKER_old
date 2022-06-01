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


class Ui_BatchParameters(object):
    def setupUi(self, BatchParameters):
        if not BatchParameters.objectName():
            BatchParameters.setObjectName(u"BatchParameters")
        BatchParameters.resize(400, 300)
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
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_deploy.sizePolicy().hasHeightForWidth())
        self.btn_deploy.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_deploy)


        self.verticalLayout.addWidget(self.topBar)

        self.form = QFrame(BatchParameters)
        self.form.setObjectName(u"form")
        self.form.setMinimumSize(QSize(0, 10))
        self.form.setStyleSheet(u"background: red;")
        self.form.setFrameShape(QFrame.StyledPanel)
        self.form.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.form)
        self.formLayout_2.setObjectName(u"formLayout_2")

        self.verticalLayout.addWidget(self.form)


        self.retranslateUi(BatchParameters)

        QMetaObject.connectSlotsByName(BatchParameters)
    # setupUi

    def retranslateUi(self, BatchParameters):
        BatchParameters.setWindowTitle(QCoreApplication.translate("BatchParameters", u"Frame", None))
        self.btn_deploy.setText(QCoreApplication.translate("BatchParameters", u"Deploy", None))
    # retranslateUi

