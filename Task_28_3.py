# Третья задача к двадцать восьмому занятию

# def hanoi(n, i=1, k=2):
#     count = 0
#     if n == 1:
#         print(f"Move disk 1 from pin {i} to {k}")
#     else:
#         tmp = 6 - i - k
#         count += hanoi(n - 1, i, tmp)
#         print(f"Move disk {n} from pin {i} to {k}")
#         count += hanoi(n - 1, tmp, k)
#     return count + 1
#
#
# moves = hanoi(3)
# print("Total moves:", moves)

# or


def hanoi(n, a, b):
    count = 0
    if n == 0: return count
    else:
        count += hanoi(n - 1, a, 6 - a - b)
        print(a, b)
        count += 1
        count += hanoi(n - 1, 6 - a - b, b)
    return count


n = int(input())
print(hanoi(n, 1, 2))
