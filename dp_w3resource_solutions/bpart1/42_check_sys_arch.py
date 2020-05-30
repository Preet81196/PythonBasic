"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 20-05-2020 08:04:32
 * @modify date 20-05-2020 08:04:32
 * @desc Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""

# Documentation can be found here: https://docs.python.org/3/library/sys.html#sys.maxsize

ARCH_64 = 2 ** 63 - 1
ARCH_32 = 2 ** 31 - 1

import sys

def get_sys_arch():
    if sys.maxsize == ARCH_64:
        return "64 Bit"
    elif sys.maxsize == ARCH_32:
        return "32 Bit"
    else:
        return "Unknown"

if __name__ == '__main__':
    print(get_sys_arch())