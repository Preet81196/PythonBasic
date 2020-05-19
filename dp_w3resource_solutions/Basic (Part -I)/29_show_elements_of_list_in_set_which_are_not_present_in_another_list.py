"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 08:10:09
 * @modify date 19-05-2020 08:10:09
 * @desc Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2
"""

"""
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
resultant_set = set()

for each in color_list_1:
    if each not in color_list_2: resultant_set.add(each)

print(resultant_set)
