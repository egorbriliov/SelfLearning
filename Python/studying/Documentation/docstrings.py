u""" The "u" prefix is useful when you want to use Unicod symbols """
f""" The "f" prefix is ​​useful when you want to use variables. """
r""" The "r" prefix is ​​useful when you want to use a string format without 
using string formatting.. """

# Docstrings rules:
# 1. Ends with point.
# 2. Docstrings start and ends after and before code, without space between 
# there. (When you describe class, you should add one space line after that)
 
#  Module docstrings (__init__.py) rules:
# 1. Describe the classes, exceptions, functions, and obligations that can 
# be exported from a module using a short comment.
#  

class Example:
    """This is an "attribute docstrings" located in __doc__ function."""
    """
    This is an "additional docstrings", it will be ignored compiler, 
    but will be recognized by Docutils.
    """
    
    def __init__(self, a: str, b: int, c: list) -> None:
        self.a: str = a
        self.b: int = b
        self.c: list = c

    def addition(self, first: int, second: int, *args) -> int:
        """Adds two numbers
        
        Parametrs:
        ----------
        
            first: intp
            Term.
            
            second:  int
            Term.
            
        Returns:
        --------

            Sum of your numbers
        
        """
        sum_numbers: int = sum([first, second])           
        if args:
            sum_args: int = sum(args)
            return sum_numbers + sum_args
        return sum_numbers

    def subtraction(self, minuend: int, subtrahend: int) -> int:
        return minuend - subtrahend   


