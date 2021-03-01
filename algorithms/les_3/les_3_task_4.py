#Определить, какое число в массиве встречается чаще всего.
import random

length = 10
array = [0] * length

for i in range(length):
    array[i] = random.randint(0, 100)
print(array)

num = array[0]
max = 0
for i in range(length - 1):
    m = 1
    for j in range(i + 1, length):
        if array[i] == array[j]:
            m += 1

    if m > max:
        max = m
        num = array[i]

if max > 1:
    print(f'{num} встречается {max}')
else:
    print('Все элементы уникальны')