# Вторая задача к семнадцатому занятию

def uppercase_deco(func):
    def wrapper(*args, **kwargs):
        res = " ".join([x.upper() for x in args if type(x) == str])
        for k, v in kwargs.items():
            for i in v:
                if type(i) == str:
                    res += " " + i.upper()
        return res
    return wrapper

@uppercase_deco
def random_msg(*args, **kwargs):
    return
print(random_msg(1, 2, 3, "all", 4, 5, 6, "last", "night", 2, 7, 8, 9, "i", a = [1, "sat", "on", 57, "the", 4], b = [12.5, 3, "levee", "and", 101.2, 43, "moaned"]))
