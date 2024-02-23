# Третья задача к семнадцатому занятию

class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square
    def get_color(self):
        while True:
            self.color = input("Enter the color:\n")
            if self.color.isalpha():
                break
            else:
                print("Try again")
    def get_square(self):
        while True:
            try:
                self.square = float(input("Enter the square:\n"))
                break
            except ValueError:
                print("Try again")
    def info(self):
        return f"This thing is of the {self.color} color; its square is {self.square} sq sm"
a = Shape("", 0)
a.get_color()
a.get_square()
print(a.info())
