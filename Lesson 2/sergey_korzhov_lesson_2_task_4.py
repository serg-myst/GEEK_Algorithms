"""
Задание 4:
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Please, enter number: '))
sum_n = 0
start_num = 1
for i in range(n):
    if i % 2 != 0:
        sum_n += start_num
    else:
        sum_n -= start_num
    start_num /= 2
print(sum_n)