"""Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'"""
import re

txt = input("Enter :")

x = re.findall("a*?b$", txt)
print(x)