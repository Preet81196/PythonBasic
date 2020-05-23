"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function to multiply all the numbers in a list.
"""


def mul_of_given_list(thelist):
    mul = None
    for each in thelist:
        if mul is None:
            mul = each
        else:
            mul *= each
    return mul


print(mul_of_given_list([-1, 65, -2]))
