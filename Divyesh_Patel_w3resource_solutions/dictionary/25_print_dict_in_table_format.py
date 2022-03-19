"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to print a dictionary in table format.
"""

my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

"""
C1 C2 C3
1  5  9
2  6  10
3  7  11w
"""

print("  ".join(my_dict.keys()))

for v1, v2, v3 in zip(*list(my_dict.values())):
    print(str(v1) + '   ' + str(v2) + '   ' + str(v3))
