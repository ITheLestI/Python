# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'counter.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 332)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"\n"
"}\n"
"\n"
"QPushButton:selected\n"
"{\n"
"	outline: none;\n"
"}\n"
"\n"
"QPushButton:active\n"
"{\n"
"	outline: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ok_button = QPushButton(self.centralwidget)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(120, 200, 121, 91))
        self.ok_button.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 26pt \"OCR A Extended\";")
        self.counter = QLabel(self.centralwidget)
        self.counter.setObjectName(u"counter")
        self.counter.setGeometry(QRect(140, 70, 81, 71))
        self.counter.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.counter.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.ok_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u041a", None))
        self.counter.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

