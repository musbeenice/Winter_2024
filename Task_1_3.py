# Третья задача к первому занятию

x, y = float(input()), float(input())
if y == 0:
    print("error")
else:
    a, b, c, d, e = x + y, x - y, x * y, x / y, x // y
    print(a, b, c, d, e)
    if a >= b:
        max_1 = a
        max_2 = b
    else:
        max_1 = b
        max_2 = a
    if c >= max_1:
        max_2 = max_1
        max_1 = c
    elif c >= max_2:
        max_2 = c
    if d >= max_1:
        max_2 = max_1
        max_1 = d
    elif d >= max_2:
        max_2 = d
    if e >= max_1:
        max_2 = max_1
        max_1 = e
    elif e >= max_2:
        max_2 = e
    print(max_1, max_2)

# or

# x = int(input())
# y = int(input())

# summ = x + y
# dif = x - y
# prod = x * y
# div = x / y
# fl_div = x // y
# mod = x % y

# max_value = max(summ, dif, prod, div, fl_div, mod)

# if summ == max_value:
#     second_max_value = max(dif, prod, div, fl_div, mod)
# elif dif == max_value:
#     second_max_value = max(summ, prod, div, fl_div, mod)
# elif prod == max_value:
#     second_max_value = max(summ, dif, div, fl_div, mod)
# elif div == max_value:
#     second_max_value = max(summ, dif, prod, fl_div, mod)
# elif fl_div == max_value:
#     second_max_value = max(summ, dif, prod, div, mod)
# else:
#     second_max_value = max(summ, dif, prod, div, fl_div)

# print(second_max_value)
