"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 21/05/20
* @decription: Write a Python program to get height and width of the console window
"""

import subprocess

# TODO: Running via Play button throws error: stty: stdin isn't a terminal, need to check this
# Otherwise, program is running via python filename.py

output = subprocess.run(["stty", "size"], capture_output=True)
print(output)
height, width = output.stdout.decode().split(' ')
print('height:', height)
print('width:', width, end='')
