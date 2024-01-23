# Вторая задача к четвертому занятию

n = int(input())

lst = []
dct = {}
counter = 1
for i in range(1, n + 1):
    dct[i] = list(range(counter, counter + n))
    counter += n
print(dct)
