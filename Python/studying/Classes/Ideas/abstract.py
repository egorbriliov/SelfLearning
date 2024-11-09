"""
Gives a chance to create only necessary interface for work with him.
"""

from abc import ABC, abstractmethod

# Created interface
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self) -> None:
        return None


# Creating interface based on created interface
class Car(Vehicle): # Will throw an error as the required methods that were specified in the created interface will be required
    pass

class Motorcycle(Vehicle):

    def go(self):
        print("You drive the Motorcycle")

    def stop(self):
        print("You stop the Motorcycle")
