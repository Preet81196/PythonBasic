"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 14/06/20
* @decription: Write a Python program to find if a given string starts with a given character using Lambda.
"""


check_me = lambda given_str, given_char: given_str.startswith(given_char)

print(check_me('Divyesh', 'S'))
print(check_me('Divyesh', 'D'))
