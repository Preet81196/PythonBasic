"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 09:49:55
 * @modify date 19-05-2020 09:49:55
 * @desc Write a Python program to add two objects if both objects are an integer type.
"""

def conditional_obj_addition(obja, objb):
    if type(obja) is int and type(objb) is int: return obja + objb
    else: return "objs are of different type"

print(conditional_obj_addition(1, '2'))
