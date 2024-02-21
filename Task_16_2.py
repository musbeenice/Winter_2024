# Вторая задача к шестнадцатому занятию

from re import *

n = str(int(input()))
msg = " ".join([str(i) for i in range(int(input()))])

regex = rf"[+-]?\b[0-{int(n[0]) - 1}]?[0-9]\b|[+-]?\b{n[0]}[0-{n[1]}]\b"

print(*findall(regex, msg))

# or

# from re import *

# text = " ".join([str(i) for i in range(123)])
# s = ""

# n = 45
# for i in range(46):
#     s += r"\b" + str(i) + r"\b"
# print(s)
