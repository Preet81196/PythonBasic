"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 09:35:05
 * @modify date 19-05-2020 09:35:05
 * @desc Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""

def conditional_sum(a, b, c):
    if (a is b) or (b is c) or (a is c):
        return 0

    return a + b + c

if __name__ == '__main__':
    print(conditional_sum(-1, 1, 3))