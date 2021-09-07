"""
Задание 3:
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

Исползую enumerate, но можно и обходить массив по индексам for i in range(n):
"""

from random import random

n = int(input('Введите длину массива: '))
a = []
for i in range(n):
    a.append(int(random()*100))

print('Исходный массив: ')
print(a)

max_num = a[0]
max_ind = 0
min_num = a[0]
min_ind = 0
for ind, x in enumerate(a):
    if x > max_num:
        max_num = x
        max_ind = ind
    if x < min_num:
        min_num = x
        min_ind = ind

print(f'Максимальное значение = {max_num}')
print(f'Минимальное значение = {min_num}')

a[max_ind] = min_num
a[min_ind] = max_num

print('Массив после замены значений: ')
print(a)