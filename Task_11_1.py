# Первая задача к одиннадцатому занятию

# from calendar import *
# from datetime import *

# lst = []

# for m in range(1, 13):
#     for d in range(1, 8):
#         if weekday(2024, m, d) == 3:
#             lst.append((date(2024, m, d) + timedelta(14)).strftime('%d.%m.%y'))

# print(", ".join(lst))

# or

from datetime import *

for i in range(1, 13):
    chet = 0
    for j in range(1, 29):
        if date(2024, i, j).weekday() == 3:
            chet += 1
            if chet == 3:
                print(date(2024, i, j).strftime('%d.%m.%Y'))
                break
