"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 08:49:53
 * @modify date 19-05-2020 08:49:53
 * @desc Write a Python program to get the least common multiple (LCM) of two positive integers.
"""

def get_lcm(firstn, secondn):
    if firstn % secondn == 0 or secondn % firstn == 0:
        return max(firstn, secondn)
    
    lowest_of_two = min(firstn, secondn)
    for each in range(lowest_of_two, firstn * secondn + 1, lowest_of_two):
        if each % firstn == 0 and each % secondn == 0:
            return each


if __name__ == '__main__':
    print('LCM:', get_lcm(12, 17))