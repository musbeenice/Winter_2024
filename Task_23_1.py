# Первая задача к двадцать третьему занятию

# msg = list(input())
#
# res = []
#
# for i in range(1, len(msg) + 1):
#     for j in range(len(msg) - i + 1):
#         res.append(msg[j:j + i])
#
# print(len(max(res, key=lambda x: len(x) if x == x[::-1] else 0)))

# or


def max_pal(s):
    len_s = len(s)
    for i in range(len_s, -1, -1):
        for j in range(len_s - i):
            ss = s[j:i + j + 1]
            print(ss)
            if ss == ss[::-1]:
                return ss


s = input()
print(max_pal(s))
