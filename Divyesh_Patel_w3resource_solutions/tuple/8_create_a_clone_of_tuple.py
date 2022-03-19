"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 03/06/20
* @decription: Write a Python program to create the colon of a tuple.
"""

tup = (1, 2, 3, [61, 62])


# def deep_copy(a_tuple):
#     # a_tuple = (1, 2, 3)
#     returnable_tup = ()
#     for each in a_tuple:
#         returnable_tup = returnable_tup, each
#     return returnable_tup

# TODO, INCOMPLETE

new_tup = *tup,  # from copy import deepcopy => deepcopy(tup)

new_tup[3].append(67)

print('id of tup:', id(tup))
print('tup:', tup)

print()
print('id of new_tup:', id(new_tup))
print('new_tup:', new_tup)
