"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/09/20
* @decription: Write a Python program to read a given CSV file having tab delimiter.
"""

import csv

with open('coutries.csv', newline='') as csvfile:
    coutries = csv.reader(csvfile, delimiter='\t')
    for each in coutries:
        print(each)
