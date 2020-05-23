"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program that matches a string that has an a followed by zero or more b's.
"""

import re


def check_regex(statement):
    pattern = 'a[b]*?'  # 'a[b]*' also works but it went greedy (will check for another largest) hence added '?' at end
    cpattern = re.compile(pattern)
    if cpattern.search(statement) is None:
        return 'FAIL'
    else:
        return 'PASS'


print(check_regex('Divyesh Patel'))
