# Первая задача к восьмому занятию

code = input()

res = ""
i = 0

while i < len(code):
    if i + 1 < len(code) and (code[i : i + 2] == "АГ" or code[i : i + 2] == "ГА"):
        res += code[i + 1] + code[i]
        i += 2
    elif i + 1 < len(code) and (code[i : i + 2] == "ТЦ" or code[i : i + 2] == "ЦТ"):
        if code[i] == "Т":
            res += "ТАГЦ" 
        else: 
            res += "ЦАГТ"
        i += 2
    else:
        res += code[i]
        i += 1

print(res)
