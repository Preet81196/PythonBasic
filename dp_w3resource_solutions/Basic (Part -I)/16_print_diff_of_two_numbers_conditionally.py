"""
Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference.
"""

given_number = input("Enter Number: ")

try:
    given_number = int(given_number)
    if given_number > 17:
        print("Answer: ", (given_number - 17) * 2)
    else:
        print("Answer: ", 17 - given_number)
except:
    print("Invalid Input")