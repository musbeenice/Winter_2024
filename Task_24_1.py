# Первая задача к двадцать четвертому занятию

# bubble sort:

# a = [17, 24, 91, 96, 67, -27, 79, -71, -79]
#
# n = len(a)
#
# for i in range(n - 1):
#     are_swapped = False
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             are_swapped = True
#         print(a)
#     if not are_swapped:
#         break
#
# print(a)

# selection sort:


# def selection(lst):
#     for i in range(len(lst) - 1):
#         mini, i_mini = lst[i], i
#         for j in range(i + 1, len(lst)):
#             if lst[j] < mini:
#                 mini, i_mini = lst[j], j
#         lst[i], lst[i_mini] = lst[i_mini], lst[i]
#         print(lst)
#     return lst
#
#
# print(selection([]))


# QuickSort:


import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        l_nums = [n for n in nums if n < q]
        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        print(f"{l_nums}")
        print(f"{e_nums}")
        print(f"{b_nums}")
        input("---")
        return quicksort(l_nums) + e_nums + quicksort(b_nums)


lst = [11, 1, 9, 2, 8, 7, 4, 8, 5, 3, 10]
print(quicksort(lst))
