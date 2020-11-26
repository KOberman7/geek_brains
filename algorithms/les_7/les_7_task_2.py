'''Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.'''

import random

SIZE = 10
lst = [float(random.randint(0, 50)) for i in range(SIZE)]
print(lst)

def merge(left_list, right_list):
    sorted_list = []
    left_list_idx = right_list_idx = 0

    left_list_len, right_list_len = len(left_list), len(right_list)

    for _ in range(left_list_len + right_list_len):
        if left_list_idx < left_list_len and right_list_idx < right_list_len:
            if left_list[left_list_idx] <= right_list[right_list_idx]:
                sorted_list.append(left_list[left_list_idx])
                left_list_idx += 1
            else:
                sorted_list.append(right_list[right_list_idx])
                right_list_idx += 1

        elif left_list_idx == left_list_len:
            sorted_list.append(right_list[right_list_idx])
            right_list_idx += 1

        elif right_list_idx == right_list_len:
            sorted_list.append(left_list[left_list_idx])
            left_list_idx += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

lst = merge_sort(lst)
print(lst)