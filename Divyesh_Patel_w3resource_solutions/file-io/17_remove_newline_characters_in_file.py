"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to remove newline characters from a file.
"""

alist = list()
with open('data.txt') as handle:
    for each in handle:
        alist.append(each.strip())

print(alist)
