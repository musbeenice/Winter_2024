# Первая задача к девятнадцатому занятию

from itertools import *

res = []
s = [10, 50, 100, 200, 1000, 2000, 5000,]

for seq in [[sum(x) for x in combinations(s, i)] for i in range(1, len(s) + 1)]:
    res.extend(seq)

print(", ".join(map(str, sorted(res))))
