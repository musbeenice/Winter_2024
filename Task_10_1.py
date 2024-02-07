# Первая задача к десятому занятию

# s = ["Мой дядя самых честных правил\n", "Когда не в шутку занемог\n"]
# with open("test1.txt", "w", encoding="utf-8") as f:
#     f.writelines(s)

# with open("test1.txt", encoding="utf-8") as f_1:
#     s = f_1.readlines()
#     print(s)
#     with open("test2.txt", "w", encoding="utf-8") as f_2:
#         for i in s[::-1]:
#             w = " ".join(i.split()[::-1])
#             print(w, file=f_2)

# with open("test2.txt", encoding="utf-8") as f_3:
#     z = f_3.readlines()
#     print(z)

# or

with open("test1.txt", "r") as f1:
    lst = f1.readlines()

print(lst)

with open("test2.txt", "w") as f2:
    for i in lst[::-1]:
        print(" ".join(i.strip().split()[::-1]), file=f2)

with open("test2.txt", "r") as f3:
    for i in f3:
        print(i.strip())
