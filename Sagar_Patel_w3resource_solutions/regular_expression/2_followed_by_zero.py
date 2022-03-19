"""Write a Python program that matches a string that has an a followed by zero or more b's."""
import re

txt = input("Enter")

x = re.findall("a0b*?", txt)

print(x)