'''Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
 Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
 Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.'''

revenue = int(input('Введите значение выручки: '))
cost = int(input('Введите число издержек фирмы: '))

if revenue > cost:
    print('Фирма работает в прибыль')
    profit = revenue / cost
    print(f'Прибыль составляет {profit}')
    profitability = profit / revenue
    print(f'Рентабельность выручки составляет: {profitability}')
else:
    print('Фирма работает в убыток')

staff = int(input('ведите количество сотрудников: '))
profit2 = profit / staff
print(f'Прибыль на каждого сотрудника составляет {profit2}')