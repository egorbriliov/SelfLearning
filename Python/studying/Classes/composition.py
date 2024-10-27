"""
Aggregation = A relationship where one object contains reference to other INDEPENDENT objects
              "has-a" relationship

Composition = The composed object directly owns components, which exists independently
              "owns-a" relationship.
"""

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels: list[Wheel] = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

print(car1.display_car())

print(car2.display_car())