"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""
import calendar

try:
    inp_year = int(input("Input the year : "))
    inp_month = int(input("Input the month : "))
    text_cal = calendar.TextCalendar()
    print(text_cal.formatmonth(inp_year, inp_month, w=0, l=0))
except:
    print("Exiting: Enter valid data")

