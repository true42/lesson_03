def sum_sum(a):
    x = input('Для выхода нажмите "Q".\nВведите числа через пробел, которые хотите суммировать: ').lower().split()
    for i in x:
        if i == 'q':
            return a
        else:
            try:
                a += int(i)
            except ValueError:
                print('Поздравляю, ваши данные обнулились!\n А теперь введите ЧИСЛА через ПРОБЕЛ')
                return sum_sum(0)
    print(a)
    return sum_sum(a)


print(sum_sum(0))