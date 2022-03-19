"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 03/06/20
* @decription: Write a Python program to convert a list to a tuple.
"""

alist = [1, 2, 3, 4, 5]

tup = *alist,  # Another way, tuple(alist)

print('type(tup):', type(tup))
print('tup:', tup)
