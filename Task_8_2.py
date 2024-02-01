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

lst = [[1, 55, 23], [27, 34, 11, 45], [3, 7, 9, 0, 78]]

# Функция для подсчета количества цифр в числе
def count_digits(number):
    return sum(c.isdigit() for c in str(number))

# Сортировка по количеству цифр и убыванию внутри каждого подсписка
sorted_lst = sorted(lst, key=lambda sublist: (sum(map(count_digits, sublist)), sublist), reverse=True)

print(sorted_lst)
