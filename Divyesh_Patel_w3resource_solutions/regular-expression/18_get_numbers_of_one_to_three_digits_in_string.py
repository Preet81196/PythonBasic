"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
"""

import re


def check_me(statement):
    pattern = '[0-9]{1,3}'
    # TODO: if we add 5120 in statement it returns ['512', '0'], restrict 1200 kinda numbers in output
    return re.findall(pattern, statement)


print(check_me('I have 120 rupees and i gave 10 rupees to someone'))
print(check_me('I have 5120 rupees and i gave 10 rupees to someone'))
