"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 07/06/20
* @decription: Write a Python program to access only unique key value of a Python object.
"""

import json

json_data = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'

info = json.loads(json_data)

print(info)
