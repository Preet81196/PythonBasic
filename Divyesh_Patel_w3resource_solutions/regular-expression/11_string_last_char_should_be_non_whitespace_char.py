"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program that matches a word at the end of string, with optional punctuation.
"""

import testregex

pattern = '[^\s]$'
testregex.test(pattern, 'hello ')
testregex.test(pattern, 'hello.')