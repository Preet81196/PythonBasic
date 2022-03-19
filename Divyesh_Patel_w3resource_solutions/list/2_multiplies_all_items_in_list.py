"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to multiplies all the items in a list.
"""

alist = [1, 2, 3, 4, 5, 6]

mul = None
for each in alist:
    if mul is None:
        mul = each
    else:
        mul *= each

print(mul)
