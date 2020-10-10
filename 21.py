from random import shuffle, choice
from pprint import pprint
from time import sleep

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation, QRect
# импортируем связанный py файл с нашим ui файлом
from design_21 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # спрячем заголовок окна
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # соберём списки посадочных мест для карт
        # игрок
        self.ucards_seats = list()
        for i in range(1, 12):
            exec(f'self.ucards_seats.append(self.ui.ucard{i})')
        # крупье
        self.dcards_seats = list()
        for i in range(1, 12):
            exec(f'self.dcards_seats.append(self.ui.dcard{i})')

        # получим перемешанную колоду карт
        self.deck = self.get_deck()

        # обнулим ставку
        self.reset_rate()

        # проверим баланс
        self.balance = 100
        self.ui.balance.setText(str(self.balance))

        # спрячем ненужные кнопки
        self.ui.ace_button_1.hide()
        self.ui.ace_button_11.hide()
        self.information_bloсk(False)
        self.ui.blackjack.hide()

        # блок с настройками
        self.settings_anim = QPropertyAnimation(self.ui.settings_box, b"geometry")
        self.settings_anim.setDuration(900)
        self.settings_button = False

        # Добавим действие при нажатии на кнопки
        self.ui.play_button.clicked.connect(self.pushed_button_play)
        self.ui.more_button.clicked.connect(self.pushed_button_more)
        self.ui.enough_button.clicked.connect(self.pushed_button_enough)
        self.ui.ace_button_1.clicked.connect(self.pushed_button_ace_1)
        self.ui.ace_button_11.clicked.connect(self.pushed_button_ace_11)
        self.ui.close_button.clicked.connect(self.pushed_button_close)
        self.ui.reset_rate_button.clicked.connect(self.reset_rate)
        self.ui.settings_button.clicked.connect(self.pushed_button_settings)
        self.ui.chip1.clicked.connect(self.pushed_button_chip)
        self.ui.chip5.clicked.connect(self.pushed_button_chip)
        self.ui.chip25.clicked.connect(self.pushed_button_chip)
        self.ui.chip50.clicked.connect(self.pushed_button_chip)
        self.ui.chip100.clicked.connect(self.pushed_button_chip)
    
    # нажата кнопка с фишкой
    def pushed_button_chip(self):
        button = self.sender()
        self.rate += int(button.text())
        self.ui.rate.setText(str(self.rate))


    # кнопка НАСТРОЙКИ
    def pushed_button_settings(self):
        
        if not self.settings_button:

            self.settings_anim.setStartValue(QRect(970, 60, 191, 551))
            self.settings_anim.setEndValue(QRect(740, 60, 191, 551))
            self.settings_button = True
        else:

            self.settings_anim.setStartValue(QRect(740, 60, 191, 551))
            self.settings_anim.setEndValue(QRect(970, 60, 191, 551))
            self.settings_button = False
        
        self.settings_anim.start()

    # кнопка СДАТЬ
    def pushed_button_play(self):
        if self.rate == 0:
            self.information_bloсk('Сделайте вашу ставку')
        elif self.rate > self.balance:
            self.information_bloсk('Ваша ставка слишком большая')
        else:
            self.ui.play_button.setEnabled(False)
            for i in range(11):
                self.ucards_seats[i].setText("")
                self.dcards_seats[i].setText("")
            self.enough_button_was_selected = False

            # спрячем кнопки выбора очков для туза
            self.ui.ace_button_1.hide()
            self.ui.ace_button_11.hide()
            self.information_bloсk(False)
            # покажем кнопки ещё и хватит
            self.ui.enough_button.show()
            self.ui.more_button.show()

            for i in range(11):
                self.ucards_seats[i].setText('')
            
            self.your_points = 0
            self.computer_points = 0
            self.your_move = 1
            self.computer_move = 1

            computer_card = self.deck.pop()
            self.computer_points += self.get_card_points(computer_card, True)
            self.ui.dpoints.setText(str(self.computer_points))

            self.ui.dcard1.setText(f'<img src="img/deck/63x85/{computer_card}.png" />')
            self.ui.dcard2.setText(f'<img src="img/deck/63x85/рубашка2.png" />')

            for i in range(2):
                your_card = self.deck.pop()
                self.your_points += self.get_card_points(your_card)
                self.ucards_seats[i].setText(f'<img src="img/deck/63x85/{your_card}.png" />')
            self.ui.upoints.setText(str(self.your_points))
            self.check_points()

    # кнопка  ЕЩЁ
    def pushed_button_more(self):
        self.your_move += 1
        your_card = self.deck.pop()
        self.your_points += self.get_card_points(your_card)
        self.ucards_seats[self.your_move].setText(f'<img src="img/deck/63x85/{your_card}.png" />')
        self.ui.upoints.setText(str(self.your_points))
        self.check_points()

    # кнопка  ХВАТИТ
    def pushed_button_enough(self):
        self.enough_button_was_selected = True
        while self.computer_points < 17:
            computer_card = self.deck.pop()
            self.computer_points += self.get_card_points(computer_card, True) 
            self.dcards_seats[self.computer_move].setText(f'<img src="img/deck/63x85/{computer_card}.png" />')
            self.computer_move += 1
        self.ui.dpoints.setText(str(self.computer_points))
        self.check_points()

    def ace_selected(self):
        # спрячем кнопки выбора очков для туза
        self.ui.ace_button_1.hide()
        self.ui.ace_button_11.hide()
        # покажем кнопку ещё
        self.ui.more_button.show()
        # разблокируем кнопки ещё и сдать
        self.ui.enough_button.setEnabled(True)
        self.ui.play_button.setEnabled(True)
        # покажем очки
        self.ui.upoints.setText(str(self.your_points))
        
    # метод при нажатии на кнопку туз 1
    def pushed_button_ace_1(self):
        self.your_points += 1
        self.ace_selected()

    # метод при нажатии на кнопку туз 11
    def pushed_button_ace_11(self):
        self.your_points += 11
        self.ace_selected()

    # метод получения перемешанной колоды карт
    def get_deck(self):
        deck = []
        
        for suit in ['пики', 'червы', 'бубны', 'трефы']:
            for card in range(2,11):
                deck.append(f'{card} {suit}')
            for card in ['валет', 'дама', 'король', 'туз']: 
                deck.append(f'{card} {suit}')
        
        shuffle(deck)
        return deck

    # метод получения очков для определённой карты
    def get_card_points(self, card, computer=False):
        my_card = card.split()

        card_points = {}
        for card in range(2, 11):
            card_points[f'{card}'] = card
        for card in ['валет', 'дама', 'король']: 
            card_points[f'{card}'] = 10

        if my_card[0] == 'туз':
            if computer == True:
                points = choice([1,11])
            else:
                self.ui.more_button.hide()
                self.ui.ace_button_1.show()
                self.ui.ace_button_11.show()
                points = self.your_points
                # блокируем кнопки
                self.ui.enough_button.setEnabled(False)
                self.ui.play_button.setEnabled(False)
        else:
            points = card_points[my_card[0]]
        
        return points

    # метод прячет/показывает основные кнопки 
    def hide_main_buttons(self):
        # спрячем кнопки ещё и хватит
        self.ui.more_button.hide()
        self.ui.enough_button.hide()
        
    # метод прячет/показывает блок с информацией
    def information_bloсk(self, message):
        if message:
            self.ui.dialog.show()
            self.ui.information_block.setText(message)
        else:
            self.ui.dialog.hide()
            self.ui.information_block.setText("")

    # обнуление ставки
    def reset_rate(self):
        self.rate = 0
        self.ui.rate.setText('0')

    # метод для закрытия программы
    def pushed_button_close(self):
        self.close()

    def check_points(self):
        
        if self.your_points > 21:
            self.information_bloсk('ПЕРЕбОР!!!')
            self.hide_main_buttons()
            # balance = balance - deposit

        elif self.your_points == 21:
            self.pushed_button_enough()
        
        if self.enough_button_was_selected:
            if self.computer_points == self.your_points:
                self.information_bloсk('НИЧЬЯ!!!')
                self.hide_main_buttons()
            elif self.computer_points > 21:
                self.information_bloсk('ВЫ ВЫИГРАЛИ!!!')
                self.hide_main_buttons()
                # balance = balance + deposit
            elif self.computer_points > self.your_points:
                self.information_bloсk('ВЫ ПРОИГРАЛИ!!!')
                self.hide_main_buttons()
                # balance = balance - deposit
            elif self.your_points > self.computer_points:
                self.information_bloсk('ВЫ ВЫИГРАЛИ!!!')
                self.hide_main_buttons()
                # balance = balance + deposit


if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())







#     if play_first == True:
#         print(f'Баланс: {balance}$')
#         play_first = False
    
#     if balance == 0:
#         print("Вы банкрот!")
#         sleep(4)
#         exit()
    
#     deposit = int(check_digit(input('Ваша ставка?\n')))
#     while deposit > balance:
#         deposit = int(check_digit(input("Ваша ставка слишком большая\n")))
    



#     print(f'Баланс: {balance}$')
#     play_again = check_user_input(input('Играть ещё?\n'), ['да', 'нет'])
  