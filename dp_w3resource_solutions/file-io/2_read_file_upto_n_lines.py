"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to read first n lines of a file.
"""

fhand = open('data.txt')
n = 3
line_count = 0

for line in fhand:
    if line_count == n:
        break
    line_count += 1
    print(line, end='')
