"""
Write a Python program to display the current date and time.
"""

from datetime import datetime

today = datetime.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)

hour_in_24 = str(today.hour)
minute = str(today.minute)
second = str(today.second)

print(year + "-" + month + "-" + day + " " + hour_in_24 + ":" + minute + ":" + second)