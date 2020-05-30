"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math
PI = math.pi

radius = input("r = ")

try:
    radius = float(radius)
    area = PI * (radius ** 2)
    print("Area =", area)    

except ValueError:
    print("Please Enter a valid value")

except:
    print("something went wrong")
