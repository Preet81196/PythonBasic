"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 03/06/20
* @decription: Write a Python program to slice a tuple.
"""

tup = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

first_part = *tup[:5],
second_part = *tup[5:],


print('first_part:', first_part)
print('second_part:', second_part)
