"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 07/06/20
* @decription: Write a Python program to convert Python dictionary object (sort by key) to JSON data.
        Print the object members with indent level 4.
"""

import json

adict = {
    'name': 'Divyesh',
    'std': 12,
    'school': 'Delhi Public School'
}

j_data = json.dumps(adict, sort_keys=True, indent=4)

print(j_data)
