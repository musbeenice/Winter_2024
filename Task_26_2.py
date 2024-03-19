# Вторая задача к двадцать шестому занятию

def dis(self):
    output = []
    for k in self.__dict__.keys():
        output.append(k)
    return ", ".join(output)


Pet = type("Pet", (), {'dis': dis})
my_pet = Pet()
my_pet.name = "Jerry"
my_pet.age = 2
my_pet.color = "Brown"
print(my_pet.dis())
