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
    play_again = input()

if ready == "да":
    
    questions_quantity = ""  # количество примеров
    max_answer = ""  #  до скольки будем считать

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
else:
    print("""Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!""")
