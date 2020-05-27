"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to get the largest number from a list
"""


# TODO: Handle Errors for blank or different type input in a single line if else, if possible
def get_largest(local_alist):
    return max(local_alist) if local_alist is not None or len(local_alist) != 0 else None


# alist = [1, 2, 3]
# alist.clear()
print(get_largest([1, 2, 3]))
