# Третья задача к тринадцатому занятию

def func(lst):
    for x in lst:
        if int(x) % 2:
            yield int(x)

g = func(input().split())

for x in g:
    print(x, end=" ")
