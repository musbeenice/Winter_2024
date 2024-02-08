# Вторая задача к восьмому занятию

# сортировка: по возрастанию общего количества цифр в подсписках + каждый подсписок по убыванию значений

lst = [[1, 55, 23], [27, 34, 11, 45], [3, 7, 9, 0, 78]]


def digits(lst):
    res = 0
    for i in lst:
        res += len(str(i))
    return res


new_lst = sorted(lst, key=digits)
print(new_lst)
res = []
for i in new_lst:
    res.append(sorted(i, reverse=True))
print(res)
