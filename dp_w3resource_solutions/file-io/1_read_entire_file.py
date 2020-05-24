"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to read an entire text file.
"""

fhand = open('data.txt')
file_content = fhand.read()
print(file_content)
