"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 03/06/20
* @decription: Write a Python program to remove an item from a tuple
"""

tup = 1, 2, 3, 4, [1, 2], 5, 6, 7, 8, 9, 10

element_to_remove = 3

try:
    element_index = tup.index(element_to_remove)
except:
    print('element not found')
    quit()

new_tup = *tup[:element_index], *tup[element_index+1:]

print(new_tup)
