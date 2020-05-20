"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 20/05/20
* @decription: Write a python program to get the path and name of the file that is currently executing.
"""

import os

file_path = __file__  # another way, os.path.realpath(__file__)

filename = file_path.split('/')[-1]
current_dir_ind = file_path.find(filename)

print('filename:', filename)
print('current dir:', file_path[:current_dir_ind-1])  # another way, os.getcwd()


