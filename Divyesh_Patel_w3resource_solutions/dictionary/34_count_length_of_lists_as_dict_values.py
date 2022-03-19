"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 06/06/20
* @decription: Write a Python program to count number of items in a dictionary value that is a list.
"""

adict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

count = 0
for key in adict:
    count += len(adict[key])

print(count)
