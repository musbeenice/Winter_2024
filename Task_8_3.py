# Третья задача к восьмому занятию

lst = ["abab", "xx", "aaaaaaa", "abcbab"]


def sort_lst(x):
    return -len(set(x))


print(sorted(lst, key=lambda x: (sort_lst(x), x)))
