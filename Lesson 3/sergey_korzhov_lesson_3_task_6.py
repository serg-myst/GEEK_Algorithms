"""
Задание 6:
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать

Сначала найдем индексы минимального и максимального элементов массива - 1-ый цикл
Пробежимся между полученными индексами и найдем сумму - 2-ой цикл
"""

from random import random

n = int(input('Введите длину массива: '))
a = []
for i in range(n):
    a.append(int(random()*100))

max_num = a[0]
max_ind = 0
min_num = a[0]
min_ind = 0
sum = 0
for ind, x in enumerate(a):
    if x > max_num:
        max_num = x
        max_ind = ind
    if x < min_num:
        min_num = x
        min_ind = ind

for i in range(min(min_ind, max_ind)+1, max(min_ind, max_ind)):
    sum += a[i]
print(f'Сумма элементов = {sum}')