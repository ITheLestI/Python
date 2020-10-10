#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
# импортируем связанный py файл с нашим ui файлом
from design_counter import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Соединим сигналы со слотами
        # self.ui.close_button.clicked.connect(self.close)
        self.ui.ok_button.clicked.connect(self.ok)

        self.counter = 0

    # функция при нажатии на кнопку
    def ok(self):
        window.setStyleSheet(u"QMainWindow\n"
"{\n"
f"	background-color: rgb({randint(0, 220)}, {randint(0, 220)}, {randint(0, 220)});\n"
"}\n"
"QPushButton:selected\n"
"{\n"
	"outline: none;\n"
"}\n"
"QPushButton:active\n"
"{\n"
	"outline: none;\n"
"}\n"

        )
        self.counter += 1 
        self.ui.counter.setText(str(self.counter))



if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
