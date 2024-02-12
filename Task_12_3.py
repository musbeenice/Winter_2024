# Третья задача к двенадцатому занятию

# def func(str_of_ranges):
#     lst = [y for x in str_of_ranges for y in range(int(x.split("-")[0]), int(x.split("-")[1]))]
#     return lst

# print(func([x for x in input().split(",")]))

# or

s = input().split(",")
res = []
for z in s:
    if "-" in z:
        x, y = map(int, z.split("-"))
        for u in range(x, y + 1):
            res.append(u)
    else:
        res.append(int(z))
print(res)
