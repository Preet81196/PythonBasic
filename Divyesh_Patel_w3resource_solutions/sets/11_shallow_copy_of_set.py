"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python program to create a shallow copy of sets.
"""

setx = {1, 2, 3}
sety = setx.copy()

print('adding 555 to sety')
sety.add(555)

print('setx:', setx)
print('sety:', sety)
