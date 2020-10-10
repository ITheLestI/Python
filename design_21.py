# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '21.ui'
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
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QSize(960, 640))
        MainWindow.setMaximumSize(QSize(960, 640))
        icon = QIcon()
        icon.addFile(u"img/21.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"	background-image: url(\"img/background1.png\");\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	color: white;\n"
"	font: 11pt \"Comic Sans MS\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	margin-left: 20px;\n"
"}\n"
"\n"
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
        self.more_button = QPushButton(self.centralwidget)
        self.more_button.setObjectName(u"more_button")
        self.more_button.setGeometry(QRect(760, 430, 151, 41))
        self.more_button.setStyleSheet(u"background-color: #aa5500;\n"
"")
        self.enough_button = QPushButton(self.centralwidget)
        self.enough_button.setObjectName(u"enough_button")
        self.enough_button.setGeometry(QRect(760, 480, 151, 41))
        self.enough_button.setStyleSheet(u"background-color: #d00000;")
        self.balance = QLabel(self.centralwidget)
        self.balance.setObjectName(u"balance")
        self.balance.setGeometry(QRect(760, 160, 151, 41))
        self.balance.setStyleSheet(u"font: 20pt \"Old English Text MT\";\n"
"color: white;\n"
"border-radius: 20px;")
        self.balance.setAlignment(Qt.AlignCenter)
        self.play_button = QPushButton(self.centralwidget)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(760, 550, 151, 41))
        self.play_button.setStyleSheet(u"background-color: #00557f;\n"
"")
        self.dealer = QLabel(self.centralwidget)
        self.dealer.setObjectName(u"dealer")
        self.dealer.setGeometry(QRect(-50, 430, 211, 211))
        self.dealer.setPixmap(QPixmap(u"img/dealer.png"))
        self.dealer.setScaledContents(True)
        self.dcard1 = QLabel(self.centralwidget)
        self.dcard1.setObjectName(u"dcard1")
        self.dcard1.setGeometry(QRect(200, 500, 63, 85))
        self.dcard2 = QLabel(self.centralwidget)
        self.dcard2.setObjectName(u"dcard2")
        self.dcard2.setGeometry(QRect(230, 500, 63, 85))
        self.dcard3 = QLabel(self.centralwidget)
        self.dcard3.setObjectName(u"dcard3")
        self.dcard3.setGeometry(QRect(260, 500, 63, 85))
        self.dcard4 = QLabel(self.centralwidget)
        self.dcard4.setObjectName(u"dcard4")
        self.dcard4.setGeometry(QRect(290, 500, 63, 85))
        self.dcard5 = QLabel(self.centralwidget)
        self.dcard5.setObjectName(u"dcard5")
        self.dcard5.setGeometry(QRect(320, 500, 63, 85))
        self.dcard6 = QLabel(self.centralwidget)
        self.dcard6.setObjectName(u"dcard6")
        self.dcard6.setGeometry(QRect(350, 500, 63, 85))
        self.dcard7 = QLabel(self.centralwidget)
        self.dcard7.setObjectName(u"dcard7")
        self.dcard7.setGeometry(QRect(380, 500, 63, 85))
        self.dcard8 = QLabel(self.centralwidget)
        self.dcard8.setObjectName(u"dcard8")
        self.dcard8.setGeometry(QRect(410, 500, 63, 85))
        self.dcard9 = QLabel(self.centralwidget)
        self.dcard9.setObjectName(u"dcard9")
        self.dcard9.setGeometry(QRect(440, 500, 63, 85))
        self.dcard10 = QLabel(self.centralwidget)
        self.dcard10.setObjectName(u"dcard10")
        self.dcard10.setGeometry(QRect(470, 500, 63, 85))
        self.dcard11 = QLabel(self.centralwidget)
        self.dcard11.setObjectName(u"dcard11")
        self.dcard11.setGeometry(QRect(500, 500, 63, 85))
        self.ucard1 = QLabel(self.centralwidget)
        self.ucard1.setObjectName(u"ucard1")
        self.ucard1.setGeometry(QRect(110, 90, 63, 85))
        self.ucard2 = QLabel(self.centralwidget)
        self.ucard2.setObjectName(u"ucard2")
        self.ucard2.setGeometry(QRect(140, 90, 63, 85))
        self.ucard3 = QLabel(self.centralwidget)
        self.ucard3.setObjectName(u"ucard3")
        self.ucard3.setGeometry(QRect(170, 90, 63, 85))
        self.ucard4 = QLabel(self.centralwidget)
        self.ucard4.setObjectName(u"ucard4")
        self.ucard4.setGeometry(QRect(200, 90, 63, 85))
        self.ucard5 = QLabel(self.centralwidget)
        self.ucard5.setObjectName(u"ucard5")
        self.ucard5.setGeometry(QRect(230, 90, 63, 85))
        self.ucard6 = QLabel(self.centralwidget)
        self.ucard6.setObjectName(u"ucard6")
        self.ucard6.setGeometry(QRect(260, 90, 63, 85))
        self.ucard7 = QLabel(self.centralwidget)
        self.ucard7.setObjectName(u"ucard7")
        self.ucard7.setGeometry(QRect(290, 90, 63, 85))
        self.ucard8 = QLabel(self.centralwidget)
        self.ucard8.setObjectName(u"ucard8")
        self.ucard8.setGeometry(QRect(320, 90, 63, 85))
        self.ucard9 = QLabel(self.centralwidget)
        self.ucard9.setObjectName(u"ucard9")
        self.ucard9.setGeometry(QRect(350, 90, 63, 85))
        self.ucard10 = QLabel(self.centralwidget)
        self.ucard10.setObjectName(u"ucard10")
        self.ucard10.setGeometry(QRect(380, 90, 63, 85))
        self.ucard11 = QLabel(self.centralwidget)
        self.ucard11.setObjectName(u"ucard11")
        self.ucard11.setGeometry(QRect(410, 90, 63, 85))
        self.dpoints = QLabel(self.centralwidget)
        self.dpoints.setObjectName(u"dpoints")
        self.dpoints.setGeometry(QRect(150, 518, 41, 41))
        self.dpoints.setStyleSheet(u"font: 20pt \"Old English Text MT\";\n"
"color: white;\n"
"border-radius: 20px;")
        self.dpoints.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.upoints = QLabel(self.centralwidget)
        self.upoints.setObjectName(u"upoints")
        self.upoints.setGeometry(QRect(60, 110, 41, 41))
        self.upoints.setStyleSheet(u"font: 20pt \"Old English Text MT\";\n"
"color: white;\n"
"border-radius: 20px;")
        self.upoints.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.information_block = QLabel(self.centralwidget)
        self.information_block.setObjectName(u"information_block")
        self.information_block.setGeometry(QRect(86, 376, 331, 61))
        self.information_block.setStyleSheet(u"font: 14pt \"Old English Text MT\";\n"
"color: white;")
        self.information_block.setAlignment(Qt.AlignCenter)
        self.ace_button_1 = QPushButton(self.centralwidget)
        self.ace_button_1.setObjectName(u"ace_button_1")
        self.ace_button_1.setGeometry(QRect(780, 430, 41, 41))
        self.ace_button_1.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #aa5500;\n"
"	margin:0\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #00557f;\n"
"}\n"
"")
        self.ace_button_11 = QPushButton(self.centralwidget)
        self.ace_button_11.setObjectName(u"ace_button_11")
        self.ace_button_11.setGeometry(QRect(840, 430, 41, 41))
        self.ace_button_11.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #aa5500;\n"
