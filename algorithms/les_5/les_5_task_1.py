'''Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
 (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
 и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
import collections

n = int(input('Введите кол-во предпиятий: '))

sum_profit = 0
enter = {}
Enterprise = collections.namedtuple('Enterprise', ['profit_1', 'profit_2', 'profit_3', 'profit_4'])

for i in range(n):
    name = input('Введите название предприятия: ')
    profit1 = int(input('Введите прибыль за 1-й квартал: '))
    profit2 = int(input('Введите прибыль за 2-й квартал: '))
    profit3 = int(input('Введите прибыль за 3-й квартал: '))
    profit4 = int(input('Введите прибыль за 4-й квартал: '))
    all_profit = profit1 + profit2 + profit3 + profit4
    enter[name] = Enterprise(
        profit_1=profit1,
        profit_2=profit2,
        profit_3=profit3,
        profit_4=profit4
    )
    print(f'Предприятие {name}: прибыль {all_profit}')

    sum_profit += all_profit

avg = sum_profit / n
print(f'Средняя прибыль за год составила: {int(avg)}')

for name, profit in enter.items():
    if sum(profit) > avg:
        print(f'Прибыль {name} выше стреднего')

for name, profit in enter.items():
    if sum(profit) < avg:
        print(f'Прибыль {name} ниже стреднего')