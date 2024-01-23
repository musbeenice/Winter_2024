# Третья задача к четвертому занятию

msg_1, msg_2 = input().split(), input().split()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
dct_1, dct_2 = {}, {}
lst_1, lst_2 = [], []

for word in msg_1:
    lst_1.extend(list(word))

lst_1_mod = lst_1.copy()
for letter in lst_1_mod:
    if not letter in alphabet:
        lst_1.remove(letter)
for letter in lst_1:
    if not letter in dct_1:
        dct_1[letter] = 0
    dct_1[letter] += 1

for word in msg_2:
    lst_2.extend(list(word))

lst_2_mod = lst_2.copy()
for letter in lst_2_mod:
    if not letter in alphabet:
        lst_2.remove(letter)
for letter in lst_2:
    if not letter in dct_2:
        dct_2[letter] = 0
    dct_2[letter] += 1

print(dct_1 == dct_2)
