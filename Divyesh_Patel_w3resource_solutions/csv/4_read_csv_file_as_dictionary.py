"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/09/20
* @decription: Write a Python program to read a given CSV file as a dictionary.
"""

import csv

with open('departments.csv', newline='') as csvfile:
    csv_dict_reader = csv.DictReader(csvfile)
    for each in csv_dict_reader:
        print(each)
