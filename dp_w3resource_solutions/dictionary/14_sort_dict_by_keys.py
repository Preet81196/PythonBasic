"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to sort a dictionary by key.
"""

adict = {3: 'sagar', 2: 'preet', 1: 'hardik', 4: 'divyesh'}

adict = dict(sorted(adict.items(), key=lambda x: x[0]))

print(adict)
