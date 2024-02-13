# Первая задача к тринадцатому занятию

def func():
    x = 1
    while True:
        yield x if x % 2 else -x
        x += 1
g = func()
for i in range(int(input())):
    print(next(g), end=" ")
