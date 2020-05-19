"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 08:20:24
 * @modify date 19-05-2020 08:20:24
 * @desc Write a Python program that will accept the base and height of a triangle and compute the area
"""

try:
    inp_base = float(input('Base: '))
    inp_height = float(input('Height: '))
except:
    print('invalid input, exiting')
    quit()

area_of_triangle = (inp_base * inp_height) / 2
print('Area', area_of_triangle)