# Первая задача к двадцать восьмому занятию

def num_of_inv(lst):
    c = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                c += 1
    return c


print(num_of_inv([1, 2, 3, 4, 5]))
print(num_of_inv([5, 4, 3, 2, 1]))
print(num_of_inv([1, 3, 2, 1, 0]))
print(num_of_inv([1, 3, 2, 3, 1]))
