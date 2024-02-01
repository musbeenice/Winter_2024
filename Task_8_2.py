# Вторая задача к восьмому занятию
# сортировка: по возрастанию общего количества уникальных цифр в подсписках + каждый подсписок по убыванию значений
lst = [[1, 55, 23], [27, 34, 11, 45], [3, 7, 9, 0, 78]]
res = []
def sorted_sublst():
    for i in lst:
        res.append(sorted(i, reverse = True))
    return res
print(sorted_sublst())
