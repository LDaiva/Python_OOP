class Rectangle:
    def __init__(self, name, l, w):
        self.name = name
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Square:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def area(self):
        return self.side ** 2

class Circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

rectangle1 = Rectangle("Rectangle", 10,20)
square1 = Square("Square",10)
circle1 = Circle("Circle", 7.5)

shapes = [rectangle1, square1, circle1]
for shape in shapes:
    print(f"{shape.name} - {shape.area()}")
