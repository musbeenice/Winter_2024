# Третья задача к двадцатому занятию

class InfSeq:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 25:
            self.num = self.num % 26
        self.num += 1
        self.let = chr(self.num + 64)
        return self.num, self.let


seq = InfSeq()
for _ in range(35):
    n, let = next(seq)
    print(f"{n}, {let},", end=" ")
