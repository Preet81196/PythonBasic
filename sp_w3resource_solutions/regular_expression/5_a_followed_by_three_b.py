"""Write a Python program that matches a string that has an a followed by three 'b'."""
import re

txt = input("Enter :")

x = re.findall("ab{3}", txt)
print(x)