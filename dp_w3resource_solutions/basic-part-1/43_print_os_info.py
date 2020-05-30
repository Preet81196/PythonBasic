"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 20-05-2020 08:17:59
 * @modify date 20-05-2020 08:17:59
 * @desc Write a Python program to get OS name, platform and release information.
"""

import os

print("OS:", os.name)
print("Platform:", os.uname().sysname)
print('Release info:', os.uname().release)