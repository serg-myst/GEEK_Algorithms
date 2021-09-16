from collections import deque


def get_dict_16_in():
    lst = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    dict_of_numbers = {lst[i]: i for i in range(16)}
    return dict_of_numbers


dict_10_16_in = get_dict_16_in()


def get_dict_16_out():
    lst = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    dict_of_numbers = {i: lst[i] for i in range(16)}
    return dict_of_numbers


dict_10_16_out = get_dict_16_out()


def get_sum_num(num_1, num_2):
    res = []
    k = 0
    if len(num_1) >= len(num_2):
        num_run = num_1
        num_find = num_2
    else:
        num_run = num_2
        num_find = num_1

    for i, v in enumerate(reversed(num_run)):
        n1 = dict_10_16_in[v]
        if i <= len(num_find) - 1:
            n2 = dict_10_16_in[num_find[len(num_find) - i - 1]]
        else:
            n2 = 0
        n3 = (n1 + n2) + k
        if n3 > 16:
            n3 -= 16
            k = 1
        else:
            k = 0
        res.append(dict_10_16_out[n3])
    if k != 0:
        res.append(str(k))
    return res[::-1]


def get_mult_num(num_1, num_2):
    if len(num_1) >= len(num_2):
        num_run = num_2
        num_find = num_1
    else:
        num_run = num_1
        num_find = num_2
    m_mult = []  # готовая матрица после умножения
    for ind, i in enumerate(reversed(num_run)):
        k = 0
        mas = []
        if ind != 0:
            mas = mas + ['0'] * (len(num_run) - 1)
        for j in reversed(num_find):
            n = dict_10_16_in[i] * dict_10_16_in[j] + k
            if n < 16:
                k = 0
                mas.append(dict_10_16_out[n])
            else:
                k = n // 16
                mas.append(dict_10_16_out[n - k * 16])
        if k != 0:
            mas.append(str(k))
        if ind == 0:
            mas = mas + ['0'] * (len(num_run) - 1)
        m_mult.append(mas)
    return m_mult


# Ввод данных для сложения. Работает универсально для любых чисел
num_1 = deque(input('Введите первое число: ').upper())
num_2 = deque(input('Введите второе число: ').upper())
print(f'Результат сложения: {get_sum_num(num_1, num_2)}')

# Для умножения используем данные из задачи. Данный алгоритм будет работать, если длина одного из чисел меньше другого
# Для полноты картины необходимо составить матрицу, строки которой будут результатом перемножения каждого числа
'''
Для примера C4F * A2A

0, 0, 7, B, 1, 6
0, 1, 8, 9, E, 0 
7, B, 1, 6, 0, 0

результат = 7D1AF6 

и т.д.

Результатом умножения будет сложения всех столбцов матрицы по правилам шестнадцатеричных чисел

'''

num_1 = deque('C4F')
num_2 = deque('A2')

res = get_mult_num(num_1, num_2)

print(f'Результат умножения: {get_sum_num(res[0][::-1], res[1][::-1])}')


# Вариант 2
# Читерский вариант. Конвертнем сначала в десятичную систему, там посчитаем и обратно конвертнем в шестнадцатиричную
def sum_numbers(num1, num2):
    return num1 + num2


def mult_numbers(num1, num2):
    return num1 * num2


def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEF"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


num_1 = int(convert_base(input('Введите первое число: ').upper(), 10, 16))
num_2 = int(convert_base(input('Введите второе число: ').upper(), 10, 16))

print(deque(convert_base(sum_numbers(num_1, num_2), 16)))
print(deque(convert_base(mult_numbers(num_1, num_2), 16)))
