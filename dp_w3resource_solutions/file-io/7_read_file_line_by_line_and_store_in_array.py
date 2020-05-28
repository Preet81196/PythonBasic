"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to read a file line by line store it into an array.
"""

super_array = []
with open('data.txt') as fhandle:
    for each in fhandle:
        super_array.append(each)

print(super_array)
