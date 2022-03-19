"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 03/06/20
* @decription: Write a Python program to convert a tuple to a string.
"""

friends_tup = 'divyesh', 'preet', 'sagar', 'fantyo'
final_str = ''

for each in friends_tup:
    final_str += ' ' + each

print(final_str)
