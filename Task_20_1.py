# Первая задача к двадцатому занятию

class Menu:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Person:
    def __init__(self, name, card, cash):
        self.name = name
        self.card = card
        self.cash = cash
        self.purchase = {}

    def buy_drink(self, drink):
        self.purchase[drink[0]] = self.purchase.get(drink[0], 0) + 1
        self.card -= drink[1]

    def buy_meal(self, meal):
        self.purchase[meal[0]] = self.purchase.get(meal[0], 0) + 1
        self.cash -= meal[1]

    def week_report(self, v_machine):
        if v_machine.days % 7 == 0:
            print(f"I spent {format(100 - self.card, ".2f")}$ using my card and {format(20 - self.cash, ".2f")}$ cash "
                  f"after a week of spending money in this vending machine")
            print(f"Also, that's what I drank and ate during {v_machine.days // 7} week(s):")
            for k, v in self.purchase.items():
                print(f"{k.title()}: {v} time(s)")
        else:
            print("Not enough days passed...")


class VendingMachine:
    def __init__(self):
        self.income = 0
        self.days = 0

    def sell_drink(self, drink, person):
        person.buy_drink(drink)
        self.income += drink[1]
        self.days += 1

    def sell_meal(self, meal, person):
        person.buy_meal(meal)
        self.income += meal[1]

    def week_resume(self, person):
        if self.days % 7 == 0:
            print(f"There were {format(self.income, ".2f")}$ gained, "
                  f"selling drinks (and meals) to {person.name} in {self.days // 7} week(s)")
        else:
            print("Not enough days passed...")


menu_drinks = Menu(pos_1=["latte", 1.49],
                   pos_2=["cappuccino", 1.49],
                   pos_3=["espresso", .99])
menu_meals = Menu(pos_1=["pancake", .59],
                  pos_2=["cheesecake", .69],
                  pos_3=["donut", .49])
me = Person("Alex", 100, 20)
vm = VendingMachine()
vm.sell_drink(menu_drinks.kwargs["pos_1"], me)
vm.sell_drink(menu_drinks.kwargs["pos_2"], me)
vm.sell_meal(menu_meals.kwargs["pos_1"], me)
vm.sell_drink(menu_drinks.kwargs["pos_3"], me)
vm.sell_meal(menu_meals.kwargs["pos_3"], me)
vm.sell_drink(menu_drinks.kwargs["pos_3"], me)
vm.sell_drink(menu_drinks.kwargs["pos_1"], me)
vm.sell_meal(menu_meals.kwargs["pos_2"], me)
vm.sell_drink(menu_drinks.kwargs["pos_1"], me)
vm.sell_meal(menu_meals.kwargs["pos_2"], me)
vm.sell_drink(menu_drinks.kwargs["pos_2"], me)
vm.week_resume(me)
me.week_report(vm)
