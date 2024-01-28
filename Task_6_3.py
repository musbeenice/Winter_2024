# Третья задача к шестому занятию

msg = input()

lst_letter = []
lst_digit = []
lst_symbol = []

for char in msg:
    if char.isalpha() == True:
        lst_letter.append(char)
    if char.isdigit() == True:
        lst_digit.append(char)
    if char.isalnum() == False:
        lst_symbol.append(char)

print(*sorted(set(lst_letter)), sep="")
print(*sorted(set(lst_digit)), sep="")
print(*sorted(set(lst_symbol)), sep="")
