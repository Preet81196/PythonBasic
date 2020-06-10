"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 10/06/20
* @decription: Create a Python project to get the value of Pi to n number of decimal places.
"""

# Note: Input a number and the program will generate PI to the nth digit

from math import pi as PI


x = str(PI)

dotpos = x.find('.')
n = int(input('Enter position: '))

uptoplace = dotpos + 1 + n

print(x[:uptoplace])
