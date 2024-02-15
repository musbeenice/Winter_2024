# Первая задача к четырнадцатому занятию

def num_dig(n, m = 0):
    while n > 0:
        m += 1
        return num_dig(n // 10, m)
    else:
        return m
print(num_dig(int(input())))
