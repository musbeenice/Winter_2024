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

n = int(input())

lst = [[1]]

# or
