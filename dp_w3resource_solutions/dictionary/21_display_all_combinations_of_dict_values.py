"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to create and display all combinations of letters, selecting each
            letter from a different key in a dictionary.
"""

# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

# adict = {1: ['a', 'b', 'z'], 2: ['c', 'd', 'x'], 3: ['e', 'f', 'y']}
adict = {1: ['a', 'b'], 2: ['c', 'd']}

alist = list(adict.values())
# [['a', 'b', 'z'], ['c', 'd', 'x'], ['e', 'f', 'y']]

flattened_list = [each for sub_list in alist for each in sub_list]

combined_list = list()

# TODO: Pending


# def join(*parts):
#     if len(parts) == 1:
#         return parts[0]
#     other = []
#     first = parts[0]
#     last = join(*parts[1:])
#     for i in first:
#         adds = [i+j for j in last]
#         other.extend(adds)
#     return other


def occurrences_generator(elem, the_list):
    occ = []
    for each in the_list:
        occ.append(elem+each)
    return occ


for each_list in alist:
    for each_ele in each_list:
        occurrences = occurrences_generator(each_ele, flattened_list)
        for each_occurrence in occurrences:
            if each_occurrence not in combined_list:
                combined_list.append(each_occurrence)


print(combined_list)
