# Третья задача к двадцать второму занятию

import keyword
from re import *

msg = input()


def replace_kw(x):
    w = x.group()
    if w in keyword.kwlist:
        return "<kw>"
    else:
        return w


print(sub(r"\b\w+\b", replace_kw, msg))

# or

# import keyword
#
# s = input()
# for i in sorted(keyword.kwlist, key=len, reverse=True):
#     s = s.replace(i, "kw")
# print(s)
