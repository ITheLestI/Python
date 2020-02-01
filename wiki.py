import wikipedia
wikipedia.set_lang("ru")

while True:
    search = input('Что искать\n')
    s = wikipedia.page(search)
    print(s.content)