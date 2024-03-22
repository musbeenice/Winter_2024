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

# or


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, item):
        if item == "name":
            return object.__getattribute__(self, item).title()
        else:
            return object.__getattribute__(self, item)

    def __getattr__(self, item):
        if item == "total":
            return self.price * self.quantity
        else:
            raise AttributeError


c = Item("closet", .99, 101)
print(c.total, c.name)
print(c.color)
