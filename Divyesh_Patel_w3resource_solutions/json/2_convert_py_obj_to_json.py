"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 07/06/20
* @decription: Write a Python program to convert Python object to JSON data.
"""

import json

adict = {
    'name': 'Divyesh',
    'std': 12,
    'school': 'Delhi Public School'
}

data = json.dumps(adict)

print(data)
