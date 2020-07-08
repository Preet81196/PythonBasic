""" Write a Python program where a string will start with a specific number."""
import re

txt = input("Enter :")

x = re.findall('^[0-9_]', txt)
print(x)