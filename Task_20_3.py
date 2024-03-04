# Третья задача к двадцатому занятию

# class InfSeq:
#     def __init__(self):
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num > 25:
#             self.num = self.num % 26
#         self.num += 1
#         self.let = chr(self.num + 64)
#         return self.num, self.let
#
#
# seq = InfSeq()
# for _ in range(35):
#     n, let = next(seq)
#     print(f"{n}, {let},", end=" ")

# or

class NumLet:
    def __init__(self):
        self.index = 0
        self.num_let = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.num_let = 1 - self.num_let
        if self.num_let == 0:
            self.index += 1
            if self.index > 26: self.index = 1
            return self.index
        else:
            return chr((ord("A")) + self.index - 1)


a = NumLet()
for i in range(36):
    print(next(a), end=" ")

# or


# def can():
#     index = 0
#     while True:
#         if index >= 25:
#             index = 0
#         index += 1
#         yield index
#         yield chr(65 + index - 1)
#
#
# f = can()
# for _ in range(5):
#     print(next(f), end=" ")
