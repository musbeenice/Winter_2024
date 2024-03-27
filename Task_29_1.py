# Первая задача к двадцать девятому занятию

from collections import Counter


def one(lst):
    c = Counter(lst)
    for k, v in c.items():
        if v == 1: return k


print(one(map(int, input().split())))

# or

s = [11, 3, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12]
print(min(set(s), key=lambda x: s.count(x)))

# or

# def unique_num(lst):
#     dct = {}
#     for num in lst:
#         dct[num] = dct.get(num, 0) + 1
#     return filter(lambda x: dct[x] == 1, dct)
#
#
# print(*unique_num([11, 3, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12]))
