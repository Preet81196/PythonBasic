"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to sort a list alphabetically in a dictionary.
"""

# Sample data: {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# Output: {'n1': [1, 2, 3], 'n3': [2, 3, 4], 'n2': [1, 2, 5]}

adict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_adict = dict()

for each in sorted(adict.keys()):
    sorted_adict[each] = sorted(adict[each])

print(sorted_adict)
