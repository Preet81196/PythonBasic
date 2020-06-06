"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 06/06/20
* @decription: Write a Python program to create a dictionary of keys x, y, and z where each key has as
            value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key
            from the dictionary.
"""

conditions = {'x': [11, 20], 'y': [21, 30], 'z': [31, 40]}

adict = dict()

for condition_key, ranges in conditions.items():
    adict[condition_key] = list(range(ranges[0], ranges[1]+1))

print(adict)

for each in adict.values():
    print(each[4])
