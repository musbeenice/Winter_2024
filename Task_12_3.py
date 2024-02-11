# Третья задача к двеннадцатому занятию

def func(str_of_ranges):
    lst = [y for x in str_of_ranges for y in range(int(x[0]), int(x[2]) + 1)]
    return lst

print(func([x for x in input().split(", ")]))
