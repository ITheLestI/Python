# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(461, 284)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 461, 281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.from_cur = QComboBox(self.verticalLayoutWidget)
        self.from_cur.setObjectName(u"from_cur")

        self.verticalLayout.addWidget(self.from_cur)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.to_cur = QComboBox(self.verticalLayoutWidget)
        self.to_cur.setObjectName(u"to_cur")

        self.verticalLayout.addWidget(self.to_cur)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.amount = QLineEdit(self.verticalLayoutWidget)
        self.amount.setObjectName(u"amount")

        self.verticalLayout.addWidget(self.amount)

        self.convert = QPushButton(self.verticalLayoutWidget)
        self.convert.setObjectName(u"convert")

        self.verticalLayout.addWidget(self.convert)

        self.total = QLabel(self.verticalLayoutWidget)
        self.total.setObjectName(u"total")

        self.verticalLayout.addWidget(self.total)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u0430\u044f \u0432\u0430\u043b\u044e\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0432\u0430\u043b\u044e\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.convert.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0432\u0435\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.total.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e: ", None))
    # retranslateUi

