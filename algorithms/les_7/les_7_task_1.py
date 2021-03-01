'''Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
 Выведите на экран исходный и отсортированный массивы.'''
import random

SIZE = 10
lst = [random.randint(-100, 100) for i in range(SIZE)]
print(lst)

def bubble(a):
    n = 1
    while n < len(a):
        for i in range(len(a)-n):
            if a[i+1] > a[i]:
                a[i+1], a[i] = a[i], a[i+1]
        n += 1
    return a
print(bubble(lst))
