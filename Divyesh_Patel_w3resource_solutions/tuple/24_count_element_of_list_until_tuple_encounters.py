"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python program to count the elements in a list until an element is a tuple
"""

alist = [10, 20, 30, (10,20), 40]
count = 0

for each in alist:
    if isinstance(each, tuple):
        break
    count += 1

print(count)
