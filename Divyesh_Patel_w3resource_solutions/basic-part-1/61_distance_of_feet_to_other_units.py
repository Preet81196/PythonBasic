"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 22/05/20
* @decription: Write a Python program to convert the distance (in feet) to inches, yards, and miles
"""


def feet_in_inches(f):
    return round(f*12, 3)


def feet_in_yards(f):
    return round(f/3, 3)


def feet_in_miles(f):
    return round(f/5280, 3)


user_input = input('Enter Feet: ')

try:
    user_input = float(user_input)

    print('Inches:', feet_in_inches(user_input))
    print('Yards:', feet_in_yards(user_input))
    print('Miles:', feet_in_miles(user_input))

except ValueError:
    print('invalid input, exiting')
    quit()

