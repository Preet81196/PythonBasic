"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/09/20
* @decription: Write a Python program to read each row from a given csv file and print a list of strings.
"""

import csv

with open('patients.csv', newline='') as csvfile:
    patients = csv.reader(csvfile)
    for each_row in patients:
        print(each_row)
