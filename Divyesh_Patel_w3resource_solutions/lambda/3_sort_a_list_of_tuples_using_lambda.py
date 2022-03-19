"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 14/06/20
* @decription: Write a Python program to sort a list of tuples using Lambda.
"""

alist = [(1, 2), (-1, 15), (2, 16), (-4, 1)]
print(alist)

alist.sort(key=lambda tup: tup[1])
print(alist)
