# Вторая задача к первому занятию

x, y = float(input()), float(input())
if y == 0:
    print("error")
else:
    a, b, c, d, e = x + y, x - y, x * y, x / y, x // y
    max_1 = a
    if b >= max_1:
        max_1 = b
    if c >= max_1:
        max_1 = c
    if d >= max_1:
        max_1 = d
    if e >= max_1:
        max_1 = e
    print(max_1)
