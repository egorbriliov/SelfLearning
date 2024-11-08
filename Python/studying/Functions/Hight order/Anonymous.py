"""
Anonymous functions:
Also known as lambda functions, which are not declared using
the standard keyword (def in Python, for example).
"""
# Example 1: describe how to write
function = lambda x: print(x)
function("zxc")

# Example 2: with using more than 1 parameter
function = lambda x, z: print(x, z)
function("zxc", "cxz")

# Example 3: lambda function in other function
numbers: list = [1, 2, 3]
squares: list = list(map(lambda x: x ** 2, numbers))
print(squares)
