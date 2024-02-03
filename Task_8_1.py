# Первая задача к восьмому занятию

# code = input()

# res = ""
# i = 0

# while i < len(code):
#     if i + 1 < len(code) and (code[i : i + 2] == "АГ" or code[i : i + 2] == "ГА"):
#         res += code[i + 1] + code[i]
#         i += 2
#     elif i + 1 < len(code) and (code[i : i + 2] == "ТЦ" or code[i : i + 2] == "ЦТ"):
#         if code[i] == "Т":
#             res += "ТАГЦ"
#         else:
#             res += "ЦАГТ"
#         i += 2
#     else:
#         res += code[i]
#         i += 1

# print(res)

# or

s = list(input())
i = 0
while i < len(s) - 1:
    if s[i] + s[i + 1] in "АГА":
        s[i], s[i + 1] = s[i + 1], s[i]
        i += 1
    elif s[i] + s[i + 1] in "ТЦТ":
        s.insert(i + 1, "АГ")
        i += 2
    i += 1
    print(s)  # отладочная печать
print("".join(s))
