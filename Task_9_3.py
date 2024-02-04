# Третья задача к девятому занятию

msg = input()

dct = {}
lst = []

for i in range(len(msg)):
    if msg[i].isalpha():
        dct[msg[i].lower()] = dct.get(msg[i].lower(), 0) + 1

lst = sorted([[k, str(v)] for k, v in dct.items()], key=lambda x: (-int(x[1]), x[0]))

for i in range(min(10, len(lst))):
    print(" - ".join(lst[i]))
