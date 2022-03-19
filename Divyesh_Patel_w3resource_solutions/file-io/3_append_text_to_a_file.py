"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to append text to a file and display the text.
"""

fhand = open('data.txt', 'a')
data_to_append = 'This line will be added at the very end'

fhand.write(data_to_append)
fhand.close()

fhand = open('data.txt')
print(fhand.read())
