# Третья задача к двадцать седьмому занятию

def count_all_els(lst, c=0):
    for el in lst:
        if isinstance(el, list):
            c += count_all_els(el)
        c += 1
    return c


print(count_all_els([]))
print(count_all_els([1, 2, 3]))
print(count_all_els(["x", "y", ["z"]]))
print(count_all_els([1, 2, [3, 4, [5]]]))
print(count_all_els([1, 2, [3, [4, 5], [6, 7, [8]]]]))
print(count_all_els([1, 2, [3, 4, 5, [6, 7, [8]]]]))
print(count_all_els(['a', 2, ['b', 3, 'c', [5.1, ['d', [6.2, 'e', [7]]]]]]))
print(count_all_els(['a', 2, ['b', [3, 'c'], [5.1, ['d', [6.2, 'e', [7]]]]]]))
