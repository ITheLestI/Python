from random import randint, choice
from timeit import default_timer
from os import path
import os
import json

def check_input(user_input, valid_list, hidden=''):
    while user_input not in valid_list:
        printable = "Должно быть "
        for item in valid_list[:-1]:
            if not item == hidden:
                printable += f'{item}, '
        
        printable = printable[:-2]
        printable += f" или {valid_list[-1]}."

         
        user_input = input(printable+'\n')   
    return user_input 

def settings():
    if not path.exists("settings.json"):
        settings = {
            "count_mode":"1"

        }

        with open("settings.json", "w") as f:
            json.dump(settings, f, ensure_ascii=False)


    with open("settings.json", "r") as f:
        settings = json.load(f)
        
    return settings


#настройки
def edit_settings():
    with open("settings.json", "r") as f, open("tmp_settings.json", "a") as f2:
        settings = json.load(f)
        print("""Текущие настройки
(1 - включено, 0 - выключено)
""")
        
        print(f"1.Вывод примеров без повторов - {settings['count_mode']}")
        print("0 - выход")
        print()
        setting_to_redact = check_input(input("Выберите настройку для редактирования: \n"), ["1", "0"])
        if setting_to_redact == '1':
            parameter = check_input(input("Ведите состояние 1 или 0: \n"), ["1","0"])
            
            settings["count_mode"] = parameter
        json.dump(settings,f2)
    os.remove("settings.json")
    os.rename("tmp_settings.json", "settings.json")



# функция чистки повторениий примеров
def cleanup():
    if path.exists(file_name):

        uniques = []
        with open(file_name, "r") as f, open(f"tmp_{file_name}", "a") as f2:
            
            for line in f:
                splited_line = line.split()
                number1, sign, number2, repeat = splited_line
                row = f"{number1} {sign} {number2}"
                
                if row not in uniques:
                    uniques.append(row)
                    f2.write(f"{number1} {sign} {number2} {repeat}\n")
        os.remove(file_name)
        os.rename(f"tmp_{file_name}", file_name)


# функция выбора оповещения неправильного ответа
def warnings():
    warnings = ["Неправильно", "Ты уверен?", "А голову дома не забыл?", "Сделай проверку"]
    return warnings[randint(0, len(warnings) - 1)]


# функция для выбора режима работы
def select_mode():

    if not path.exists(file_name):
        mode = check_input(input("""Выбери режим игры:
        1 - обычная тренировка
        0 - выход
        """),["1", "0", "dev"], 'dev')

    else:
        mode = check_input(input("""Выбери режим игры:
        1 - обычная тренировка
        2 - работа над ошибками
        0 - выход
        """),["1", "0", "2", "dev"], 'dev')

    

    return mode


# функция временных окончаний
def time_endings(digit):
    digit = str(digit)
    last_digit = int(digit[-1])
    prelast_digit = int(digit[-2])
    if 5 < last_digit < 10 or last_digit == 0 :
        return ''
    else:
        if last_digit == 1:
            if prelast_digit == 1:
                return ""
            else:
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
    uniques = []
    task_number = 0

    count_mode = settings()

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
    

    #сделать остановку для цикла while по количеству возможных вариантов
    possible_questions = max_answer**2
    if count_mode[count_mode] == 1:
        if possible_questions <= questions_quantity:
        
            print(f"Такого кол-ва различных примеров не существует, выберете не больше {possible_questions}")
            questions_quantity = input()            
            while not questions_quantity.isdigit():
                print("Введите число")
                questions_quantity = input()        
            
            while task_number != questions_quantity: 
        
        
                for i in range(int(questions_quantity)):
                
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

                    row = f"{first} {sign} {second}"
                    while row not in uniques:
                        uniques.append(row)
                        task_number+=1
                        print(f"Пример {task_number}")        
                        print(first, sign, second)
                        start =  default_timer()
                        answer = input()
                        stop = default_timer()
                        answers_time += round(stop-start)

                        while not answer.isdigit():
                            print("Должна быть цифра")
                            start =  default_timer()
                            answer = input()
                            stop = default_timer()
                            answers_time += round(stop-start)
                            
                        
                        if int(answer) == correct:
                            print("Правильно, молодец!")
                            print("")
                            correct_answers+=1
                        else:
                            # создадим файл для записи ошибок
                            with open(file_name, 'a') as f:
                                f.write(f"{first} {sign} {second} 3\n")

                            print(warnings())
                            print(f"Правильный ответ: {correct}")
                            print("")
                            mistakes+=1
                else:
                    
                    continue
    else:
        while task_number != questions_quantity: 
        
        
            for i in range(int(questions_quantity)):
                
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

                    task_number+=1
                    print(f"Пример {task_number}")        
                    print(first, sign, second)
                    start =  default_timer()
                    answer = input()
                    stop = default_timer()
                    answers_time += round(stop-start)

                    while not answer.isdigit():
                        print("Должна быть цифра")
                        start =  default_timer()
                        answer = input()
                        stop = default_timer()
                        answers_time += round(stop-start)
                        
                    
                    if int(answer) == correct:
                        print("Правильно, молодец!")
                        print("")
                        correct_answers+=1
                    else:
                        # создадим файл для записи ошибок
                        with open(file_name, 'a') as f:
                            f.write(f"{first} {sign} {second} 3\n")

                        print(warnings())
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
    with open(file_name, 'r') as f:
        line = f.readline()
        if path.exists(f"tmp_{file_name}"):
            os.remove(f"tmp_{file_name}")
        while line:
            splited_line = line.split()
            number1, sign, number2, repeat = splited_line
            
            if sign == "+":
                correct_answer = int(number1) + int(number2)
            if sign == "-":
                correct_answer = int(number1) - int(number2)

            print(number1, sign, number2)
            answer = input()
            while not answer.isdigit():
                print("Должна быть цифра")
                answer = input()
            
            
            

            if correct_answer == int(answer):
                print("Правильно!")
                repeat = int(repeat) - 1
            
                if repeat >= 1:                    
                    with open(f"tmp_{file_name}", "a") as f2:
                        f2.write(f"{number1} {sign} {number2} {repeat}\n")
            else:
                with open(f"tmp_{file_name}", "a") as f2:
                    f2.write(f"{number1} {sign} {number2} {repeat}\n")
                print(warnings())       

            line = f.readline()
        
    os.remove(file_name)
    os.rename(f"tmp_{file_name}", file_name)

            



# основной блок программы    
print("Привет, меня зовут Роджер, а как тебя?")
name = input()
print(f"Приятно познакомиться, {name.title()}")
file_name = f"{name.lower()}_errors.txt"


while True:
    # выберем режим работы
    mode = select_mode()

    if mode == '1':
        count()
    elif mode == 'dev':
        print("Режим разработчика")
        print("1 - cleanup")
        print("2 - settings")
        print("3 - edit settings")
        print("4 - check_input")
        mode = input()
        if int(mode) == 1:
            cleanup()
            print("Чистка файла с ошибками пользователя выполнена успешно")
        if int(mode) == 2:
            settings()
            print("Настройки порочитаны")
        if int(mode) == 3:
            edit_settings()
        if int(mode) == 4:
            check_input(input('введи что-то:'), ['1','2','ok'], "dev")
    elif mode == '2':
        fix_errors()
    elif mode == '0':
        break
