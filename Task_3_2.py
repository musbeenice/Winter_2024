# Вторая задача к третьему занятию

# num = input()
# lst = []

# for digit in num:
#     lst.append(int(digit))

# for i in range(10):
#     res = lst.count(i)
#     print(i, "-", res)

# or

n = input()
for k in "0123456789":
    print(k, "-", n.count(k))  # !!!

# or

# hm = [0] * 10
# print(hm)
# s = input()
# for k in s:
#     i = int(k)
#     hm[i] += 1
# for k, v in enumerate(hm):
#     print(k, "-", v)
# print(hm)
