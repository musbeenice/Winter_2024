# Вторая задача к пятнадцатому занятию

from re import *

ab = "ABCEHKMOPTXYАВСЕНКМОРТХУ"
tmpl = rf"[{ab}]\d\d\d[{ab}][{ab}]1?78"
msg = input()

print(*findall(tmpl, msg))
