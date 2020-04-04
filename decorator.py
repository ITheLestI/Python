from timeit import default_timer


# функция-декоратор для получения времени выполнения любой функции
def show_time(func):
    # функция-обёртка
    def wrapper(*args, **kwargs):

        start = default_timer()
        result = func(*args, **kwargs)  # вызов функции
        stop = default_timer()

        spent_time = f'{round(stop-start, 8)} seconds'
        print(spent_time)
        # вернём  результат выполнения функции
        return result

    return wrapper


# функция создания списка чётных чисел через цикл for
@show_time  # синтаксический сахар для вызова декоратора show_time(even_numbers1)
def even_numbers1(n):
    numbers = []
    for i in range(2, n+2, 2):
        numbers.append(i)
    return numbers


# функция создания списка чётных чисел через генератор списка
# @show_time
def even_numbers2(n):
    numbers = [i for i in range(2, n+2, 2)]
    return numbers


# вызов функции с использованием декоратора c синтаксическим сахаром @show_time
even_numbers1(10000000)

# прямое использование декоратора без синтаксического сахара @show_time
received_func = show_time(even_numbers2)
even_numbers_list = received_func(10000000)

# посмотрим типы объектов и имя полученной функции из декоратора
print(type(received_func), received_func.__name__)   # <class 'function'> wrapper
print(type(even_numbers_list))  # <class 'list'>

# или альтернативная запись
even_numbers_list = show_time(even_numbers2)(10000000)  # wrapper(10000000) => even_numbers2(10000000)

# ====================================================================================================
# если нам нужно передать какие-либо аргументы в сам декоратор:


# функция-декоратор для получения времени выполнения функции с аргументами
def show_time_with_arguments(arg):
    print(arg)  # выведем на экран аргумент

    # функция-обёртка 1
    def outer(func):
        # функция-обёртка 2
        def wrapper(*args, **kwargs):

            start = default_timer()
            result = func(*args, **kwargs)  # вызов функции
            stop = default_timer()

            spent_time = f'{round(stop-start, 8)} seconds'
            print(spent_time)
            # вернём  результат выполнения функции
            return result

        return wrapper
    return outer


# прямое использование декоратора с аргументами без синтаксического сахара show_time_with_arguments
even_numbers_list_2 = show_time_with_arguments('my name')(even_numbers2)(10000000)
