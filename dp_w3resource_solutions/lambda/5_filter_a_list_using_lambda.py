"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 14/06/20
* @decription: Write a Python program to filter a list of integers using Lambda.
"""

alist = list(range(1, 11))
print('original:', alist)

odds = list(filter(lambda each_iter: each_iter % 2 != 0, alist))
evens = list(filter(lambda each_iter: each_iter % 2 == 0, alist))

print('odds:', odds)
print('evens:', evens)
