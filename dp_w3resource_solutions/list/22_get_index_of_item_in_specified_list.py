"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to find the index of an item in a specified list.
"""


def get_ind_of_list_element(local_list, ele):
    if ele not in local_list:
        return 'not present'
    return local_list.index(ele)


alist = ['divyesh', 'patel', 'prit', 'sagar', 'rajalaxmi', 'subramaniam']
print(get_ind_of_list_element(alist, 'sagar'))
print(get_ind_of_list_element(alist, 'hardik'))
