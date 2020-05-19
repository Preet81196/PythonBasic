"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 19-05-2020 07:47:36
 * @modify date 19-05-2020 07:47:36
 * @desc Write a Python program to concatenate all elements in a list into a string and return it.
"""

"""
[1, 5, 12, 2] => '15122'
"""

def concatenate_us(alist):
    concatenated_str = ''
    for each in alist:
        concatenated_str += str(each)
    
    return concatenated_str


if __name__ == '__main__':
    print(concatenate_us([1, 5, 12, 2]))
