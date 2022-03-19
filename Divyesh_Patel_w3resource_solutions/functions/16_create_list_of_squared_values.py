"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function to create and print a list where the values are square of numbers
            between 1 and 30 (both included).
"""


def print_square_values_upto(a):
    print([each ** 2 for each in range(1, a+1)])


print_square_values_upto(30)
