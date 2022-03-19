"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription:  the occurrence and position of the substrings within a string
"""

# Related Article can be found here: https://docs.python.org/3.7/howto/regex.html

import re

text = 'hello world this is divyesh patel, how beautiful this world is.'
pattern = 'world'
cpattern = re.compile(pattern)
thelist = cpattern.finditer(text)
for each in thelist:
    print(each.group(), each.span())


