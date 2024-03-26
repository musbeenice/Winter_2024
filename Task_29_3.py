# Третья задача к двадцать девятому занятию

def are_isomorphic(w1, w2):
    if len(w1) == len(w2):
        dct1, dct2 = {}, {}
        for i in range(len(w1)):
            dct1[w1[i]] = dct1.get(w1[i], 0) + 1
            dct2[w2[i]] = dct2.get(w2[i], 0) + 1
        print(list(dct1.values()), list(dct2.values()))
        return list(dct1.values()) == list(dct2.values())
    else:
        return False


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
