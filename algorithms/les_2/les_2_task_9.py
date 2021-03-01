# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num = int(input('Введите целое число: '))

max_sum = 0
max_num = 0

while num != 0:
    m = num
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    if s > max_sum:
        max_sum = s
        max_num = m
    num = int(input('Введите целое число: '))
print(f'Число {max_num} имеет сумму {max_sum}')