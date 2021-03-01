# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите целое число: '))

def nums(n, level=0):
    if level == 0 and n == 0:
        return 1, 0
    even = 0
    odd = 0
    if n == 0:
        return even, odd
    elif n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
    res = nums(n, level + 1)
    even += res[0]
    odd += res[1]
    return even, odd
even, odd = nums(num)
print(f'Количество четных чисел {even}, нечетных {odd}')