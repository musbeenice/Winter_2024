# Первая задача к девятнадцатому занятию

from itertools import *

res = []

for seq in [[sum(x) for x in combinations([10, 50, 100, 200, 1000, 2000, 5000,], i)] for i in range(1, 8)]:
    res.extend(seq)

print(", ".join(map(str, sorted(res))))
