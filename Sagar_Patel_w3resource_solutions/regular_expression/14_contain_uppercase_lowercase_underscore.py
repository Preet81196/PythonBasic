"""Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores."""
import re

txt = input("Enter :")

x = re.findall('^[a-zA-Z0-9_]*$', txt)
print(x)