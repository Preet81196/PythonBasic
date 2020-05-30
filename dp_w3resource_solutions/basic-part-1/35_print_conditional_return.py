"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 09:45:29
 * @modify date 19-05-2020 09:45:29
 * @desc Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
"""

def conditional_return(a, b):
    if (a is b) or ((a + b) is 5) or (abs(a - b) is 5): return True
    else: return False

print(conditional_return(10, 5))
