"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 20/05/20
* @decription: Write a Python program to parse a string to Float or Integer.
"""

given_str = "238.4589"

try:
    print(float(given_str))
    print(int(float(given_str)))
except ValueError:
    print('Can\'t convert to int or float')
