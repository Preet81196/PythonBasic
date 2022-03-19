"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 14/06/20
* @decription: Write a Python program to create a function that takes one argument,
            and that argument will be multiplied with an unknown given number.
"""


def make_multiplier(x):
    return lambda n: x*n


f = make_multiplier(12)

print(f(2))
