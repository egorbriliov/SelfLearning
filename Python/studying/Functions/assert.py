
def number_squared(number: int | float) -> int | float:
    """
    Squares a number.
    Number: must be more than zero
    """
    # Will call an error if number will be lower than zero
    assert number > 0, "number must be more than zero"
    return number ** 2

# Normal number
number_1: int = 2
# The number that will cause an error
number_2: int = -1

for number in [number_1, number_2]:
    print(f"{number} squared  = {number_squared(number)}")