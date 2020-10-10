import currency_exchange
from translate import Translator

#currency_list
cl = currency_exchange.currencies()
ru_cl = {}
translator = Translator(to_lang="ru")

for i in cl:
    ru_cl[translator.translate(i[6:]).title()] = i[:3]
print(ru_cl)
