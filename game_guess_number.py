# Игра "Угадай число"
import random

play_again = 'да'
print('Привет! Как тебя зовут?')
name = input()
name = name.title()

def endings(digit):
    if digit == 1:
        return "ку"
    elif digit in {2, 3, 4}:
        return "ки"
    elif digit in {5, 6, 7, 8, 9}:
        return "ок"


def guessNumber():
    print('Что ж ' + name + ', я загадываю число от 1 до 20.')

    number = random.randint(1, 20)
    counter = 0

    for counter in range(6):
        if counter == 0:
            print('Попробуй угадать:')
        else:
            print('Попробуй ещё раз')

        guess_number = int(input())

        if guess_number > number:
            print('Твоё число слишком большое')
        if guess_number < number:
            print('Твоё число слишком маленькое')
        if guess_number == number:
            break

    if guess_number == number:
        counter = str(counter+1)
        print('Отлично, '+name+'! Ты справился за '+counter+' попыт'+endings(int(counter)))
    if guess_number != number:
        number = str(number)
        print('Увы. Я загадала число '+number)

while play_again == "да":
    guessNumber()
    print("Сыграем еще?")
    play_again = input()
    play_again = play_again.lower()
    while play_again not in {'да', "нет"}:
        print("Введи да или нет")
        play_again = input()