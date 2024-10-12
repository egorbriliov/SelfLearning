import re

"Descriptions"

# Module re also has a flags
# Definition of flags:

# re.IGNORECASE makes the match case-insensitive
ignore_case = re.IGNORECASE

#
multiline = re.M or re.MULTILINE

# re.VERBOSE give a chance to use commentaries and multi-line patterns
pattern = r'''
\d+ # Some comments
\s+ # Some comments
\w+ # Some comments 
'''
verbose_1 = re.match(pattern=pattern, string="f", flags=re.VERBOSE)

# re.DOTALL allows the character "." to match any character, including a newline.
dotall = re.DOTALL

"Examples"

# Flags using as parameter
match_1 = re.match(pattern="f", string="f", flags=re.M)

# You can also simultaneously use many flags with use "|"
match_2 = re.match(pattern="f", string="f", flags=re.M | re.IGNORECASE)

