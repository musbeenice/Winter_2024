# Первая задача к четырнадцатому занятию

def num_dig(n):
    if abs(n) < 10:
        return 1
    return 1 + num_dig(abs(n) // 10)
print(num_dig(int(input())))
