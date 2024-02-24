# Вторая задача к семнадцатому занятию

def uppercase_deco(func):
    def wrapper(*args, **kwargs):
        res = [x.upper() for x in args if type(x) == str]
        for k, v in kwargs.items():
            if type(v) == str:
                res.append(v.upper())
            if type(v) == list or type(v) == tuple or type(v) == set:
                for i in v:
                    if type(i) == str:
                        res.append(i.upper())
        return res
    return wrapper

@uppercase_deco
def random_msg(*args, **kwargs):
    return
print(random_msg(1, 2, 3, "led", 4, 5, 6, "zepp", "all", 2, 7, 8, 9, "last", abc = "night", v = "i", f = 123, h = 34.5, a = (1, "sat", "on"), e = {57, "the", 4}, b = [12.5, 3, "levee", "and", 101.2, 43, "moaned"]))
