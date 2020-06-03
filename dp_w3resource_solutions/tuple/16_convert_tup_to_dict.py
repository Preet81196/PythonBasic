"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 03/06/20
* @decription: Write a Python program to convert a tuple to a dictionary.
"""

tup = ('name', 'Divyesh'), ('city', 'Mumbai')

x = dict((x, y) for x, y in tup)
print(x)
