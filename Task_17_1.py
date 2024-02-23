# Первая задача к семнадцатому занятию

from re import *

def remove_dupl(text):
    while findall(r"\b(\w+) \1\b", text) != []:
        text = sub(r"\b(\w+) \1\b", r"\1", text)
    return text

msg = "Повторы здесь здесь запрещены запрещены запрещены законом законом законом законом законом"

print(remove_dupl(msg))
