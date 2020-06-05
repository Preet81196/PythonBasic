"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python script to concatenate following dictionaries to create a new one.
"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

aggregated_dict = dict([each_ele for each in [dic1.items(), dic2.items(), dic3.items()] for each_ele in each])
print(aggregated_dict)

# Another way maybe
# aggregated_dict = dict()
#
# for key, value in dic1.items():
#     aggregated_dict[key] = value
#
# for key, value in dic2.items():
#     aggregated_dict[key] = value
#
# for key, value in dic3.items():
#     aggregated_dict[key] = value
#
# print(aggregated_dict)


# Another more way maybe
# aggregated_dict = dict()
# alist = list()
#
# alist.extend(dic1.items())
# alist.extend(dic2.items())
# alist.extend(dic3.items())
#
# for key, value in alist:
#     aggregated_dict[key] = value
#
# print(aggregated_dict)
