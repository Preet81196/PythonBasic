"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function to check whether a number is perfect or not.
"""


def is_perfect_number(a):
    if not isinstance(a, int) or a <= 0:
        return False

    summation = 0
    for each in range(1, a):
        if a % each == 0:
            summation += each
    if summation == a:
        return True
    return False


print(is_perfect_number(6))
