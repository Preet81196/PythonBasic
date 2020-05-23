"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 20/05/20
* @decription: Write a Python program to list all files in a directory in Python.
"""

import os

target_dir = '/Users/divyeshpatel/'
dir_items = os.listdir(target_dir)
final_list = [each for each in dir_items if not each.startswith('.')]
final_list.sort()

for each in final_list:
    print(each)
