"""
Задание 7:
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться
"""
from random import random

n = int(input('Введите длину массива: '))
a = []
for i in range(n):
    a.append(int(random()*100))

# Перебор списка 2 раза
min_num = a[0]
print(a)
min_ind = 0
for ind, n in enumerate(a):
    if n <= min_num:
        min_num = n
        min_ind = ind
print(min_num)

if min_ind == 0:
    min_num = a[1]
else:
    min_num = a[0]

for ind, n in enumerate(a):
    if ind != min_ind:
        if n <= min_num:
            min_num = n
print(min_num)


# Читерские способы. При условии, что длина массива >= 2
# 1
print(a)
print(sorted(a)[:2])

# 2
min_num = min(a)
print(min_num)
a.remove(min_num)
min_num = min(a)
print(min_num)