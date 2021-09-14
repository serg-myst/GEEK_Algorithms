"""
Задание 2:
Написать два алгоритма нахождения i-го по счёту простого числа:

1) Без использования «Решета Эратосфена»
2) Используя алгоритм «Решето Эратосфена»

Можно предположить, что на больших объем алгоритм с использованием решета Эратосфена будет работать быстрее
"""
import cProfile


def new_massive(n):
    a = [i for i in range(n+1)]
    return a


def without_sieve_eratosthenes(num, n, a):
    a[1] = 0
    for i in range(num, n):
        if a[i] != 0:
            j = i + i
            while j < n:
                a[j] = 0
                j += i

    res = [i for i in a if i != 0]
    # print(f'Количество простых чисел в диапазоне до {n}: {res}')


def sieve_eratosthenes(n, a):
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    # print(f'Количество простых чисел в диапазоне до {n}: {lst}')


a = new_massive(1000000)

cProfile.run('without_sieve_eratosthenes(2, 1000000, a)')
cProfile.run('sieve_eratosthenes(1000000, a)')

"""
Функция without_sieve_eratosthenes:

 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.256    0.256 <string>:1(<module>)
        1    0.236    0.236    0.255    0.255 sergey_korzhov_lesson_4_task_2.py:17(without_sieve_eratosthenes)
        1    0.019    0.019    0.019    0.019 sergey_korzhov_lesson_4_task_2.py:26(<listcomp>)
        1    0.000    0.000    0.256    0.256 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Функция sieve_eratosthenes:

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.210    0.210 <string>:1(<module>)
        1    0.199    0.199    0.205    0.205 sergey_korzhov_lesson_4_task_2.py:30(sieve_eratosthenes)
        1    0.000    0.000    0.210    0.210 {built-in method builtins.exec}
    78498    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""