"	margin:0\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #00557f;\n"
"}\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(790, 90, 81, 71))
        self.label.setPixmap(QPixmap(u"img/money.png"))
        self.label.setScaledContents(True)
        self.dialog = QLabel(self.centralwidget)
        self.dialog.setObjectName(u"dialog")
        self.dialog.setGeometry(QRect(10, 320, 481, 211))
        self.dialog.setPixmap(QPixmap(u"img/dialog.png"))
        self.dialog.setScaledContents(True)
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(900, 10, 41, 41))
        self.close_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	margin:0;\n"
"	margin-top: 7px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"img/close_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QSize(32, 32))
        self.chip1 = QPushButton(self.centralwidget)
        self.chip1.setObjectName(u"chip1")
        self.chip1.setGeometry(QRect(106, 230, 51, 51))
        self.chip1.setStyleSheet(u"QPushButton\n"
"{\n"
"	margin-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	margin-bottom: 11px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"img/chips/1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chip1.setIcon(icon2)
        self.chip1.setIconSize(QSize(45, 45))
        self.chip5 = QPushButton(self.centralwidget)
        self.chip5.setObjectName(u"chip5")
        self.chip5.setGeometry(QRect(156, 230, 51, 51))
        self.chip5.setStyleSheet(u"QPushButton\n"
"{\n"
"	margin-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	margin-bottom: 11px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"img/chips/5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chip5.setIcon(icon3)
        self.chip5.setIconSize(QSize(45, 45))
        self.chip25 = QPushButton(self.centralwidget)
        self.chip25.setObjectName(u"chip25")
        self.chip25.setGeometry(QRect(206, 230, 51, 51))
        self.chip25.setStyleSheet(u"QPushButton\n"
"{\n"
"	margin-left: 25px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	margin-bottom: 11px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"img/chips/25.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chip25.setIcon(icon4)
        self.chip25.setIconSize(QSize(45, 45))
        self.chip50 = QPushButton(self.centralwidget)
        self.chip50.setObjectName(u"chip50")
        self.chip50.setGeometry(QRect(256, 230, 51, 51))
        self.chip50.setStyleSheet(u"QPushButton\n"
"{\n"
"	margin-left: 25px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	margin-bottom: 11px;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"img/chips/50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chip50.setIcon(icon5)
        self.chip50.setIconSize(QSize(45, 45))
        self.chip100 = QPushButton(self.centralwidget)
        self.chip100.setObjectName(u"chip100")
        self.chip100.setGeometry(QRect(306, 230, 51, 51))
        self.chip100.setStyleSheet(u"QPushButton\n"
"{\n"
"	margin-left: 30px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	margin-bottom: 11px;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"img/chips/100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chip100.setIcon(icon6)
        self.chip100.setIconSize(QSize(45, 45))
        self.chips_image = QLabel(self.centralwidget)
        self.chips_image.setObjectName(u"chips_image")
        self.chips_image.setGeometry(QRect(376, 205, 61, 71))
        self.chips_image.setPixmap(QPixmap(u"img/chips.png"))
        self.chips_image.setScaledContents(True)
        self.rate = QLabel(self.centralwidget)
        self.rate.setObjectName(u"rate")
        self.rate.setGeometry(QRect(450, 210, 111, 71))
        self.rate.setStyleSheet(u"font: 20pt \"Old English Text MT\";\n"
"color: white;\n"
"border-radius: 20px;")
        self.reset_rate_button = QPushButton(self.centralwidget)
        self.reset_rate_button.setObjectName(u"reset_rate_button")
        self.reset_rate_button.setGeometry(QRect(370, 276, 61, 51))
        self.reset_rate_button.setStyleSheet(u"QPushButton\n"
"{\n"
"	margin-left: 20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	margin-top: 7px;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"img/reset_rate1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reset_rate_button.setIcon(icon7)
        self.reset_rate_button.setIconSize(QSize(51, 51))
        self.settings_button = QPushButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(840, 6, 75, 51))
        self.settings_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	margin:0;\n"
"	margin-top: 7px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"img/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon8)
        self.settings_button.setIconSize(QSize(32, 32))
        self.settings_box = QWidget(self.centralwidget)
        self.settings_box.setObjectName(u"settings_box")
        self.settings_box.setGeometry(QRect(970, 60, 191, 551))
        self.settings_box.setStyleSheet(u"background-image: url(\"img/settings_background.jpg\");\n"
"border-radius: 20px;\n"
"")
        self.settings21 = QLabel(self.settings_box)
        self.settings21.setObjectName(u"settings21")
        self.settings21.setGeometry(QRect(10, 410, 171, 121))
        self.settings21.setPixmap(QPixmap(u"img/21.png"))
        self.settings21.setScaledContents(True)
        self.ace = QLabel(self.settings_box)
        self.ace.setObjectName(u"ace")
        self.ace.setGeometry(QRect(20, 20, 41, 51))
        self.ace.setPixmap(QPixmap(u"img/aces2.png"))
        self.ace.setScaledContents(True)
        self.checkBox = QCheckBox(self.settings_box)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(70, 38, 111, 16))
        self.checkBox.setStyleSheet(u"color: white;\n"
"font: 11pt \"Comic Sans MS\";\n"
"background: none;")
        self.table = QLabel(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(30, 60, 901, 551))
        self.table.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
"border-radius: 30px;\n"
"border: 10px solid #553010")
        self.deck = QPushButton(self.centralwidget)
        self.deck.setObjectName(u"deck")
        self.deck.setGeometry(QRect(800, 300, 63, 85))
        self.deck.setCursor(QCursor(Qt.OpenHandCursor))
        self.deck.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	margin-left: 0px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"img/deck/63x85/\u0440\u0443\u0431\u0430\u0448\u043a\u04301.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deck.setIcon(icon9)
        self.deck.setIconSize(QSize(63, 85))
        self.blackjack = QLabel(self.centralwidget)
        self.blackjack.setObjectName(u"blackjack")
        self.blackjack.setGeometry(QRect(50, 320, 441, 161))
        self.blackjack.setPixmap(QPixmap(u"img/blackjack.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.table.raise_()
        self.more_button.raise_()
        self.enough_button.raise_()
        self.balance.raise_()
        self.play_button.raise_()
        self.dealer.raise_()
        self.dcard1.raise_()
        self.dcard2.raise_()
        self.dcard3.raise_()
        self.dcard4.raise_()
        self.dcard5.raise_()
        self.dcard6.raise_()
        self.dcard7.raise_()
        self.dcard8.raise_()
        self.dcard9.raise_()
        self.dcard10.raise_()
        self.dcard11.raise_()
        self.ucard1.raise_()
        self.ucard2.raise_()
        self.ucard3.raise_()
        self.ucard4.raise_()
        self.ucard5.raise_()
        self.ucard6.raise_()
        self.ucard7.raise_()
        self.ucard8.raise_()
        self.ucard9.raise_()
        self.ucard10.raise_()
        self.ucard11.raise_()
        self.dpoints.raise_()
        self.upoints.raise_()
        self.information_block.raise_()
        self.ace_button_1.raise_()
        self.ace_button_11.raise_()
        self.label.raise_()
        self.dialog.raise_()
        self.close_button.raise_()
        self.chip1.raise_()
        self.chip5.raise_()
        self.chip25.raise_()
        self.chip50.raise_()
        self.chip100.raise_()
        self.chips_image.raise_()
        self.rate.raise_()
        self.reset_rate_button.raise_()
        self.settings_button.raise_()
        self.settings_box.raise_()
        self.deck.raise_()
        self.blackjack.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0413\u0420\u0410 21", None))
        self.more_button.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0429\u0401", None))
        self.enough_button.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0412\u0410\u0422\u0418\u0422", None))
        self.balance.setText("")
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0414\u0410\u0422\u042c", None))
        self.dealer.setText("")
        self.dcard1.setText("")
        self.dcard2.setText("")
        self.dcard3.setText("")
        self.dcard4.setText("")
        self.dcard5.setText("")
        self.dcard6.setText("")
        self.dcard7.setText("")
        self.dcard8.setText("")
        self.dcard9.setText("")
        self.dcard10.setText("")
        self.dcard11.setText("")
        self.ucard1.setText("")
        self.ucard2.setText("")
        self.ucard3.setText("")
        self.ucard4.setText("")
        self.ucard5.setText("")
        self.ucard6.setText("")
        self.ucard7.setText("")
        self.ucard8.setText("")
        self.ucard9.setText("")
        self.ucard10.setText("")
        self.ucard11.setText("")
        self.dpoints.setText("")
        self.upoints.setText("")
        self.information_block.setText("")
        self.ace_button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.ace_button_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label.setText("")
        self.dialog.setText("")
        self.close_button.setText("")
        self.chip1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.chip5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.chip25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.chip50.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.chip100.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.chips_image.setText("")
        self.rate.setText("")
        self.reset_rate_button.setText("")
        self.settings_button.setText("")
        self.settings21.setText("")
        self.ace.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"smart select", None))
        self.table.setText("")
        self.deck.setText("")
        self.blackjack.setText("")
    # retranslateUi

