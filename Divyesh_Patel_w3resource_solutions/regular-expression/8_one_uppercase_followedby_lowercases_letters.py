"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to find the sequences of one upper case letter followed by lower case letters.
"""

import testregex

pattern = '[A-Z][a-z]+'
testregex.test(pattern, 'hello world')
testregex.test(pattern, 'World')
