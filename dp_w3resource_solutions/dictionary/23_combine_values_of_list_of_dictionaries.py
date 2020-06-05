"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to combine values in python list of dictionaries.
"""

# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

alist = [{'item': 'item1', 'amount': 400},
         {'item': 'item2', 'amount': 300},
         {'item': 'item1', 'amount': 750}]

combined_dict = dict()

for each_dict in alist:
    combined_dict[each_dict['item']] = combined_dict.get(each_dict['item'], 0) + each_dict['amount']

print(combined_dict)
