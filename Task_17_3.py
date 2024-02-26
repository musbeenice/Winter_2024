# Третья задача к семнадцатому занятию

class Shape:
    def __init__(self, color="Red", square=0):
        self.color = color
        self.square = square
    def get_color(self):
        return self.color
    def get_square(self):
        return self.square
    def set_color(self, col = "Black"):
        self.color = col
    def set_square(self, sq = 0):
        self.square = sq
abc = Shape()
print(abc.color, abc.square)
abc.set_color("Green")
print(abc.get_color())
abc.set_color()
print(abc.get_color())
abc.set_square(25)
print(abc.get_square())

# or

# class Shape:
#     def __init__(self, color="Red", square=0):
#         self.color = color
#         self.square = square
#     def set_color(self):
#         while True:
#             self.color = input("Enter the color:\n")
#             if self.color.isalpha():
#                 break
#             else:
#                 print("Try again")
#     def get_color(self):
#         return self.color
#     def set_square(self):
#         while True:
#             try:
#                 self.square = float(input("Enter the square:\n"))
#                 break
#             except ValueError:
#                 print("Try again")
#     def get_square(self):
#         return self.square
#     def info(self):
#         print(f"The thing is of the {self.color} color; its square is {self.square} sq sm")
# a = Shape()
# print(a.color, a.square)
# a.set_color()
# a.set_square()
# print(a.get_color())
# print(a.get_square())
# a.info()
