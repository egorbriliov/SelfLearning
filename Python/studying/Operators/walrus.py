"""
The ":=" operator, known as the "walrus operator", was introduced in Python 3.8.
It allows you to assign values to variables in expressions, which can simplify code and make it more readable."""

"""
Usage examples
"""

""" Example 1: Assignment and use in the condition """

# Without walrus operator
value = input("Enter something: ")
if value:
    print(f"You entered: {value}")

# With walrus operator
if value := input("Enter something: "):
    print(f"You entered: {value}")


"""
In this value, the value entered by the user is assigned to the variable value and immediately used in the fundamental if.
Example 2: Using in a loop
"""

# Without walrus operator
data = []
while True:
    value = input("Enter a number (or 'exit to exit): ")
    if value == 'exit':
        break
    data.append(int(value))

# With walrus operator
# Here := allows you to test a condition and assign a value at the same time.
data = []
while (value := input("Enter a number (or 'exit' to exit)")) != 'exit':
    data.append(int(value))


# Benefits
# Code reduction: Reduces the number of lines of code.
# Readability: Makes it easier to understand when a match occurs in conditions.

# Limitations
# The operator cannot be used in expressions where it is not specified
# (for example, in include lists, unless there is an explicit context).
# Using the walrus tool can make your code more concise and maintainable,
# but it should be used with caution so as not to degrade readability.