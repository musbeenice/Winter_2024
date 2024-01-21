# Вторая задача к третьему занятию

num = input()
lst = []

for digit in num:
    lst.append(int(digit))

for i in range(10):
    res = lst.count(i)
    print(i, "-", res)
