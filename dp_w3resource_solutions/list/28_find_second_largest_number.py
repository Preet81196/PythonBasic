"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 28/05/20
* @decription: Write a Python program to find the second largest number in a list.
"""

numbers = [12, 3, 4, 6, 12, 56, 2, 6, 34, 20, 10, 38, 59, 95, 9, 96, 64, 65, 34, 3, 7]


def get_second_largest(ll):
    ll = set(ll)
    ll = sorted(ll, reverse=True)

    if len(ll) == 1:
        return ll[0]
    return ll[1]


print(get_second_largest(numbers))
