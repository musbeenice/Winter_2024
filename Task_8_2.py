# Вторая задача к восьмому занятию
# сортировка: по возрастанию общего количества цифр в подсписках + каждый подсписок по убыванию значений
lst = [[1, 55, 23], [27, 34, 11, 45], [3, 7, 9, 0, 78]]

res = []
for i in lst:
    res.append(list(map(str, i)))
print(res)

result = []
for i in lst:
    inner_list = []
    for j in ''.join(map(str, i)):
        inner_list.append(int(j))
    result.append(inner_list)

print(result)
