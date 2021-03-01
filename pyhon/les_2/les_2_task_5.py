'''Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.'''

list = [7, 5, 3, 3, 2]

print(list)

while True:
    number = int(input('Введите число для вставки: '))
    if list.count(number):
        list.insert(list.index(number) + list.count(number), float(number))
        print(list)
    else:
        param = 0
        n_param = 0
        for n, i in enumerate(list):
            if number > i:
                list.insert(n, number)
                print(list)
                break
            else:
                list.append(number)
                print(list)
                break