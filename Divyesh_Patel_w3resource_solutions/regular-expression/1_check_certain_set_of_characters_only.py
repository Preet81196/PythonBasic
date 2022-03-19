"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to check that a string contains only a certain set of characters
              (in this case a-z, A-Z and 0-9).
"""

import re


def check_for_certain_chars(statement):
    # This pattern checks for any non (a to z, A to Z and 0 to 9) characters, and returns match object
    # if finds any other character than listed characters (due to ^ which acts as a NOT in this)
    # if it not find any, it returns None (note, we allowed a space)

    pattern = '[^a-zA-Z0-9 ]+'  # This means get elements other than listed, if NONE then all good
    if re.search(pattern, statement) is None:
        return 'PASS'  # Nothing found
    else:
        return 'FAIL'  # Found problematic character

    # cpattern = re.compile(pattern)
    # if cpattern.search(statement) is None:
    #     return 'PASS'  # Nothing found
    # else:
    #     return 'FAIL'  # Found problematic character


print(check_for_certain_chars('Divyesh & Patel'))
print(check_for_certain_chars('Divyesh Patel'))
