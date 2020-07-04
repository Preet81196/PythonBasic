"""Write a Python program that matches a word at the end of string, with optional punctuation."""

import re

txt = input("Enter :")

x = re.findall("\w+\S*$", txt)
print(x)