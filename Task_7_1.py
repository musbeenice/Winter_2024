# Первая задача к седьмому занятию

s = list(map(int, input().split()))
res = 1
for k in s:
    res *= k
for n in range(res, 0, -1):
    for m in s:
        if n % m:  # то же самое, что != 0
            break
    else:
        nok = n
print(nok)

# or

# s = list(map(int, input().split()))
# def nod(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     return a + b
# def nok2(a, b):
#     return a * b // nod(a, b)
# x = 1
# for i in s:
#     x = nok2(x, i)
# print(x)