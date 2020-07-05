'''Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.'''

def int_func(s):
    s = input('Input words with space: ').title()
    return s


print(int_func('text'))