"""Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)."""

import re

txt = "8 times before 11:45 AM"

x = re.findall("[a-zA-Z0-9]", txt)

print(x)


