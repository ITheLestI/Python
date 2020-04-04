def check_digit(user_input: str, your_warning: str = '') -> str:
    """
    функция проверки ввода числа

        описание функциии
    
        :param str user_input: пользовательский ввод
        :return: str
    """
    while not user_input.isdigit():
        if your_warning:
            print(your_warning)
        else:
            print('Должна быть цифра')

        user_input = input()

    return user_input


# функция проверки введённых данных в соответствии со списком допустимых вариантов
def check_input(user_input: str, acceptable_list: list, default_warning: bool = False) -> str:
    user_input = user_input.lower()
    # сформируем строку с допустимыми данными
    items = ''
    for item in acceptable_list[:-1]:
        items += f'{item}, '

    items = items[:-2]
    items += f' или {acceptable_list[-1]}'

    # если ничего не ввели, сохраним предыдущие настройки
    acceptable_list.append('')

    while user_input not in acceptable_list:
        if user_input not in acceptable_list:
            if default_warning:
                print()
                print('Некорректные символы')
            else:
                print()
                print(f'Должно быть {items}')
        user_input = input('Введите заново:\n')

    # вернём выбранный вариант
    return user_input