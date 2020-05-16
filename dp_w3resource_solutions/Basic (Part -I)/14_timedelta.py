"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import date

date_one = date(2020, 5, 16)
date_two = date(2020, 10, 24)

delta = date_two - date_one
print(abs(delta.days), "days")