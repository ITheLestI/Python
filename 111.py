
a = [i for i in s if i.isdigit()]

def summa(*args):
    
    summa = 0
    for i in args:
        summa+=i
    print('Сумма равна ',summa)


def my_test(*args,**kargs):
    print(kargs)
    print(args)

my_test(a=20, b=30)

#[] - список с ключами 0, 1, -1
#{} - словарь с задаваемыми ключами или можество(=список, но нет повторений)
#() - кортеж константный список

