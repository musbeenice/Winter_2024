# Третья задача к двадцать третьему занятию

# from itertools import *
#
# nums = [i for i in input().split()]
#
#
# def largest_num(lst):
#     lst = list(permutations(lst, len(lst)))
#     res = []
#
#     for n in lst:
#         mx = ""
#         for v in n:
#             mx += str(v)
#         res.append(mx)
#
#     return max(res, key=lambda x: int(x))
#
#
# print(largest_num(nums))

# or

lst = [7, 71, 72, 73]
s = list(map(str, lst))
while True:
    print(s)
    for i in range(len(s) - 1):
        if s[i] + s[i + 1] < s[i + 1] + s[i]:
            s[i], s[i + 1] = s[i + 1], s[i]
            break
    else:
        break
print(int("".join(map(str, s))))

# or

# import functools
#
#
# def get_biggest(numbers):
#     def compare(x, y):
#         return -1 if str(x) + str(y) > str(y) + str(x) else 1
#
#     nu = sorted(numbers, key=functools.cmp_to_key(compare))
#
#     return int("".join([str(i) for i in nu]))
#
#
# print(get_biggest([7, 71, 72, 73]))
