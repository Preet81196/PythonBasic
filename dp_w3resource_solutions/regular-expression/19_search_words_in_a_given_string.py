"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to search some literals strings in a string. Go to the editor
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
"""

import re


patterns = ['fox', 'dog', 'horse']
statement = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    if re.search(pattern, statement) is not None:
        print(pattern, 'is present')
    else:
        print(pattern, 'not present')
