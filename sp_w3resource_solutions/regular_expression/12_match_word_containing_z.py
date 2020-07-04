"""Write a Python program that matches a word containing 'z'."""


import re

txt = input("Enter :")

x = re.findall('\w*z.\w*', txt)
print(x)