"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 28/05/20
* @decription: Write a Python program to get the frequency of the elements in a list.
"""

numbers = [12, 3, 4, 6, 12, 56, 2, 6, 34, 20, 10, 38, 59, 95, 9, 96, 64, 65, 34, 3, 7]
unique = set(numbers)

for each in unique:
    print(each, numbers.count(each))
