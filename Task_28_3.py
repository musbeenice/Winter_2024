# Третья задача к двадцать восьмому занятию

def hanoi(n, i=1, k=2):
    count = 0
    if n == 1:
        print(f"Move disk 1 from pin {i} to {k}")
    else:
        tmp = 6 - i - k
        count += hanoi(n - 1, i, tmp)
        print(f"Move disk {n} from pin {i} to {k}")
        count += hanoi(n - 1, tmp, k)
    return count + 1


moves = hanoi(3)
print("Total moves:", moves)
