"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function to sum all the numbers in a list.
"""


def sum_of_given_list(thelist):
    summation = None
    for each in thelist:
        if summation is None:
            summation = each
        else:
            summation += each
    return summation


print(sum_of_given_list([1, 65, 2, 89, 1, 4]))
