"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: This is a Common Utility file for re module to test programs
"""

import re


def test(pattern, statement):
    if re.search(pattern, statement) is None:
        print(pattern, "=>", statement + ":", 'FAIL')
    else:
        print(pattern, "=>" , statement + ":", 'PASS')
