import random
from time import sleep

name = input('Как тебя зовут?\n')
name = name.title()

play_again = 'да'
while play_again == 'да':
    
    play_to = input(f'{name}, до скольки загадать мне число?\n')
    while not play_to.isdigit():
        print('Должна быть цифра.')
        play_to = input()
    play_to = int(play_to)

    print(f'Хорошо, {name}, я загадываю число от 1 до {play_to}')
    number = random.randint(1, play_to)

    print('У тебя есть 6 попыток')

    for i in range(6):

        user_number = ''
        while not user_number.isdigit():
            print(f'попытка {i+1}:')
            user_number = input()
            if not user_number.isdigit():
                print('Должна быть цифра.')
        user_number = int(user_number)

        if user_number != number:
            if user_number < number:
                print("Твоё число слишком маленькое")
            else:
                print("Твоё число слишком большое")
            if i == 5:
                print(f'''Твои попытки закончились, ты проиграл!!!
Я загадал число {number}''')
        else:
            print(f"Ты угадал за {i+1} попыток!!!")
            break
    print('Сыграем ещё? да или нет')
    play_again = input()
    while play_again not in {'да', 'нет'}:
        print('Должно быть \'да\' или \'нет\'')
        play_again = input()

print(f'До скорой встречи, {name}!!!')
sleep(1)