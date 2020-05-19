"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 07:31:21
 * @modify date 19-05-2020 07:34:10
 * @desc Write a Python program to check whether a specified value is contained in a group of values.
"""

"""
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

given_list = [1, 5, 8, 3]

inp_check = input("Enter Number: ")

try:
    inp_check = int(inp_check)
except:
    print("invalid input, exiting")
    quit()

print(inp_check in given_list)
