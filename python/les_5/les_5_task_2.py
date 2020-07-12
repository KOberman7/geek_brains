'''Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.'''

counter = 0
with open('2.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        counter += 1
        l_words = line.split(' ')
        print(f'Строка: {line}, длина строки: {len(l_words)}')
    print(f'Количество строк: {counter}')