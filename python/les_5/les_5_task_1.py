'''Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''
while True:
    with open('1.txt', 'a', encoding='utf-8') as frst:
        first = input('Введите стоку для записи: ')
        if first == '':
            break
        frst.write(first + '\n')