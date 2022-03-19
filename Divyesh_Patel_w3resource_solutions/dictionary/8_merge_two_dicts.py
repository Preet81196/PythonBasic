"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python script to merge two Python dictionaries.
"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}

merged_dict = dic1.copy()
merged_dict.update(dic2)
print(merged_dict)


# Another Way
# merged_dict = dict([each_ele for each in [dic1.items(), dic2.items()] for each_ele in each])
# print(merged_dict)
