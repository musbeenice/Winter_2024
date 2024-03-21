# Первая задача к двадцать седьмому занятию

def filling_dartboard(db, n):
    x, y = 0, 0
    dx, dy = 0, 1
    for z in range(n**2):
        db[x][y] = min(x, y, n - x - 1, n - y - 1) + 1
        if x + dx > n - 1 or y + dy > n - 1 or db[x + dx][y + dy]:
            if dx == 0 and dy == 1:
                dx, dy = 1, 0
            elif dx == 1 and dy == 0:
                dx, dy = 0, -1
            elif dx == 0 and dy == -1:
                dx, dy = -1, 0
            elif dx == -1 and dy == 0:
                dx, dy = 0, 1
        x, y = x + dx, y + dy
    return db


num = int(input())
matrix = [[0 for _ in range(num)] for _ in range(num)]

for row in filling_dartboard(matrix, num):
    print(*row)
