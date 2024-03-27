# Третья задача к двадцать девятому занятию

def are_isomorphic(w1, w2):
    if len(w1) != len(w2): return False
    dct1, dct2 = {}, {}
    for i in range(len(w1)):
        dct1[w1[i]] = dct1.get(w1[i], 0) + 1
        dct2[w2[i]] = dct2.get(w2[i], 0) + 1
    print(list(dct1.values()), list(dct2.values()))
    return list(dct1.values()) == list(dct2.values())


# a = 'RAMBUNCTIOUSLY'
# b = 'THERMODYNAMICS'
# a = 'HAKANK'
# b = 'VISITS'
# a = 'TITLE'
# b = 'URUST'
# a = 'ISOMORPHIC'
# b = 'COMORPHISM'
a = 'ISOMORPHIC'
b = 'GUNINJACGO'
print(are_isomorphic(a, b))

# or


def isomorf(s, z):
    d = {}
    if len(s) != len(z):
        return False, 1
    for i in range(len(s)):
        if s[i] in d:
            if z[i] != d[s[i]]: return False, 2
        else:
            if z[i] in d.values(): return False, 3
            d[s[i]] = z[i]
        print(i, s[i], z[i], d)
    return True


a = input()
b = input()
print(isomorf(a, b))
