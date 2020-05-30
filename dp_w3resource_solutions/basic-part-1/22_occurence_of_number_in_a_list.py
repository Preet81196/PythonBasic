"""
Write a Python program to count the number 4 in a given list.
"""

given_list = [1, 2, 4, 6, 4, 2, 8, 4, 2, 8, 3, 4, 4]

print("Count(using built-in function):", given_list.count(4))

# Alternate way
count = 0
for each in given_list:
    if each == 4: count += 1

print("Count(using a loop):", count)