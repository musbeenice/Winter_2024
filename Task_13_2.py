# Вторая задача к тринадцатому занятию

# Вывод num палиндромов:
def palindrome():
    n = 0
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            yield n

g = palindrome()
num = int(input())

for _ in range(num):
    print(next(g), end=" ")

# or

# Вывод чисел-палиндромов до числа = limit:
# def func():
#     for x in range(1, limit):
#         if str(x) == str(x)[::-1]:
#             yield x

# g = func(int(input()))

# while True:
#     try:
#         print(next(g), end=" ")
#     except StopIteration:
#         break
