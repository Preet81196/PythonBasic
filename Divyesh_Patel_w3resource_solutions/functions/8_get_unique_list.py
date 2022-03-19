"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""


def get_uniq(alist):
    # return list(set(alist))  # Just another way, TODO: profile it both the methods
    uniq_list = list()
    for each in alist:
        if each not in uniq_list:
            uniq_list.append(each)
    return uniq_list


print(get_uniq([1, 1, 2, 3, 4, 4, 5]))
