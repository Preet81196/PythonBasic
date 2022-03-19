"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 22/05/20
* @decription: Write a Python program to calculate the hypotenuse of a right angled triangle.
"""


def calculate_hypotenuse(a, b):
    try:
        a, b = float(a), float(b)
        return ((a ** 2) + (b ** 2)) ** (1/2)
    except ValueError:
        return 'please provide int type or float kind of values'


print(calculate_hypotenuse(3.0, 4.0))
