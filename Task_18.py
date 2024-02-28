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
        student.receive_hometask(hometask)
        self.work += 1
    def check(self, student):
        self.verdict = {task: randint(0, 1) for task in student.send_away()}
        return self.verdict
class Student:
    group = []
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.results = []
        Student.group.append(self)
    def receive_hometask(self, hometask):
        self.tasks.append(hometask)
    def send_away(self):
        return self.tasks
    def receive_verdict(self, professor):
        self.results.extend(task for task, res in professor.check(self).items() if res == 1)
    def __str__(self):
        return f"Student {self.name} has received and solved {', '.join(self.tasks)}. These tasks were correct: {', '.join(self.results) if self.results != [] else None}"

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
alex.receive_verdict(some_prof)
pyotr.receive_verdict(some_prof)
stepa.receive_verdict(some_prof)
print(alex)
print(pyotr)
print(stepa)
