def my_func(arg1, arg2, arg3):
    """
    Возвращает сумму наибольших двух аргументов

    :param arg1:
    :param arg2:
    :param arg3:
    :return:
    """
    list_arg = sorted([arg1, arg2, arg3])
    print(list_arg)
    return list_arg[2] + list_arg[1]

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


resultant = my_func(chek_input(1), chek_input(2), chek_input(3))
print(resultant)