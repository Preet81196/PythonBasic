"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to sum all the items in a list.
"""

import sys


def sum_list(alist):
    try:
        return sum(alist)
    except:
        sys.stderr.write("Error")
        quit()


numbers = [1, 2, 'dfd']
print(sum_list(numbers))
