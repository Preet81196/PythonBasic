"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to combine two dictionary adding values for common keys.
"""

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

adict = d1.copy()

for key, value in d2.items():
    adict[key] = adict.get(key, 0) + value

print(adict)
