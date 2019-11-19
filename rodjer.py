from random import randint, choice
from timeit import default_timer
from os import path

# функция для выбора режима работы
def select_mode():

    if not path.exists(file_name):
        print("""Выбери режим игры:
        1 - обычная тренировка
        """)
        mode = input()
    else:
        print("""Выбери режим игры:
        1 - обычная тренировка
        2 - работа над ошибками""")
        mode = input()

    while mode not in {"1", "2"}:
        print("Введи 1 или 2")
        mode = input()

    return mode


# функция временных окончаний
def time_endings(digit):
    digit = str(digit)
    last_digit = int(digit[-1])
    if 5 < last_digit < 10 or last_digit == 0:
        return ''
    else:
        if last_digit == 1:
            return "у"
        else:
            return "ы"


# функция перевода секунд в минуты и секунды
def seconds_convert(time_in_seconds):
    if time_in_seconds<60:
        time_spent = f"{time_in_seconds} секунд{time_endings(time_in_seconds)}"
    else:
        minutes = str(round(time_in_seconds/60))
        seconds =str(time_in_seconds-(int(minutes)*60))

        if seconds == 0:
            time_spent = f"{minutes} минут{time_endings(minutes)}"
        else:
            time_spent = f"{minutes} минут{time_endings(minutes)} и {seconds} секунд{time_endings(seconds)}"

    return time_spent


# функция вывода примеров, их проверки и формирования файла с ошибками
def count():
    print('Давай проверим твои знания в математике')    
         
    questions_quantity = ""  # количество примеров
    max_answer = ""  #  до скольки будем считать
    mistakes = 0
    correct_answers = 0
    answers_time = 0

    while not questions_quantity.isdigit():
        print("Сколько примеров ты готов решить?")
        questions_quantity = input()

        if questions_quantity.isdigit():
            while int(questions_quantity) < 1:
                print("Число должно быть больше нуля")
                questions_quantity = input()
                while not questions_quantity.isdigit():
                    print("Должна быть цифра")
                    questions_quantity = input()
        else:    
            print("Должна быть цифра")
    
    while not max_answer.isdigit():
        print("До скольки будем считать?")
        max_answer = input()

        if max_answer.isdigit():
            while int(max_answer) < 2:
                print("Число должно быть больше одного")
                max_answer = input()
                while not max_answer.isdigit():
                    print("Должна быть цифра")
                    max_answer = input()
        else:    
            print("Должна быть цифра")
    
    for i in range(int(questions_quantity)):
        print(f"Пример {i+1}")
        first = randint(1, int(max_answer))
        second = randint(1, int(max_answer))
        sign = choice("+-")
        
        if sign == '-':
            while first<second:
                first = randint(1, int(max_answer))
                second = randint(1, int(max_answer))
            correct = first-second
        
        if sign == "+":
            while first+second>int(max_answer):
                first = randint(1, int(max_answer))
                second = randint(1, int(max_answer))
            correct = first+second

        
        print(first, sign, second)
        start =  default_timer()
        answer = input()
        stop = default_timer()
        answers_time += round(stop-start)

        while not answer.isdigit():
            print("Должна быть цифра")
            start =  default_timer()
            answer = input()
            stop = default_timer
            answers_time+=stop-start
            
        
        if int(answer) == correct:
            print("Правильно, молодец!")
            print("")
            correct_answers+=1
        else:
            # создадим файл для записи ошибок
            with open(file_name, 'a') as f:
                f.write(f"{first} {sign} {second}\n")

            print("Неправильно")
            print(f"Правильный ответ: {correct}")
            print("")
            mistakes+=1

    if mistakes == 0:
        print("Молодец, " +name+ ". Ты правильно ответил на все вопросы за " + seconds_convert(answers_time))
    else:
        print("Правильных ответов: "+str(correct_answers))
        print("Неправильных ответов: "+str(mistakes))
        print("затраченное время - " + seconds_convert(answers_time))


# функция работы над ошибками
def fix_errors():
    print('работа над ошибками')

# основной блок программы    
print("Привет, меня зовут Роджер, а как тебя?")
name = input()
print(f"Приятно познакомиться, {name.title()}")

file_name = f"{name.lower()}_errors.txt"

# выберем режим работы
mode = select_mode()

if mode == '1':
    count()
elif mode == '2':
    fix_errors()

