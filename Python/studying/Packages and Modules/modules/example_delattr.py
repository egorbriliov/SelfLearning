# delattr() function can be used to delete attribute from class object

class Example:
    def __init__(self):
        self.example = "example"


if __name__ == "__main__":
    example = Example()
    print(f"\nHas been created new object: {example.__str__()}")


    def attribute_check():
        """If object attribute available returns True else False"""
        try:
            value = example.example
            return "Object attribute is available"
        except Exception as E:
            return "Object attribute is not available"


    print(f"\nStatus attribute before using delattr(): \n{attribute_check()}")

    delattr(example, "example")
    print("\nAttribute has been deleted with using delattr()")
    print(f"\nStatus attribute after using delattr(): \n{attribute_check()}")
