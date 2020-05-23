"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to check for a number at the end of a string
"""

import testregex

pattern = '.*[0-9]$'
testregex.test(pattern, 'divlo')
testregex.test(pattern, 'patel4')
testregex.test(pattern, '4')
testregex.test(pattern, '')
