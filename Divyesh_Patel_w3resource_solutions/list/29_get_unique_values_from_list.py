"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 28/05/20
* @decription: Write a Python program to get unique values from a list
"""

numbers = [12, 3, 4, 6, 12, 56, 2, 6, 34, 20, 10, 38, 59, 95, 9, 96, 64, 65, 34, 3, 7]

print(list(set(numbers)))

# Another way
# unique = list()
# for each in numbers:
#     if each not in unique:
#         unique.append(each)
#
# print(unique)
