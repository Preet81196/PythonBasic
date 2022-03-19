"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python program to remove an item from a set if it is present in the set.
"""

aset = {'apple', 'mango', 'banana', 'grapes'}

removable_member = 'cherry'

if removable_member in aset:
    aset.discard(removable_member)
    print(aset)
else:
    print('member is not present')
