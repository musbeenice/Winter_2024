# Первая задача к пятому занятию

n = int(input())
dct = {}

# for line in range(1, n + 1):
#     for value in range(1, line + 1):
#         dct.setdefault(line, []).append(1)

for line in range(n):
    row = [1]
    if line > 0:
        previous_row = dct[line - 1]
        for i in range(len(previous_row) - 1):
            row.append(previous_row[i] + previous_row[i + 1])
        row.append(1)
    dct[line] = row

for line, values in dct.items():
    spaces = " " * (n - line)
    print(spaces, end="")
    print(" ".join(list(map(str, values))))  # можно без list()
