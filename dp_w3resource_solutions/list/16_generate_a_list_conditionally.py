"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to generate and print a list of first and last 5 elements
            where the values are square of numbers between 1 and 30 (both included)
"""

origin = list(range(1, 31))
print('origin:', origin)
first_number_of_elements = 5
destination = [each ** 2 for each in origin
               if origin.index(each) < first_number_of_elements or
               origin.index(each) >= len(origin) - first_number_of_elements]

print('destination:', destination)
