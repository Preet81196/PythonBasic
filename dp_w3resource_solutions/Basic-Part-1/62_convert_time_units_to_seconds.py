"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 22/05/20
* @decription: Write a Python program to convert all units of time into seconds.
"""

SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

try:
    inp_days = int(input('Days: '))
    inp_hours = int(input('Hours: '))
    inp_minutes = int(input('Minutes: '))
    inp_seconds = int(input('Seconds: '))

    res = (inp_days * SECONDS_IN_DAY) + (inp_hours * SECONDS_IN_HOUR) + (inp_minutes * SECONDS_IN_MINUTE) + inp_seconds
    print('Seconds:', res)
except ValueError:
    print('invalid inputs, only int values are allowed, exiting')
    quit()
