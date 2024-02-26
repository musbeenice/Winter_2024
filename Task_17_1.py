# Первая задача к семнадцатому занятию

from re import *

def remove_dupl(text):
    while findall(r"(\w+)\W+\1", text) != []:
        text = sub(r"(\w+)\W+\1", r"\1", text, flags = re.I)
    return text

msg = "Повторы здесь здесь запрещены запрещены запрещены законом законом законом законом законом"

print(remove_dupl(msg))

# or

# import re

# s = "напишите программу программу, которая устраняет повторы повторы слов"
# f = re.finditer(r"\b\w+\b", s)
# res = s
# prev_group, prev_start, prev_end = "", 0, 0
# for i in f:
#     i_group, i_start, i_end = i.group(), i.start(), i.end()
#     if i_group == prev_group:
#         res = res[:prev_end] + "*" * (len(i_group) + i_start - prev_end) + res[i_end:]
#     prev_group, prev_start, prev_end = i_group, i_start, i_end
#     print(res)
# res = re.sub(r"\*", r"", res)
# print(res)
