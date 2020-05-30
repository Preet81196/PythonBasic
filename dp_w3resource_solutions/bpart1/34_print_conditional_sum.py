"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 09:40:27
 * @modify date 19-05-2020 09:40:27
 * @desc Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""

def conditional_sum(a, b):
    answer_sum = a + b
    if (answer_sum >= 15) and (answer_sum <= 20): return 20
    else: return answer_sum

print(conditional_sum(10, 6))
