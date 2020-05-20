"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 20-05-2020 08:00:47
 * @modify date 20-05-2020 08:00:47
 * @desc Write a Python program to check whether a file exists.
"""

file_name = input('Enter filename: ')

try:
    open(file_name)
    print("Success")
except FileNotFoundError:
    print('no file found')