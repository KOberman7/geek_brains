'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.'''

#list

num = input('Введите число от 1 до 12: ')

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if num == '12' or num == '1' or num == '2':
    print('winter')
elif num == '3' or num == '4' or num == '5':
    print('spring')
elif num == '6' or num == '7' or num == '8':
    print('summer')
elif num == '9' or num == '10' or num == '11':
    print('autumn')
else:
    print('error')

#dict

season = {
    'winter': (12, 1, 2),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11)
}

num2 = int(input('Введите число от 1 до 12: '))

for key in season.keys():
    if num2 in season[key]:
        print(key)