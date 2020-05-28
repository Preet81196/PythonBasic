"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 28/05/20
* @decription: Write a Python program to count the number of elements in a list within a specified range.
"""


# Have build this program differently with what w3resource has build
# TODO: meet the requirements of the original problem

def count_range_elements_in_list(ll, limit1, limit2):
    given_range = range(limit1, limit2+1)
    no_of_elements_in_list = 0
    for each in ll:
        if each in given_range:
            no_of_elements_in_list += 1
    return no_of_elements_in_list


numbers = [10, 20, 30, 40, 40, 40, 70, 80, 99]

print((count_range_elements_in_list(numbers, 10, 40)))  # both ranges are included
