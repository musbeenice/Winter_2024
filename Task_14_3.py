# Третья задача к четырнадцатому занятию

def triangle(n):
    if n == 1:
        print("*")
    else:
        print("*" * n)
        triangle(n - 1)
    if n > 1:
        print("*" * n)
triangle(int(input()))
