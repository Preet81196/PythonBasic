"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores
"""

import testregex

pattern = '^[a-zA-Z0-9_]*$'
testregex.test(pattern, 'theowrld')
testregex.test(pattern, 'the_world')
testregex.test(pattern, 'the world')
testregex.test(pattern, '*&')
