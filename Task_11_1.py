# Первая задача к одиннадцатому занятию

from calendar import *
from datetime import *

lst = []

for m in range(1, 13):
    for d in range(1, 8):
        if weekday(2024, m, d) == 3:
            lst.append((date(2024, m, d) + timedelta(14)).strftime('%d.%m.%y'))

print(", ".join(lst))
