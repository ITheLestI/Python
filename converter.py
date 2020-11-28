#! /usr/bin/env python
# -*- coding: utf-8 -*-
import currency_exchange
from translate import Translator
import json
import os
import sys
from lib import *
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
from math import floor
# импортируем связанный py файл с нашим ui файлом
from design_converter import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
		# вызовем метод родительского класса
        super(MainWindow, self).__init__()

        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Соединим сигналы со слотами
        self.ui.convert.clicked.connect(self.pushed_button)

        file_name = "currencies.json"


        if not os.path.exists(file_name):
            cl = currency_exchange.currencies()
            self.ru_cl = {}
            translator = Translator(to_lang="ru")

            for i in cl:
                self.ru_cl[translator.translate(i[6:]).title()] = i[:3]
            with open(file_name, "w", encoding="utf8") as f:
                json.dump(self.ru_cl, f, ensure_ascii=False)
        else:
            with open(file_name, "r", encoding='utf8') as f:
                self.ru_cl = json.load(f)
        
        currencies_list = []
        for i in self.ru_cl:
            currencies_list.append(i)

        currencies_list.sort()

        for i in currencies_list:
            self.ui.from_cur.addItem(i)
            self.ui.to_cur.addItem(i)

    # функция при нажатии на кнопку
    def pushed_button(self):
        result = ""
        b = []
        if check_digit(user_input=self.ui.amount.text(), ui=True):
            total = currency_exchange.exchange(self.ru_cl[self.ui.from_cur.currentText()], self.ru_cl[self.ui.to_cur.currentText()], self.ui.amount.text())
            a = total[0]
            #print(total)
            for i in a[:-4]:
                if i != ",":

                    b.append(i)              
            for i in b:
                result+=i
            self.ui.total.setText(f" Итого: {int(float(result))} {a[-4:]}")

if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
