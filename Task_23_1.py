# Первая задача к двадцать третьему занятию

msg = list(input())

res = []

for i in range(1, len(msg) + 1):
    for j in range(len(msg) - i + 1):
        res.append(msg[j:j + i])

print(len(max(res, key=lambda x: len(x) if x == x[::-1] else 0)))
