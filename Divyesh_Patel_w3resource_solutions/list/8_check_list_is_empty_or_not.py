"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to check a list is empty or not.
"""


def is_empty(local_list):
    return len(local_list) == 0


alist = [1, 1, 2, 3, 3, 5, 6, 6, 5, 3, 4, 5, 5, 2, 1, 5, 8]
print(is_empty(alist))
