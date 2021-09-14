"""
Задание 1:
Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков


Задание из предыдущего урока:
Определить, какое число в массиве встречается чаще всего.

Делаем замеры двух вариантов решения
Воспользуемся модулем time и просто засечем время старта и время завершения процедуры.
Разница даст нам время выполнения
Также сделаем замер через cProfile

Вывод:
На больших массивах вариант 2 работает быстрее
"""

import time
from random import random
import cProfile


def new_massive(n):
    a = []
    for i in range(n):
        a.append(int(random() * 100))
    return a


def option_1(a):
    b = time.time()
    max_count = 0
    max_ind = 0
    for n in set(a):
        if a.count(n) > max_count:
            max_count = a.count(n)
            max_ind = n
    e = time.time()
    print(f'Цифра {max_ind} встретилась больше всего ({max_count}) раз')
    # print(f'Время выполнения {e - b}')


def option_2(a):
    b = time.time()
    print(max(set(a), key=lambda x: a.count(x)))
    e = time.time()
    print(f'Время выполнения {e - b}')


n = int(input('Введите размер массива: '))
a = new_massive(n)
option_1(a)
option_2(a)

cProfile.run('option_1(a)')
cProfile.run('option_2(a)')

"""
Вариант 1:

Результаты замера time.time()
массив 100000 элементов - 0.0932302474975586
массив 1000000 элементов - 0.9224550724029541
массив 10000000 элементов - 8.743255853652954
массив 100000000 элементов - 95.87899827957153

Результаты замера cProfile
массив 100000 элементов:
103    0.090    0.001    0.090    0.001 {method 'count' of 'list' objects}
массив 1000000 элементов:
103    0.899    0.009    0.899    0.009 {method 'count' of 'list' objects}
массив 10000000 элементов:
109    9.301    0.085    9.301    0.085 {method 'count' of 'list' objects}
массив 100000000 элементов:
105   91.420    0.871   91.420    0.871 {method 'count' of 'list' objects} 

Вариант 2:

Результаты замера time.time()
массив 100000 элементов - 0.08820986747741699
массив 1000000 элементов - 0.879338264465332
массив 10000000 элементов - 8.720167875289917
массив 100000000 элементов - 90.26142382621765

Результаты замера cProfile
массив 100000 элементов:
100    0.087    0.001    0.087    0.001 {method 'count' of 'list' objects}
массив 1000000 элементов:
100    0.868    0.009    0.868    0.009 {method 'count' of 'list' objects}
массив 10000000 элементов:
100    8.510    0.085    8.510    0.085 {method 'count' of 'list' objects}
массив 100000000 элементов:
100   85.491    0.855   85.491    0.855 {method 'count' of 'list' objects}
"""
