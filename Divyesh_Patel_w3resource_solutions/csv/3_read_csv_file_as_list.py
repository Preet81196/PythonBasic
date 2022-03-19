"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/09/20
* @decription: Write a Python program to read a given CSV file as a list.
"""

import csv

with open('coutries.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    print(data)

