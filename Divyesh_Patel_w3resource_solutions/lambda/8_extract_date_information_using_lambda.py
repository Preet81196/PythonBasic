"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 15/06/20
* @decription: Write a Python program to extract year, month, date and time using Lambda.
"""

import datetime

current = datetime.datetime.now()

get_year = lambda x: x.year
get_month = lambda x: x.month
get_day = lambda x: x.day
get_time = lambda x: x.time()

print('year:', get_year(current))
print('month:', get_month(current))
print('day:', get_day(current))
print('time:', get_time(current))
