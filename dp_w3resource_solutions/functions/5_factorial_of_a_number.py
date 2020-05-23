"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function to calculate the factorial of a number (a non-negative integer).
            The function accepts the number as an argument.
"""


def get_factorial(a):
    if not isinstance(a, int) and a <= 0:
        return None
    else:
        factorial = 1
        for each in range(1, a+1):
            factorial *= each

        return factorial


print(get_factorial(3))
