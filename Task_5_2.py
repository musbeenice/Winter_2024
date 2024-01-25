# Вторая задача к пятому занятию

n = int(input())
lst = []
lst_1 = []
for i in range(n - 1, 1, -1):
    counter = 0
    if n % i == 0:
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                counter += 1
        if counter == 0:
            lst.append(i)

res = []
for prime_factor in lst:
    power = 0
    while n % prime_factor == 0:
        n //= prime_factor
        power += 1
    res.append(f"{prime_factor} - {power}")
print(" \n".join(res))
