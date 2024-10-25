"""
Polymorphism = Greek word that means to "have many forms or faces"
               Poly = Many
               Morphe = Form

                TWO WAYS TO ACHIEVE POLYMORPHISM
                1. Inheritance = An object could be treated of the same type as a parent class
                2. "Duck typing" = Object must have necessary attributes/methods
"""

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.15 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5



shapes = [Circle(4), Square(5), Triangle(6, 7 )]

for shape in shapes:
    print(f"{shape.area()}cm")
