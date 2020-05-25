"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to get the file size of a plain file
"""

# Related docs can be found here https://docs.python.org/3/library/stat.html#stat.ST_SIZE

import os
file_size = None

file_stats = os.stat('data.txt')
print(file_stats.st_size)  # in bytes

