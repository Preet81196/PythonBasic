"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 07/06/20
* @decription: Write a Python program to create a new JSON file from an existing JSON file.
"""

with open('6_one.json') as handle:
    data = handle.read().strip()

with open('6_two.json', 'w') as whandle:
    whandle.write(data)

