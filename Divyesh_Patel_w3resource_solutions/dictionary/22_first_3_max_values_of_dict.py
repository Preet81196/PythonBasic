"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to find the highest 3 values in a dictionary.
"""

d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 50, 'e': 700, 'f': 45}

print('top 3 max:', sorted(d1.values(), reverse=True)[:3])
