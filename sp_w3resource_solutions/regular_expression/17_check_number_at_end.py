"""Write a Python program to check for a number at the end of a string."""

import re

txt = input("Enter :")

x = re.findall('[\b0-9_]', txt)

print(x)