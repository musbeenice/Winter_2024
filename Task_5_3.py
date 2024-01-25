# Третья задача к пятому занятию

fib_1 = 0
fib_2 = 1
n = int(input())
for _ in range(n):
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    print(fib_1, end=" ")
