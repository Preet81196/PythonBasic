"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to replace whitespaces with an underscore and vice versa
"""

import re

sp_statement = 'currently spaced divyesh patel intro'
un_statement = 'this_all_string_is_written_with_the_help_of_underscore'

sp_pattern = '\s'
un_pattern = '_'

csp_pattern = re.compile(sp_pattern)
underscored_str = csp_pattern.sub('_', sp_statement)
print(underscored_str)

cun_pattern = re.compile(un_pattern)
spaced_str = cun_pattern.sub(' ', un_statement)
print(spaced_str)
