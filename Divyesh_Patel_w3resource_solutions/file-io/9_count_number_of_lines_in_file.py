"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to count the number of lines in a text file.
"""

total_lines = 0
with open('data.txt') as fhandle:
    for line in fhandle:
        total_lines += 1


print(total_lines)
