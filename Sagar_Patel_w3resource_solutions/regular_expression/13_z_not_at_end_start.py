"""Write a Python program that matches a word containing 'z', not at the start or end of the word."""


import re

txt = input("Enter :")

x = re.findall('\Bz\B', txt)
print(x)