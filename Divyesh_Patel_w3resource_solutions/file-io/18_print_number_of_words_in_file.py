"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program that takes a text file as input and returns the number of words of a given
        text file.
"""

# Note: Some words can be separated by a comma with no space.

with open('data.txt') as handle:
    data = handle.read()
    data = data.replace(',', ' ')
    alist = data.split(' ')
    print(len(alist))


