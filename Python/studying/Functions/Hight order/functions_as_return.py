"""
Returning function

As functions are objects, we can also return a function from another function. In the below example, the create_adder
function returns adder function.
"""


# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_15 = create_adder(15)

print(add_15(10))
