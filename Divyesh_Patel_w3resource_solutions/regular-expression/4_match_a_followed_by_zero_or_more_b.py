"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program that matches a string that has an a followed by zero or more b's.
"""

import re


def check_me(statement):
    pattern = 'a[b]+'
    if re.search(pattern, statement) is None:
        return 'FAIL'
    else:
        return 'PASS'


print(check_me('Divyesh Patel'))
print(check_me('Divyesh Pabel'))








