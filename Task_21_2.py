# Вторая задача к двадцать первому занятию

matrix = [[1, 1, 1, 1],
          [9, 6, 8, 555],
          [9, 2, 70, 1],
          [1, 1, 1, 1]]

length = len(matrix)
vbn = float("inf")  # Very Big Number

r = {(0, 0): matrix[0][0]}


def printing():
    for i in range(length):
        for j in range(length):
            print(r.get((i, j), vbn), end=" ")
        print()
    input("---")


for i in range(length):
    for j in range(length):
        if (i, j) not in r:
            r[(i, j)] = matrix[i][j] + min(r.get((i - 1, j), vbn), r.get((i, j - 1), vbn))
            print(r.get((i - 1, j), vbn), r.get((i, j - 1), vbn))
        printing()

# обратный путь - от нижней правой ячейки к верхней левой в новой матрице:
x = y = length - 1
route = [(x, y)]  # вывод пути в виде координат матрицы
while x > 0 or y > 0:
    if r.get((x - 1, y), vbn) < r.get((x, y - 1), vbn):
        x -= 1
    else:
        y -= 1
    route.append((x, y))
    print(route)
    input("===")
print(route[::-1])
