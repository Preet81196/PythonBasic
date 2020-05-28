"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to assess if a file is closed or not.
"""

# with open closes the file as we come out of the indentation,
# otherwise we need to close manually for previous methods

with open('data.txt') as handle:
    pass

print(handle.closed)
