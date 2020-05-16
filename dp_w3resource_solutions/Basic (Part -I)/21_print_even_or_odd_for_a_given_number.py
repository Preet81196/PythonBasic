"""
Write a Python program to find whether a given number (accept from the user) is even or odd, 
print out an appropriate message to the user.
"""

try:
    given_number = int(input("Enter a number: "))
    if given_number % 2 == 0:
        print("Even")
    else:
        print("Odd")

except:
    print("Invalid, Exiting...")