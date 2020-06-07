"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 07/06/20
* @decription: Write a Python program to convert Python objects into JSON strings. Print all the values.
"""
import json

alist = [1, 2, 3, 4, 5]
adict = {1: 'spacex', 2: 'nasa'}
astr = 'earth'
anum = 12
afloat = 12.24
atup = (1, 2, 3)

print('alist json:', json.dumps(alist))
print('adict json:', json.dumps(adict))
print('astr json:', json.dumps(astr))
print('anum json:', json.dumps(anum))
print('afloat json:', json.dumps(afloat))
print('atup json:', json.dumps(atup))
