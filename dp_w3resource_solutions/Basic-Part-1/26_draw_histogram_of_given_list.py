"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 07:35:11
 * @modify date 19-05-2020 07:35:11
 * @desc Write a Python program to create a histogram from a given list of integers
"""

def draw_histogram(alist):
    for each in alist:
        print(each * '*')

if __name__ == '__main__':
    draw_histogram([2, 5, 1, 6])