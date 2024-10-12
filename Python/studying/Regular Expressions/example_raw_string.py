"""Description"""
import re

# Raw strings are used to ignore special characters as "/"
raw_string = r"123/s"  # As you can see you need to use "r" before "

"Examples"
# Tried to find "/" in line
example_1 = re.search(pattern=r"/", string=r"zxc/")

# Tried to find "/n" in line
example_2 = re.search(pattern=r"/n", string=r"xcz/nzx")

# You also can use raw string when using creating path strings
path = r"C:\Users\Name\Documents"



