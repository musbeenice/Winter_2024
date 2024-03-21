# Вторая задача к двадцать седьмому занятию

class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name.title()

    @property
    def total(self):
        return self.price * self.quantity


q = Item("lamp", .99, 101)

print(q.name)
print(q.total)
