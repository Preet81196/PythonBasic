"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to find the second smallest number in a list.
"""

l1 = [1, 2, -8, -2, 0, -2]
l2 = [1, 1, 0, 0, 2, -2, -2]
l3 = [1, 1, 1, 0, 0, 0, 2, -2, -2]
l4 = [2, 2]
l5 = [2]


# TODO: Find second smallest manually
def find_second_smallest(ll):
    ll = list(set(ll))
    ll.sort()

    if len(ll) <= 1:
        return None
    return ll[1]


print(find_second_smallest(l1))
print(find_second_smallest(l2))
print(find_second_smallest(l3))
print(find_second_smallest(l4))
print(find_second_smallest(l5))
