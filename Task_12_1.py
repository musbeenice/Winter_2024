# Первая задача к двеннадцатому занятию

def func(lst):
    lst_1 = [i for i in range(len(lst)) if lst[i] == min(lst)]
    lst_2 = [i for i in range(len(lst)) if lst[i] == max(lst)]
    return lst_1, lst_2

print(*func([int(x) for x in input().split()]))
