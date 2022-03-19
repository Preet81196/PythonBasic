"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 14/06/20
* @decription: Write a Python program to sort a list of dictionaries using Lambda.
"""

alist = [{'name': 'Divyesh', 'roll_number': 4},
         {'name': 'Preet', 'roll_number': 2},
         {'name': 'Sagar', 'roll_number': 1},
         {'name': 'Rushabh', 'roll_number': 3}]
print(alist)

alist.sort(key=lambda each_dict: each_dict['roll_number'])
print(alist)
