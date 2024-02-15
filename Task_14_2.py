# Вторая задача к четырнадцатому занятию

def total_dig(n, t = 0):
    while n > 0:
        dig = n % 10
        t += dig
        return total_dig(n // 10, t)
    return t
print(total_dig(int(input())))
