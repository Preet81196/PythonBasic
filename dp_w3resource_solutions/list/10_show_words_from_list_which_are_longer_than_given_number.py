"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to find the list of words that are longer than n from a given list of words.
"""


def get_big_words_from_list(local_list, n):
    if not isinstance(local_list, list) or not isinstance(n, int):
        return -1
    return [each for each in local_list if len(each) > n]


alist = ['divyesh', 'patel', 'prit', 'sagar', 'rajalaxmi', 'subramaniam']
print(get_big_words_from_list(alist, 7))
