"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to map two lists into a dictionary.
"""

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

adict = dict()

for key, value in zip(keys, values):
    adict[key] = value

print(adict)
