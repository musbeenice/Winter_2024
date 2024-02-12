# Первая задача к двенадцатому занятию

def func(lst):
    lst_1 = [x for x in range(len(lst)) if lst[x] == min(lst)]
    lst_2 = [x for x in range(len(lst)) if lst[x] == max(lst)]
    return lst_1, lst_2

print(*func([int(x) for x in input().split()]))
