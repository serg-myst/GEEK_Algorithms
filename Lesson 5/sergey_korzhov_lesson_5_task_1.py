"""
Задание 1:
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
и отдельно вывести наименования предприятий, чья прибыль ниже среднего

Составим словарь: {'Предприятие1': Прибыль1, 'Предприятие2': Прибыль2 и т.д.}
После ввода делаем расчет по заданию
"""

company_dict = {}
sum_profit_all_companies = 0

all_companies = int(input('Введите количество предприятий: '))
print()

for comp in range(all_companies):
    company_name = input('Введите название предприятия:')
    sum_profit = 0
    for quarter in range(4):
        quarter_value = int(input(f'Введите значение прибыли за {quarter + 1} квартала: '))
        sum_profit += quarter_value
    sum_profit_all_companies += sum_profit
    company_dict[company_name] = sum_profit
    print()

average_profit = round(sum_profit_all_companies / all_companies, 2)
in_profit = [key for key in company_dict.keys() if company_dict[key] > average_profit]
out_profit = [key for key in company_dict.keys() if company_dict[key] < average_profit]

print()
print(f'Общая прибыль по всем предприятиям = {sum_profit_all_companies}')
print(f'Средняя прибыль по всем предприятиям = {average_profit}')
print(f'Предприятия с прибылью выше среднего - {in_profit}')
print(f'Предприятия с прибылью меньше среднего - {out_profit}')
