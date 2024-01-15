# Третья задача к первому занятию

x = int(input())
y = int(input())

summ = x + y
dif = x - y
prod = x * y
div = x / y
fl_div = x // y
mod = x % y

max_value = max(summ, dif, prod, div, fl_div, mod)

if summ == max_value:
    second_max_value = max(dif, prod, div, fl_div, mod)
elif dif == max_value:
    second_max_value = max(summ, prod, div, fl_div, mod)
elif prod == max_value:
    second_max_value = max(summ, dif, div, fl_div, mod)
elif div == max_value:
    second_max_value = max(summ, dif, prod, fl_div, mod)
elif fl_div == max_value:
    second_max_value = max(summ, dif, prod, div, mod)
else:
    second_max_value = max(summ, dif, prod, div, fl_div)

print(second_max_value)
