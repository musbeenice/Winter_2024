# Вторая задача к девятому занятию

example = input()
words = [input() for _ in range(int(input()))]
lst = []
dct = {}

vowels = "аеёиоуыэюя"

for i in range(len(example)):
    if example[i] in vowels:
        lst.append(i)

for word in words:
    for i in range(len(word)):
        if word[i] in vowels:
            dct.setdefault(word, []).append(i)
            # or dct[word] = dct.get(word, []) + [i]

for k, v in dct.items():
    if v == lst:
        print(k, end=", ")
