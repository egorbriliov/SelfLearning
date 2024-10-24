# enumerate() function adds a counter to an iterable and returns it as an enumerate object

# Example
if __name__ == "__main__":
    example: list = ["a", "b", "C"]
    print("Iteration was started!")
    for index, element in enumerate(example, start=1):
        print(f"{index}: {element}")
    print("Iteration was ended!")


