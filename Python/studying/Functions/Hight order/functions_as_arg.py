"""
Passing Function as an argument to other function

Functions are like objects in Python, therefore, they can be passed as argument to other functions.
Consider the below example, where we have created a function greet which takes a function as an argument.
"""


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function \
    passed as an argument.")
    print(greeting)


greet(shout)
greet(whisper)
