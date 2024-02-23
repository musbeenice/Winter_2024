# Третья задача к семнадцатому занятию

class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square
    def get_color(self):
        self.color = input("Enter the color:\n")
    def get_square(self):
        self.square = float(input("Enter the square:\n"))
    def info(self):
        return f"This thing is of the {self.color} color; its square is {self.square} sq sm"
a = Shape("", 0)
a.get_color()
a.get_square()
print(a.info())
