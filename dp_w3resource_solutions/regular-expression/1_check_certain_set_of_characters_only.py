"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to check that a string contains only a certain set of characters
              (in this case a-z, A-Z and 0-9).
"""

import re


def check_it(statement):
    pattern = '[0-9a-zA-Z]'
    return re.search(pattern, statement)


print(check_it("Divyesh Patel"))
