  """Write a Python program which accepts the radius of a circle from the user and compute the area. """





from math import pi

radius = float(input("Enter radius : "))
area = pi * (radius ** 2)
print('r = ', radius)
print('Area = ', area)
