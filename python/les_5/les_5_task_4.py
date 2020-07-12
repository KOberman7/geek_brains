'''Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('numbers2.txt', 'a', encoding='utf-8') as new_file:
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        line = file.read().split('\n')
        for i in line:
            i = i.split(' - ')
            new_file.writelines(dic[i[0]] + '-' + i[1] + '\n')