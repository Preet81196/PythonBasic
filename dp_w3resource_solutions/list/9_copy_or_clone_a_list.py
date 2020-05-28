"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to clone or copy a list.
"""

# Related docs can be found here: https://en.wikipedia.org/wiki/Object_copying#Shallow_copy

alist = [1, 2, 3]
new_list = alist.copy()

new_list.append(67)
print('new list:', new_list)
print('alist:', alist)
