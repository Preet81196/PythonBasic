"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 06/06/20
* @decription: Write a Python program to match key values in two dictionaries.
"""

# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

dict_one = {'key1': 1, 'key2': 3, 'key3': 2}
dict_two = {'key1': 1, 'key2': 2}

matches = dict()

for key in dict_one:
    if key in dict_two.keys() and dict_one[key] == dict_two[key]:
        matches[key] = dict_one[key]

print(matches)
