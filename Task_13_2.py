# Вторая задача к тринадцатому занятию

def func(limit):
    for x in range(1, limit):
        if str(x) == str(x)[::-1]:
            yield x

g = func(int(input()))
while True:
    try:
        print(next(g), end=" ")
    except StopIteration:
        break
