"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
import random


def median(lst, half):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]

    pivot = lst[0]

    less = []
    more = []
    pivots = []
    for item in lst:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    if len(less) > half:
        return median(less, half)
    elif len(less) + len(pivots) > half:
        return pivots[0]
    else:
        return median(more, half - len(more) - len(pivots))


m = int(input('Введите длину массива: '))
array = [random.randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив {array}')
print(f'Медиана {median(array, m)}')
