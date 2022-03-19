"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com
* @date: 23/05/20
* @decription: Write a Python program to read last n lines of a file.
"""

fhandle = open('data.txt')
number_of_last_lines = 2
counter = 0
for each_line in reversed(list(fhandle)):
    if counter == number_of_last_lines:
        break
    counter += 1
    print(each_line.strip())
