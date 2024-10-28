# super() = Function used in a child class to call methods from parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

from enum import Enum

class Colors(Enum):
    Pink: str = "pink"
    Red: str = "red"
    Blue: str = "blue"
    Yellow: str = "yellow"

class Shape:
    def __init__(self, color, is_filled) -> None:
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius) -> None:
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle  with an area of {3.14 * self.radius * self.radius}cm^2")


class Square(Shape):
    def __init__(self, color, is_filled, width) -> None:
        super().__init__(color, is_filled)
        self.width = width


class Triangle(Square):
    def __init__(self, color, is_filled, width, height) -> None:
        super().__init__(color, is_filled, width)
        super().describe()
        self.height = height

shape = Shape(color=Colors.Blue, is_filled=False)
circle = Circle(color=Colors.Red, is_filled=True, radius=5)
square = Square(color=Colors.Pink, is_filled=False, width=6)
triangle = Triangle(color=Colors.Yellow, is_filled=True, width=7, height=8)

shape.describe()
circle.describe()
