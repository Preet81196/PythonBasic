"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python program to use of frozensets.
"""

setx = frozenset([1, 2, 3])
sety = frozenset([3, 4, 5])

print('setx is sub set of y:', setx.issubset(sety))
print('setx union sety', setx.union(sety))

setx.add('5')  # This will Produce error and execution will be stopped, as frozensets can't be changed (immutable)

print('setx:', setx)
