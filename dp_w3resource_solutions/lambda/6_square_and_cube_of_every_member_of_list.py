"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 14/06/20
* @decription: Write a Python program to square and cube every number in a given list of integers using Lambda.
"""

alist = list(range(1, 6))
print('original:', alist)

squares = list(map(lambda each_iter: each_iter ** 2, alist))
cubes = list(map(lambda each_iter: each_iter ** 3, alist))

print('squares:', squares)
print('cubes:', cubes)
