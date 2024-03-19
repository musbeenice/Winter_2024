# Третья задача к двадцать шестому занятию

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age_1):
        self._age = age_1 if 1 <= age_1 <= 100 else None
        if self._age is None:
            raise ValueError("Недопустимый возраст")

    @age.deleter
    def age(self):
        del self._age


p = Person(20)
p.age = 30
print(p.age)
p.age = 0
