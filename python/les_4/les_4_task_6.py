''' Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.'''
# a
from itertools import count, cycle
i = int(input('Введите число меньше 20: '))
for el in count(i):
    if el > 20:
        break
    else:
        print(el)

print('-' * 50)

# б
a = 0

for el in cycle('Vera K '):
    if a > 10:
        break
    print(el)
    a += 1