"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to find sequences of lowercase letters joined with a underscore.
"""

import re


def check_me(statement):
    pattern = '[a-z]+_[a-z]+'
    if re.search(pattern, statement) is None:
        return 'FAIL'
    else:
        return 'PASS'


print(check_me('hello_world'))
print(check_me('hello_World'))
print(check_me('Divyesh Patel'))
