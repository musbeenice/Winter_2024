# Вторая задача ко второму занятию

# we print several identical smallest numbers

lst = []
n = int(input())
for i in range(n):
    lst.append(float(input()))

smallest = lst[0]
for i in range(n):
    if lst[i] < smallest:
        smallest = lst[i]
for i in range(n):
    if smallest == lst[i]:
        print(smallest)

# we print 1st and 2nd largest number:

n = int(input())
largest_1 = 0
largest_2 = 0
for _ in range(1, n + 1):
    num = int(input())
    if num > largest_1:
        largest_2 = largest_1
        largest_1 = num
    elif num > largest_2:
        largest_2 = num
print(largest_1)
print(largest_2)
