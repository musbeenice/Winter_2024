# Третья задача к двадцать третьему занятию

from itertools import *

nums = [i for i in input().split()]


def largest_num(lst):
    lst = list(permutations(lst, len(lst)))
    res = []

    for n in lst:
        mx = ""
        for v in n:
            mx += str(v)
        res.append(mx)

    return max(res, key=lambda x: int(x))


print(largest_num(nums))
