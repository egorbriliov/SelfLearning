import re

"Descriptions"

# Method re.match in Python is used to search for a match at the beginning of a string with a specified pattern.
# re.match received:
# string: string where will be tried to found pattern
# pattern: that what will be searched for in the string

"Examples"

# Will returned None, because of not started with pattern "f"
value_1 = re.match(pattern="f", string="zxc")

# Will returned re object
value_2 = re.match(pattern="f", string="f")

# You can also use flags in re.match as parameter
value_3 = re.match(pattern="f", string="f", flags=re.IGNORECASE)




