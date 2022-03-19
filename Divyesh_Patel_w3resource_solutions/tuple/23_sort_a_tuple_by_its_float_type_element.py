"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 04/06/20
* @decription: Write a Python program to sort a tuple by its float element.
"""

# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

alist = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

new_list = sorted(alist, key=lambda x: float(x[1]), reverse=True)

print(new_list)
