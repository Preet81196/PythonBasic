"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to find the substrings within a string.
"""


import re

text = 'hello world this is divyesh patel, how beautiful this world is.'
pattern = 'world'
alist = re.findall(pattern, text)
print(alist)