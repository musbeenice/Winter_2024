# Вторая задача к третьему занятию

num = int(input())
lst = []

while num > 0:
    last_digit = num % 10
    lst.append(last_digit)
    num //= 10
lst.reverse()

for i in range(10):
    res = lst.count(i)
    print(i, "-", res)
