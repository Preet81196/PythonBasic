"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to remove duplicates from a list.
"""

alist = [1, 1, 2, 3, 3, 5, 6, 6, 5, 3, 4, 5, 5, 2, 1, 5, 8]
perfect_list = list()

for each in alist:
    if each not in perfect_list:
        perfect_list.append(each)

print(sorted(perfect_list))

"""
# easy method
list1 = [1,2,2,3,4,5,5,6,2,3,1,7,8,8,6]

print(set(list1))"""


