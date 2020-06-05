"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to print all unique values in a dictionary.
"""

# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S001', 'S009'}

alist = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}]

alist_new = set([value for each_dict in alist for key, value in each_dict.items()])

print(alist_new)
