# Первая задача к двадцать шестому занятию

def are_alike(a, b):
    if len(a) == len(b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
            if count == 2:
                return False
        else:
            return True
    elif a == b[:-1] or a[:-1] == b:
        return True
    else:
        return False


print(are_alike(input(), input()))

# or


# def cmpr(s, z):
#     if abs(len(s) - len(z)) > 1: return False
#     if s in z or z in s: return True
#     if len(s) != len(z): return False
#     if sum([s[i] != z[i] for i in range(len(s))]) > 1: return False
#     return True
#
#
# print(cmpr(input(), input()))

# or


# def compare(s, t):
#     if abs(len(s) - len(t)) > 1: return False
#     for i in range(min(len(s), len(t))):
#         if s[i] != t[i]:
#             return s[i:] == t[i + 1:] or s[i + 1:] == t[i:]
#     else:
#         return True
#
#
# print(compare(input(), input()))
