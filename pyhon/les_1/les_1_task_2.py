'''Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

sec = int(input('Введите число в секундах: '))

h = ((sec // 3600)) % 24
m = (sec // 60) % 60
s = sec % 60

print(f'Время {h}:{m}:{s}')