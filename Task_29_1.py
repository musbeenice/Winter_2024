# Первая задача к двадцать девятому занятию

def unique_num(lst):
    dct = {}
    for num in lst:
        dct[num] = dct.get(num, 0) + 1
    return filter(lambda x: dct[x] == 1, dct)


print(*unique_num([11, 3, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12]))
