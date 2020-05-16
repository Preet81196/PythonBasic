"""
Write a Python program to display the current date and time.
"""
from datetime import datetime

today = datetime.today()

today_in_str = str(today)

dot_index = today_in_str.find('.')

print(today_in_str[0:dot_index])
print("bye")