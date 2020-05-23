"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python program that accepts a hyphen-separated sequence of words as input and prints
            the words in a hyphen-separated sequence after sorting them alphabetically.
"""


def sort_hyphen_separated_sequence(sequence):
    alist = sequence.split('-')
    if not isinstance(sequence, str) or len(sequence) == 0:
        return None
    hy_separated = None
    alist.sort()
    for each in alist:
        if hy_separated is None:
            hy_separated = each
        else:
            hy_separated = hy_separated + '-' + each
    return hy_separated


print(sort_hyphen_separated_sequence('green-red-yellow-black-white'))
print(sort_hyphen_separated_sequence('patel-divyesh'))
