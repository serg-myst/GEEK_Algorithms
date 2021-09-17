"""
Задание 2:
Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

"""
Анализ используемой памяти показывает, что второй вариант будет эффективнее, особеннно при вводе мегабольших строк
Память, отведенная под пользовательскую переменную с каждым циклом будет только уменьшаться
Это видно и по общей затраченной памяти
Интересный момент под переменные sum_even, sum_odd изначачально выделено 28 байт и хранятся они в одной ячейке.
Это видно по ID. После присваения значений переменные складываютяс в разные ячейки. Получается, что объем памяти
увеличивается.
"""

import sys


def get_size(obj):
    return sys.getsizeof(obj)


num = int(input('Please, enter number: '))

print(f'Число пользователя до цикла: {get_size(num)} id = {id(sum)}')

sum_even = 0
sum_odd = 0

print(f'Память под четные цифры до цикла: {get_size(sum_even)} id = {id(sum_even)}')
print(f'Память под нечетные цифры до цикла: {get_size(sum_odd)} id = {id(sum_odd)}')

for i in str(num):
    if int(i) % 2 == 0:
        sum_even += 1
    else:
        sum_odd += 1

_a = get_size(num)
_b = get_size(sum_even)
_c = get_size(sum_odd)
_d = _a + _b + _c

print(f'Число пользователя после цикла: {_a} id = {id(sum)}')
print(f'Память под четные цифры после цикла: {_b} id = {id(sum_even)}')
print(f'Память под нечетные цифры после цикла: {_c} id = {id(sum_odd)}')
print(f'Всего затрачено памяти: {_d}')

print(f'Четных {sum_even}')
print(f'Нечетных {sum_odd}')


# Цикл без преобразования в строку
num = int(input('Please, enter number: '))

print(f'Число пользователя до цикла: {get_size(num)} id = {id(sum)}')

sum_even = 0
sum_odd = 0

print(f'Память под четные цифры до цикла: {get_size(sum_even)} id = {id(sum_even)}')
print(f'Память под нечетные цифры до цикла: {get_size(sum_odd)} id = {id(sum_odd)}')

while num > 0:
    if num % 2 == 0:
        sum_even += 1
    else:
        sum_odd += 1
    num = num // 10

_a = get_size(num)
_b = get_size(sum_even)
_c = get_size(sum_odd)
_d = _a + _b + _c

print(f'Число пользователя после цикла: {_a} id = {id(sum)}')
print(f'Память под четные цифры после цикла: {_b} id = {id(sum_even)}')
print(f'Память под нечетные цифры после цикла: {_c} id = {id(sum_odd)}')
print(f'Всего затрачено памяти: {_d}')

print(f'Четных {sum_even}')
print(f'Нечетных {sum_odd}')