"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program that matches a word containing 'z', not at the start or end of the word.
"""

import testregex

pattern = '^[^z].+z.+[^z]$'
testregex.test(pattern, 'hellowdiv')
testregex.test(pattern, 'hellowzdiv')
testregex.test(pattern, 'zeebra')
testregex.test(pattern, 'teebraz')
