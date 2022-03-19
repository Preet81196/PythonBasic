"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 03/06/20
* @decription: Write a Python program to replace last value of tuples in a list.
"""

# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

alist = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = list()

for each in alist:
    tup = *each[:-1], 100
    new_list.append(tup)

print(new_list)
