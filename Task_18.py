# Задача к восемнадцатому занятию

from random import *

class Tasks:
    def __init__(self, hometasks):
        self.hometasks = hometasks
class Professor:
    def __init__(self):
        self.work = 0
        self.verdict = {}
    def give_task(self, hometask, student):
        student.receive(hometask)
        self.work += 1
    def check(self, student):
        for task in student.send_away():
            self.verdict[task + f"_{student.name}"] = self.verdict.get(task + f"_{student.name}", 0) + randint(0, 1)
        return self.verdict
    def __str__(self):
        if self.work == 1:
            return f"Professor has given just one task and it was{"".join([" not " if v == 0 else " " for v in self.verdict.values()])}solved correctly"
        else:
            res = 0
            for v in self.verdict.values():
                res += v
            return f"Professor has given {self.work} tasks and {res} of them were solved corretly"
class Student:
    group = []
    def __init__(self, name):
        self.name = name
        self.tasks = []
        Student.group.append(self)
    def receive(self, hometask):
        self.tasks.append(hometask)
    def send_away(self):
        return self.tasks
    def __str__(self):
        return f"Student {self.name} has received and solved {", ".join([i for i in self.tasks])}"

ht = Tasks(["Task_1", "Task_2", "Task_3", "Task_4", "Task_5", "Task_6", "Task_7", "Task_8"])

some_prof = Professor()
alex = Student("Alex")
pyotr = Student("Pyotr")
stepa = Student("Stepa")

some_prof.give_task(ht.hometasks[0], alex)
some_prof.give_task(ht.hometasks[5], alex)
some_prof.give_task(ht.hometasks[5], pyotr)
some_prof.give_task(ht.hometasks[7], pyotr)
some_prof.give_task(ht.hometasks[3], stepa)
some_prof.give_task(ht.hometasks[0], stepa)
some_prof.check(alex)
some_prof.check(pyotr)
some_prof.check(stepa)
print(alex)
print(pyotr)
print(stepa)
print(some_prof)
