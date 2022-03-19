"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to convert a list into a nested dictionary of keys.
"""

# Sample data: [1, 2, 3, 4]
# Output: {1: {2: {3: {4: {}}}}}

alist = [1, 2, 3, 4]
temp = {}
new_dict = {}

for each in sorted(alist, reverse=True):
    new_dict.clear()
    new_dict[each] = temp
    temp = new_dict.copy()

print(new_dict)
