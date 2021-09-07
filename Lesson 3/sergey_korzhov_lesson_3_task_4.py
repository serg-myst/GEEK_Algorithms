"""
Задание 3:
Определить, какое число в массиве встречается чаще всего.

План такой. Сворачиваем до уникальных значенй в массиве. В этом нам поможет множество set(a)
Пробегаемся по множеству и считаем сколько раз цифра встречается в исходном массиве a.count(n)
"""

a = [1, 2, 1, 3, 34, 1, 5, 2, 1, 2, 6, 2, 2, 2, 2, 3]
max_count = 0
max_ind = -1
for i, n in enumerate(set(a)):
    if a.count(n) > max_count:
        max_count = a.count(n)
        max_ind = i
print(f'Цифра {a[max_ind]} встретилась больше всего ({max_count}) раз')

# Что и выше только через лямбду
print(max(set(a), key=lambda x: a.count(x)))
