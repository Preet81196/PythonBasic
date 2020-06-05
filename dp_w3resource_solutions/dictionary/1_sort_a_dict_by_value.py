"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python script to sort (ascending and descending) a dictionary by value.
"""

adict = {'divyesh': 1200, 'preet': 3400, 'sagar': 4500, 'hardik': 740}

adict_asc = dict(sorted(adict.items(), key=lambda x: x[1]))
adict_desc = dict(sorted(adict.items(), key=lambda x: x[1], reverse=True))

print('ASC:', adict_asc)
print('DESC:', adict_desc)
