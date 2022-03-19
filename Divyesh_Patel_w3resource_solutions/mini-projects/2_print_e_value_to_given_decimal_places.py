"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 10/06/20
* @decription: Create a Python project to get the value of e to n number of decimal places.
"""

# Note: Input a number and the program will generate e to the 'nth digit

from math import e as E


x = str(E)

dotpos = x.find('.')
n = int(input('Enter position: '))

uptoplace = dotpos + 1 + n

print(x[:uptoplace])
