# Вторая задача к четвертому занятию

n = int(input())
d, x, y, z = {}, 0, 0, 0
length = len(str(n**2))
 
for i in range(n):
    for j in range(n):
        d[i, j] = 0
 
dx, dy = 0, 1
for i in range(n**2):
    z += 1
    d[x, y] = z
    if d.get((x + dx, y + dy), -1) != 0:
        if (dx, dy) == (0, 1):
            dx, dy = 1, 0
        elif (dx, dy) == (1, 0):
            dx, dy = 0, -1
        elif (dx, dy) == (0, -1):
            dx, dy = -1, 0
        elif (dx, dy) == (-1, 0):
            dx, dy = 0, 1
    x, y = x + dx, y + dy
for i in range(n):
    for j in range(n):
        print(f"{str(d[i, j]).rjust(length)}", end=" ")
    print()
