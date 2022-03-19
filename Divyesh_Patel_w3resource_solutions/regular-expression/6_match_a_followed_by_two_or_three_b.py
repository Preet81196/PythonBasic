"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program that matches a string that has an a followed by two to three 'b'.
"""

import re


def check_me(statement):
    # Although as per requirement it's working fine, but I want to add a more condition
    # which says show only 2-3 occurrences of b, not more than that, so added a TODO
    pattern = 'ab{2,3}?'  # TODO: added [^b] at end, so we won't get greater than 3 b's at max, but not working
    if re.search(pattern, statement) is None:
        return 'FAIL'
    else:
        return 'PASS'


print(check_me('Divyesh Patel abbb world'))
