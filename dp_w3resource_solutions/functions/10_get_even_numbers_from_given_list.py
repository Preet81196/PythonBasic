"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to print the even numbers from a given list.
"""


def get_even_numbers(alist):
    if not isinstance(alist, list) and len(alist) == 0:
        return None
    evens = list()
    for each in alist:
        if each % 2 == 0:
            evens.append(each)
    return evens


print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
