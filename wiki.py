import wikipedia
wikipedia.set_lang("ru")

while True:

    try:
        search = input('Что искать\n')
        if search == 'стоп':
            break
        s = wikipedia.page(search)
        print(s.content)
    except:
        s = wikipedia.search(search)
        print("Такой страницы не найдено. Возможно Вы имели ввиду:")
        print("===================================================")
        for item in s:
            print(item)
        print("===================================================")
        print()