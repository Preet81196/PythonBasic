"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 03/06/20
* @decription: Write a Python program to reverse a tuple.
"""

tup = 1, 2, 3, 4, 5

alist = list(tup)
alist.reverse()

tup = tuple(alist)
print(tup)
