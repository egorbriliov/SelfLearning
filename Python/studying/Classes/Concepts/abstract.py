from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self) -> None:
        return None

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):

    def go(self):
        print("You drive the Motorcycle")

    def stop(self):
        print("You stop the Motorcycle")
