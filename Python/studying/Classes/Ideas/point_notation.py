""" Example how you can use point notation in organizations your classes"""

class Example:
    """An example of a classes whose parameters and methods we will use in the point notation"""
    name: str = "Example"

    @classmethod
    def print_name(cls) -> None:
        """Prints class name"""
        print(cls.name)
        return None

class Notation:
    """Class witch explain point notation usage"""
    def __init__(self):
        pass

    @property
    def name(self) -> Example:
        """Returns the name of the included class"""
        return Example()



if __name__ == '__main__':
    """Example of usage"""
    # Creating obj, but can work with cls
    notation: Notation = Notation()
    # Example of usage point notation
    notation.name.print_name()

