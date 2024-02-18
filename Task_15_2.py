# Вторая задача к пятнадцатому занятию

from re import *

msg = input()

regex = r"[AАBВCСEЕHНKКMМOОPРTТXХ]\d{3}[AАBВCСEЕHНKКMМOОPРTТXХ][AАBВCСEЕHНKКMМOОPРTТXХ]\d{2,3}"
print(*findall(regex, msg))
