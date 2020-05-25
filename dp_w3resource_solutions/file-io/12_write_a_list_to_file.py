"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to write a list content to a file.
"""

alist = ['Divyesh', 'Preet', 'Rushabh', 'Karan', 'Harshu']
with open('target.txt', 'w') as handle:
    for each in alist:
        handle.write(each+'\n')
