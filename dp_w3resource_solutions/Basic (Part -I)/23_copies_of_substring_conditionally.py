"""
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2
"""

given_str = "Divyesh Patel"
number_of_copies = 4

if len(given_str) < 2:
    print(number_of_copies * given_str)
else:
    print(number_of_copies * given_str[:2])
