"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 06/06/20
* @decription: Write a Python program to replace dictionary values with their average.
"""

# Sample data:  [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#                {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#                {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]

# Output: [{'subject': 'math', 'id': 1, 'V+VI': 76.0},
#           {'subject': 'math', 'id': 2, 'V+VI': 73.5},
#           {'subject': 'math', 'id': 3, 'V+VI': 80.5}]

data = [{'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
        {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
        {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}]

alist = list()

for each in data:
    new_dict = dict()
    new_dict['id'] = each['id']
    new_dict['subject'] = each['subject']
    new_dict['V+VI'] = (each['V'] + each['VI']) / 2
    alist.append(new_dict)

print(alist)
