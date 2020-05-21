"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

import calendar
y = int(input("enter year: "))
m = int(input("enter month: "))

print(calendar.month(y,m))