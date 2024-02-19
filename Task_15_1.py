# Первая задача к пятнадцатому занятию

dct = {"lz": 1, "when": 2, 1:{"the": 22, 3: {1: 111, "levee": 222, 1: 34, 3: {"breaks": 1111, 1: 2222, 5:{1: {1: 25}}, 2: 3333}}, 1: 19,}, 32: 33}
x = int(input())
res = []
def func(d, x):
    for k, v in d.items():
        if k == x:
            res.append(v)
        if type(v) == dict:
            func(v, x)
        else:
            pass
func(dct, x)
print(res)
