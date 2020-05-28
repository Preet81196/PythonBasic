"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to flatten a shallow list.
"""

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
flattened_list = [each for each_list in original_list for each in each_list]

print(flattened_list)
