"""Write a Python program that matches a string that has an a followed by zero or one 'b'."""
import re

txt = input("Enter :")

x = re.findall("ab?", txt)
print(x)