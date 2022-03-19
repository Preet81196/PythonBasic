"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program that matches a word at the beginning of a string
"""

import testregex

pattern = '^[^\s]'
testregex.test(pattern, 'Hello Patel')
testregex.test(pattern, ' Hello')
