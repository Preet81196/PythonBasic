"""Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. """

import calendar


mon = int(input("Enter month:"))
year = int(input("Enter year:"))
print(calendar.month(year, mon))
