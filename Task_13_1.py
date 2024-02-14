# Первая задача к тринадцатому занятию

# def func():
#     x = 1
#     while True:
#         yield x if x % 2 else -x
#         x += 1

# g = func()

# for _ in range(int(input())):
#     print(next(g), end=" ")

# or

def sgns():
    i, s = 0, -1
    while True:
        i, s = i + 1, -s
        yield i * s

g = sgns()

for _ in range(int(input())):
    print(next(g), end=" ")
