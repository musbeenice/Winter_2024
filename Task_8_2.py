# Вторая задача к восьмому занятию
# сортировка: по возрастанию общего количества уникальных цифр в подсписках + каждый подсписок по убыванию значений
# lst = [[1, 55, 23], [27, 34, 11, 45], [3, 7, 9, 0, 78]]
# res = []


# def sorted_sublst():
#     for i in lst:
#         res.append(sorted(i, reverse=True))
#     return res


# print(sorted_sublst())


# def sorted_lst():
#     for i in lst:
#         sub_list = []
#         for j in "".join(map(str, i)):
#             sub_list.append(int(j))
#     return len(set(sub_list))


# до сортировки не дошел

# or

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
