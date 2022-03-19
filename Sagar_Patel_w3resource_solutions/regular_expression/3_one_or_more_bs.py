"""Write a Python program that matches a string that has an a followed by one or more b's."""
import re

txt = input("Enter :")

x = re.findall("ab+", txt)

print(x)