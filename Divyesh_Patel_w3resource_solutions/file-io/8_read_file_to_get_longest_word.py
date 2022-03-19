"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a python program to find the longest words.
"""


def get_longest_word_from_file(filename):
    try:
        with open(filename) as fhandle:
            longest_word_so_far = ''
            alist = list()
            for line in fhandle:
                alist += line.strip().split()
            for each in alist:
                if len(each) >= len(longest_word_so_far):
                    longest_word_so_far = each
            return longest_word_so_far
    except:
        return -1


print(get_longest_word_from_file('data.txt'))
