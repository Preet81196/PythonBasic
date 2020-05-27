"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to generate and print a list except for the first 5 elements,
            where the values are square of numbers between 1 and 30 (both included).
"""

origin = list(range(1, 31))
print('origin:', origin)
first_number_of_elements = 5
destination = [each ** 2 for each in origin]


after_first_five = destination[first_number_of_elements:]

# 30-10 (10, because of the new list)
before_last_five = after_first_five[:len(destination) - 2*first_number_of_elements]
print('output:', before_last_five)
