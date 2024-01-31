# Вторая задача к седьмому занятию


def code(string, n):
    res = ""
    for i in string:
        new_ord = ord(i) + n
        if chr(ord("a")) <= i <= chr(ord("a") + 25):
            new_ord = ord("a") + (new_ord - ord("a")) % 26
            res += chr(new_ord)
        elif chr(ord("A")) <= i <= chr(ord("A") + 25):
            new_ord = ord("A") + (new_ord - ord("a")) % 26
            res += chr(new_ord)
        else:
            res += i
    return res


while True:
    print(code(input(), int(input())))
