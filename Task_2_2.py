# Вторая задача ко второму занятию

lst = []
n = int(input())
for i in range(n):
    lst.append(float(input()))

smallest = lst[0]
for i in range(n):
    if lst[i] < smallest:
        smallest = lst[i]
print(smallest)
