# Вторая задача к четырнадцатому занятию

def total_dig(n):
    if abs(n) < 10:
        return n
    return abs(n) % 10 + total_dig(abs(n) // 10)
print(total_dig(int(input())))
