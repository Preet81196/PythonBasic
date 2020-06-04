"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python program to remove an empty tuple(s) from a list of tuples.
"""

# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

alist = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

new_list = [each for each in alist if len(each) is not 0]
print(new_list)
