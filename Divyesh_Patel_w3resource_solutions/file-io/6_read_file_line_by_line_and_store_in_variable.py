"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to read a file line by line store it into a variable.
"""

file_contents = str()
with open('data.txt') as fhandle:
    for each in fhandle:
        file_contents += each

print(file_contents)
