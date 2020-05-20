"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 20-05-2020 07:40:29
 * @modify date 20-05-2020 07:40:29
 * @desc Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""

# Formula can be found here
# https://orion.math.iastate.edu/dept/links/formulas/form2.pdf

def calculate_geo_distance(point1, point2):
    if isinstance(point1, tuple) and isinstance(point2, tuple) and len(point1) == 2 and len(point2) == 2:
        return (((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)) ** (1/2)
    else:
        return "invalid data provided"

if __name__ == '__main__':
    print(calculate_geo_distance((4, 0), (6, 6)))