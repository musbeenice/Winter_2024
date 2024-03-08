# Третья задача к двадцать второму занятию

import keyword
from re import *

msg = input()
forbidden = keyword.kwlist


def func(x):
    s = x.group()
    if s in forbidden:
        return "<kw>"
    else:
        return s


res = sub(r"\b\w+\b", func, msg)
print(res)
