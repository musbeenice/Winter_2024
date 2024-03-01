# Вторая задача к девятнадцатому занятию

class Fibonacci:
    def __init__(self):
        self.f_1 = 0
        self.f_2 = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.f_1, self.f_2 = self.f_2, self.f_1 + self.f_2
        return self.f_1

fib_iter = Fibonacci()

for i in range(int(input())):  # вывод: n членов последовательности 
    print(next(fib_iter), end=" ")
