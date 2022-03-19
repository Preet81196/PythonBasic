"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a python program to check whether two lists are circularly identical.
"""

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

"""
[10, 10, 0, 0, 10]
[10, 10, 10, 0, 0] => matches with list2 [10, 10, 10, 0, 0]
"""


def check_circularly_identical(ll_1, ll_2):
    is_similar = False
    if not isinstance(ll_1, list) or not isinstance(ll_2, list) or len(ll_1) != len(ll_2):
        return is_similar

    iterator = 0
    while iterator < len(ll_1):
        ll_1.insert(0, ll_1.pop())
        if ll_1 == ll_2:
            is_similar = True
            break
        iterator += 1
    return is_similar


print(check_circularly_identical(list1, list2))
