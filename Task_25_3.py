# Третья задача к двадцать пятому занятию

s = input().split()
print("".join([x.title() for x in s]))
# or
print("".join(map(lambda x: x.title(), s)))
