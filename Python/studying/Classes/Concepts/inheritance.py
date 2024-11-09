# Other key principles are Inheritance, a way to form new classes using classes that have already been defined.

from enum import Enum

class Pronouns(Enum):
    """
    Pronouns for a person
    """
    HE: str = "he"
    SHE: str = "she"
    IT: str = "it"


class Human:
    def __init__(self, age: int, height: int, weight: float, name: str, pronoun: Pronouns):
        self.age: int = age
        self.height: int = height
        self.weight: float = weight
        self.name: str = name.lower()
        self.pronoun: Pronouns = pronoun


egor: Human = Human(
    age=20,
    height=174,
    weight=76.5,
    name="Egor",
    pronoun=Pronouns.HE
)

alex: Human = Human(
    age=18,
    height=179,
    weight=81.2,
    name="Alex",
    pronoun=Pronouns.HE
)

ksenia: Human = Human(
    age=18,
    height=172,
    weight=53.1,
    name="Ksenia",
    pronoun=Pronouns.SHE
)

for person in [egor, alex, ksenia]:
    print(f"\n{person.name.title()} is {person.age} years old. \n" +
          f"{person.pronoun.value.title()}'s weight is {person.weight} and height is a {person.height}.")


