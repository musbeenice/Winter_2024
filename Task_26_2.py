# Вторая задача к двадцать шестому занятию

def dis(self):
    for i in self.__dict__:
        print(i, self.__dict__)


Pet = type("Pet", (), {'dis': dis})
my_pet = Pet()
my_pet.name = "Jerry"
my_pet.age = 2
my_pet.color = "Brown"
my_pet.dis()
