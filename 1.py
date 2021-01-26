def division(arg1, arg2):
    """
    Производит деление arg1/arg2
    Возвращает итог деления

    :param Делимое число:
    :param Делитель:
    :return:
    """
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        print('Вы делите на 0. Так нельзя. Давай-те попробуем ещё раз.')
        return division(chek_input(1), chek_input(2))


def chek_input(number):
    """
    Проверяет, чтобы вводилось число.
    Возвращает введённое число

    :param number:
    :return:
    """
    try:
        input_integer = float(input(f"Введите {number}-е число: "))
        return input_integer
    except ValueError:
        print('Введите ЧИСЛО')
        return chek_input(number)


resultant = division(chek_input(1), chek_input(2))
print(resultant)
