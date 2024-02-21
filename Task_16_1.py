# Первая задача к шестнадцатому занятию

from re import *
 
msg = input()
 
print("".join(findall(r"\b(\w)\w+\b", msg)).upper())

# or

# from re import *
 
# msg = input()

# res = sub(r"\b\w+\b", lambda x: x.group().title()[0], msg).replace(" ", "")
 
# print(res)
