# Третья задача к двеннадцатому занятию

def func(str_of_ranges):
    lst = [y for x in str_of_ranges for y in range(int(x.split("-")[0]), int(x.split("-")[1]))]
    print([x for x in str_of_ranges])
    return lst

print(func([x for x in input().split(", ")]))
