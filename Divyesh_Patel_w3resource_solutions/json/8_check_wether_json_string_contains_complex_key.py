"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 07/06/20
* @decription: Write a Python program to check whether a JSON string contains complex object or not.
"""

import json

data = """
{
    "students": 
        [{"firstName": "Nikki", "lastName": "Roysden"}, 
        {"firstName": "Mervin", "lastName": "Friedland"}, 
        {"firstName": "Aron ", "lastName": "Wilkins"}], 
    "teachers": 
        [{"firstName": "Amberly", "lastName": "Calico"}, 
        {"firstName": "Regine", "lastName": "Agtarap"}],
    "1+2j": {
        "new_key": True
    }
}
"""

# TODO: Pending

info = json.loads(data)

if '1+2j' in info:
    print('yes')
else:
    print('not exists')
