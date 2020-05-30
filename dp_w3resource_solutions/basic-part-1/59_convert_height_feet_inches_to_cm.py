"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 21/05/20
* @decription: Write a Python program to convert height (in feet and inches) to centimeters
"""

print("***Convert Height (feet, inches) to Centimeters*** Leave Blank if values are not present")

feets = input('Feets: ')
inches = input('Inches: ')

if feets == '':
    feets = 0
if inches == '':
    inches = 0

try:
    feets = float(feets)
    inches = float(inches)
except ValueError:
    print('invalid input, setting 0 instead')
    if not isinstance(feets, float):
        feets = 0
    if not isinstance(inches, float):
        inches = 0

print('Centimeters:', (feets * 30.48) + (inches * 2.54))
