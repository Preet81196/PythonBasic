"""Write a Python program that matches a word at the beginning of a string"""
import re

txt = input("Enter :")

x = re.findall("^\w+", txt)
print(x)