''' Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''

def my_func(a, b, c):
    if a > b and b > c:
        return a + b
    elif a > b and c > b:
        return a + c
    else:
        return b + c

print(my_func(1, 2, 3))
print(my_func(8, 2, 3))
print(my_func(3, 2, 0))