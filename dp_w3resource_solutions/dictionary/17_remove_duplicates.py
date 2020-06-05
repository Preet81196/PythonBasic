"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to remove duplicates from Dictionary.
"""

adict = {1: 'divyesh', 2: 'tesla', 3: 'fb', 4: 'spacex', 5: 'fb'}

curated_dict = dict()

for key, value in adict.items():
    if value not in curated_dict.values():
        curated_dict[key] = value

print(curated_dict)
