# Вторая задача к пятнадцатому занятию

from re import *

msg = input()

regex = r"[AАBВCСEЕHНKКMМOОPРTТXХ]\d{3}[AАBВCСEЕHНKКMМOОPРTТXХ][AАBВCСEЕHНKКMМOОPРTТXХ]78|[AАBВCСEЕHНKКMМOОPРTТXХ]\d{3}[AАBВCСEЕHНKКMМOОPРTТXХ][AАBВCСEЕHНKКMМOОPРTТXХ]178"
print(*findall(regex, msg))
