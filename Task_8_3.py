# Третья задача к восьмому занятию

lst = ["abab", "xx", "yy", "aaaaaaa", "abcbab"]


def sort_lst(x):
    return -len(set(x)), x


print(sorted(lst, key=sort_lst))

# or w lambda

print(sorted(lst, key=lambda x: (-len(set(x)), x)))
