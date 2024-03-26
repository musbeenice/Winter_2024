# Вторая задача к двадцать девятому занятию

print((lambda x, y: sum(a != b for a, b in zip(x, y)))(*input().split()))
