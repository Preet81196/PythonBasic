"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to search a literals string in a string and also find the location within
            the original string where the pattern occurs.
"""

import re


text = 'the quick brown fox jumps over the lazy dog.'
pattern = 'fox'

match = re.search(pattern, text)
if match is not None:
    start = match.start()
    end = match.end()

print(text[start:end])
