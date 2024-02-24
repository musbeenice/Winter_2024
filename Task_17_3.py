# Третья задача к семнадцатому занятию

class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square
    def set_color(self):
        while True:
            self.color = input("Enter the color:\n")
            if self.color.isalpha():
                break
            else:
                print("Try again")
    def get_color(self):
        print(self.color)
    def set_square(self):
        while True:
            try:
                self.square = float(input("Enter the square:\n"))
                break
            except ValueError:
                print("Try again")
    def get_square(self):
        print(self.square)
    def info(self):
        print(f"The thing is of the {self.color} color; its square is {self.square} sq sm")
a = Shape(0, 0)
a.set_color()
a.set_square()
a.get_color()
a.get_square()
a.info()
