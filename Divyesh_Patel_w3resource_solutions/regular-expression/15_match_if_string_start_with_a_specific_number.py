"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program where a string will start with a specific number.
"""

import testregex

pattern = '^4'  # Assumed that specific number as 4
testregex.test(pattern, 'hello world')
testregex.test(pattern, '490')
