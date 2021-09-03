"""
Задание 2:
Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = int(input('Please, enter number: '))

sum_even = 0
sum_odd = 0
for i in str(num):
    if int(i) % 2 == 0:
        sum_even += 1
    else:
        sum_odd += 1

print(f'Четных {sum_even}')
print(f'Нечетных {sum_odd}')

# Цикл без преобразования в строку
num = int(input('Please, enter number: '))

sum_even = 0
sum_odd = 0
while num > 0:
    if num % 2 == 0:
        sum_even += 1
    else:
        sum_odd += 1
    num = num // 10

print(f'Четных {sum_even}')
print(f'Нечетных {sum_odd}')