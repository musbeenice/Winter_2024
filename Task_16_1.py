# Первая задача к шестнадцатому занятию
from re import *
 
msg = input()
 
print("".join(findall(r"\b(\w)\w+\b", msg)).upper())
