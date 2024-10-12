import re

"Descriptions"

# Method re.search in Python is used to search pattern in string
# re.search received: re.object if finding else None
# string: string where will be tried to found pattern
# pattern: that what will be searched for in the string

"Examples"

# Will returned None, because of not started with pattern "f"
value_1 = re.search(pattern="f", string="zxc")

# Will returned re object
value_2 = re.search(pattern="f", string="f")

# You can also use flags in re.match as parameter
value_3 = re.search(pattern="f", string="f", flags=re.IGNORECASE)