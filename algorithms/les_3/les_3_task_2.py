#Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
#второй массив надо заполнить значениями 0, 3, 4, 5, (
# индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
import random

N = 10
array = [0] * 10
idx = []
for i in range(N):
    array[i] = random.randint(0, 100)
    if array[i] % 2 == 0:
        idx.append(i)

print(array)
print(f'Индексы четных чисел {idx}')