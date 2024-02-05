# Вторая задача к девятому занятию

# example = input()
# words = [input() for _ in range(int(input()))]
# lst = []
# dct = {}

# vowels = "аеёиоуыэюя"

# for i in range(len(example)):
#     if example[i] in vowels:
#         lst.append(i)

# for word in words:
#     for i in range(len(word)):
#         if word[i] in vowels:
#             dct.setdefault(word, []).append(i)
#             # or dct[word] = dct.get(word, []) + [i]

# for k, v in dct.items():
#     if v == lst:
#         print(k, end=", ")

# or

vowels = "аеёиоуыэюя"

lst = ["кино", "дорога", "поросенок", "итог", "титан", "погост", "идея"]
sample = "питон"


def similar(st):
    res = []
    for i in range(len(st)):
        if st[i] in vowels:
            res.append(i)

    return res


sample_sim = similar(sample)
print(sample_sim)
for i in lst:
    # print(i, similar(i))
    if similar(i) == sample_sim:
        print(i)
