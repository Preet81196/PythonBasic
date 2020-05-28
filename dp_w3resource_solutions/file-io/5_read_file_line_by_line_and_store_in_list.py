"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to read a file line by line and store it into a list.
"""

alist = list()

with open('data.txt') as fhandle:
    for each in fhandle:
        alist.append(each.strip())

print(alist)
