# Первая задача к двадцать шестому занятию

def are_alike(a, b):
    if len(a) == len(b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
            if count == 2:
                return False
        else:
            return True
    else:
        return False


msg1, msg2 = input(), input()
print(are_alike(msg1, msg2))
