def my_func(x, y):
    return x**y


def my_func_2(x, y):
    x_copy = x
    for exponentiation in range(-1*y-1):
        x_copy *= x
    return 1/x_copy


print(my_func(4, -2))
print(my_func_2(4, -2))