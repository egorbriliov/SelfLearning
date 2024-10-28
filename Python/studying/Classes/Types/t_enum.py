from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)