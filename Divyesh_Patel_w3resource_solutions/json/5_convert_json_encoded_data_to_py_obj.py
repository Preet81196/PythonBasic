"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 07/06/20
* @decription: Write a Python program to convert JSON encoded data into Python objects.
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
        {"firstName": "Regine", "lastName": "Agtarap"}]
}
"""

info = json.loads(data)

print(info)
