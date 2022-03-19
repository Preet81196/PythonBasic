"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
"""

import testregex

pattern = '^a.b$'
testregex.test(pattern, 'divlo')
testregex.test(pattern, 'divlo adb')
testregex.test(pattern, 'adbd')
testregex.test(pattern, 'aKb')
testregex.test(pattern, 'a b')
