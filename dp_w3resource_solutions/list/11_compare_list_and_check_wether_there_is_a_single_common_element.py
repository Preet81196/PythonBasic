"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python function that takes two lists and returns True if they have at least one common member.
"""


def compare(local_list_1, local_list_2):
    for each in local_list_1:
        if each in local_list_2:
            return True
    return False


alist = ['divyesh', 'patel', 'prit', 'sagar', 'rajalaxmi', 'subramaniam']
friends = ['hardik', 'rushabh', 'karan', 'urvish', 'sagar', 'preet']

print(compare(alist, friends))
