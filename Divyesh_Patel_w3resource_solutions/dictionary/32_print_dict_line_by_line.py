"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to print a dictionary line by line.
"""

# Sample data: {'Aex':{'class':'V', 'roll_id':2}, 'Pooja':{'class':'V', 'roll_id':3}}
# Aex
# class : V
# roll_id : 2
# Pooja
# class : V
# roll_id : 3


adict = {'Aex': {'class': 'V', 'roll_id': 2}, 'Pooja': {'class': 'V', 'roll_id': 3}}

for each_key in adict:
    print(each_key)
    for sub_key in adict[each_key]:
        print(sub_key, ":", adict[each_key][sub_key])
