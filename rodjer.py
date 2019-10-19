from random import randint, choice
from timeit import default_timer


print("Привет, меня зовут Роджер, а как тебя?")
name = input()
name = name.title()
print(f"Приятно познакомиться, {name}")
print('''Давай проверим твои знания в математике
Ты готов?''')
ready = input()
ready = ready.lower()

while ready not in {'да', "нет"}:
    print("Введи да или нет")
    ready = input()

if ready == "да":
    
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
        stop = default_timer
        answers_time+=stop-start

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
            print("Неправильно")
            print(f"Правильный ответ: {correct}")
            print("")
            mistakes+=1
    

    if answers_time<60:
        time_spent = answers_time
    else:
        minutes = str(round(answers_time/60))
        seconds =str(answers_time-(minutes*60))
    



    if mistakes == 0:
        print("Молодец, " +name+ ". Ты правильно ответил на все вопросы.")
    else:
        print("Правильных ответов:"+str(correct_answers))
        print("Неправильных ответов:"+str(mistakes))
else:
    print("""Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!""")
