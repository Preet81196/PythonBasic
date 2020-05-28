"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""

alist = [7, 8, 120, 25, 44, 20, 27]
new_list = [each for each in alist if each % 2 != 0]
print(new_list)

