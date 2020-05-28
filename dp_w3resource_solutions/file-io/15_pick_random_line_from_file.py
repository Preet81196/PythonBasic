"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to read a random line from a file.
"""

import random

with open('data.txt') as handle:
    lines = list(handle)
    print(random.choice(lines))
