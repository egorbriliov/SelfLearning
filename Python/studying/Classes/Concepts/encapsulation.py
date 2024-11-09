# A key principle of OOP is the ability to hide certain parts of the objects’ data from the outside,
# a concept known as Encapsulation.


class Human:
	def __init__(self, age: int, height: int, weight: float, name: str):
		self.age: int = age
		self.height: int = height
		self.weight: float = weight
		self.name: str = name.lower()

egor: Human = Human(
				age=20,
			    height=174,
			    weight=76.5,
                name="Egor"
			    )

print(f"{egor.name.title()} is {egor.age} years old. He's weight is {egor.weight} and height is a {egor.height}.")