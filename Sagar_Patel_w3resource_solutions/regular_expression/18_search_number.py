""" Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. Go to the editor

"Exercises number 1, 12, 13, and 345 are important"""

import re
str = "Exercises number 1, 12, 13, and 345 are important"
results = re.finditer(r"([0-9]{1,3})", str)
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))