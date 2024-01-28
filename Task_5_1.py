# Первая задача к пятому занятию

# Расчет биномиальных коэффициентов

# n = int(input())
# dct = {}

# for line in range(n):
#     row = [1]
#     if line > 0:
#         previous_row = dct[line - 1]
#         for i in range(len(previous_row) - 1):
#             row.append(previous_row[i] + previous_row[i + 1])
#         row.append(1)
#     dct[line] = row

# for line, values in dct.items():
#     spaces = " " * (n - line)
#     print(spaces, end="")
#     print(" ".join(list(map(str, values))))  # можно без list()

# or

# n = int(input())

# lst = [[1]]

# for i in range(1, n + 1):
#     cur = [1]
#     for j in range(1, i):
#         cur.append(lst[-1][j - 1] + lst[-1][j])
#     cur.append(1)
#     lst.append(cur)

# for cur in lst:
#     print(*cur)

# or

# n = int(input())

# lst_1 = [0, 1]

# for i in range(1, n + 1):
#     lst_2 = [0]
#     for j in range(i):
#         lst_2.append(lst_1[j] + lst_1[j + 1])
#         print(lst_2[-1], end=" ")
#     lst_2.append(0)
#     print()
#     lst_1 = lst_2.copy()

# or

n = int(input())

lst = [0, 1, 0]

print(1)
for i in range(2, n + 1):
    x = lst[0]
    for j in range(1, i + 1):
        y = x + lst[j]
        print(y, end=" ")
        x = lst[j]
        lst[j] = y
    print()
    lst.append(0)