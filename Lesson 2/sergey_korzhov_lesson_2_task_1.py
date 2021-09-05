"""
Задание 1:
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""

while True:
    z = input('Введите знак операции "* / + -": ')
    if z == '0':
        break
    if z in ('*', '/', '+', '-'):
        a = float(input('1-е число: '))
        b = float(input('2-е число: '))
        if b == 0:
            print('Error: Деление на 0')
        elif z == '*':
            print(a * b)
        elif z == '/':
            print(a / b)
        elif z == '+':
            print(a + b)
        elif z == '-':
            print(a - b)
    else:
        print('Неверный знак операции!')