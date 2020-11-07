#! /usr/bin/env python
# -*- coding: utf-8 -*-
import currency_exchange
from translate import Translator
import json
import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
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
            ru_cl = {}
            translator = Translator(to_lang="ru")

            for i in cl:
                ru_cl[translator.translate(i[6:]).title()] = i[:3]
            with open(file_name, "w", encoding="utf8") as f:
                json.dump(ru_cl, f, ensure_ascii=False)
        else:
            with open(file_name, "r", encoding='utf8') as f:
                ru_cl = json.load(f)
        
        currencies_list = []
        for i in ru_cl:
            currencies_list.append(i)

        currencies_list.sort()

        for i in currencies_list:
            self.ui.from_cur.addItem(i)
            self.ui.to_cur.addItem(i)

    # функция при нажатии на кнопку
    def pushed_button(self):
        pass


        #total = currency_exchange.exchange(, )


if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
