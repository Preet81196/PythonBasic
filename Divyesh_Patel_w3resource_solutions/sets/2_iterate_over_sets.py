"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python program to iteration over sets.
"""

aset = {'apple', 'mango', 'banana', 'grapes'}
counter = 1

for each in aset:
    print('fruit' + ' ' + str(counter) + ':', each)
    counter += 1

