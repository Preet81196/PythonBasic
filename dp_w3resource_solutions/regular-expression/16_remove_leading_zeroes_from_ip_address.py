"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program to remove leading zeros from an IP address.
"""

import re


pattern = '\.[0]*'
ip = '127.01.01.100'
sub_result = re.sub(pattern, '.', ip)
print(sub_result)
