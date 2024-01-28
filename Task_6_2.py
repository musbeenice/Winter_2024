# Вторая задача к шестому занятию

pupil_1, pupil_2 = input().split(), input().split()

lst_1, lst_2 = [], []

for book in pupil_1:
    lst_1.append(book)
    tes_1 = set(lst_1)
for book in pupil_2:
    lst_2.append(book)
    tes_2 = set(lst_2)

print(len(tes_1.intersection(tes_2)))
