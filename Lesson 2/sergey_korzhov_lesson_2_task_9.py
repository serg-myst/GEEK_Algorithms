"""
Задание 9:
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

max_num = 0
max_sum = 0
while True:
    num = int(input('Введите число (для прекращения ввода нажимет 0): '))
    if num == 0:
        break
    n = num
    sum_n = 0
    while n > 0:
        sum += n % 10
        n //= 10
    if sum_n > max_sum:
        max_sum = sum_n
        max_num = num
print(f'Число {max_num} с максимальной суммой цифр {max_sum}')
