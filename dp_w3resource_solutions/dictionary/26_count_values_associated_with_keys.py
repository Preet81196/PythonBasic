"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to count the values associated with key in a dictionary.
"""

# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'},
#                 {'id': 2, 'success': False, 'name': 'Rabi'},
#                 {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True

counter = 1

data = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]

result = [counter for each_dict in data if each_dict['success'] is True]
print('result:', len(result))

# Another Way, no need to create a long list.
# counter = 0
# for each_dict in data:
#     if each_dict['success'] is True:
#         counter += 1
#
# print(counter)
