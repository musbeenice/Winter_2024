# Третья задача к пятому занятию

n = int(input())
a, b = 0, 1
for _ in range(n, end=" "):
    print(b)
    # a, b = b, a + b  # более экономный вариант
    tmp = a
    a = b
    b = tmp + b
