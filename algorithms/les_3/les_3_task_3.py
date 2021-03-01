#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

len_ = 10
array = [0] * len_

for i in range(len_):
    array[i] = random.randint(0, 100)
print(array)

min = 0
max = 0

for i in range(len_):
    if array[i] < array[min]:
        min = i
    elif array[i] > array[max]:
        max = i

array[min], array[max] = array[max], array[min]

print(f'Минимальный элемент {array[min]}, максимальный {array[max]}')
print(f'{array=}')


