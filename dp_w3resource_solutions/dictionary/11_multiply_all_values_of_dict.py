"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to multiply all the items in a dictionary
"""

adict = {'divyesh': 1, 'rushabh': 2, 'raj': 3, 'patel': 4}


def mul_of_list(alist):
    mul = None
    for each in alist:
        if mul is None:
            mul = each
        else:
            mul *= each
    return mul


print('sum:', mul_of_list(adict.values()))
