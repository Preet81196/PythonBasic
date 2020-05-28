"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
"""

# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

alist = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
removable_ind = [0, 4, 5]
ind_iterator_to_change = 0  # if we remove 5th element in loop which comes 3rd in iteration
# There will be no element at that time, so we are updating the varibale according to current situation of list
# As .pop() will shift elements to left after each call.

for each_ind in removable_ind:
    alist.pop(each_ind - ind_iterator_to_change)
    ind_iterator_to_change += 1

print(alist)
