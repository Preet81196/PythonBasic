"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 06/06/20
* @decription: Write a Python program to store a given dictionary in a json file.
"""

import json

data = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'},
                     {'firstName': 'Mervin', 'lastName': 'Friedland'},
                     {'firstName': 'Aron ', 'lastName': 'Wilkins'}],
        'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'},
                     {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

data_json = json.dumps(data)

with open('39_school_data.json', 'w') as handle:
    handle.write(data_json)

