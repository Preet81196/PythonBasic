"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function to check whether a number is in a given range.
"""


def is_in_range(given_range, check):
    if check in range(given_range[0], given_range[1]+1):
        return True
    else:
        return False


print(is_in_range((3, 6), 7))
