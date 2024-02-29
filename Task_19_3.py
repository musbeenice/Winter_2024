# Третья задача к девятнадцатому занятию

class Person:
    def __init__(self, sname, name, mname):
        self.sname = sname
        self.name = name
        self.mname = mname

    def __str__(self):
        return f"{self.mname[::-1] + self.name[::-1] + self.sname[::-1]}"

p = Person("Plant", "Robert", "Anthony")
print(p)
