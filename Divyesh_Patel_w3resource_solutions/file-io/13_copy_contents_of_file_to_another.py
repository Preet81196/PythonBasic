"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to copy the contents of a file to another file
"""

source_file = 'origin.txt'
destination_file = 'destination.txt'

with open(source_file) as source_handle:
    source_content = source_handle.read()

with open(destination_file, 'w') as dest_handle:
    dest_handle.write(source_content)
