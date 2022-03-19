"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to get the difference between the two lists
"""

first = ['divyesh', 'patel', 'rushabh', 'dave']
second = ['preet', 'patel']

diff_res = list()

for each in first:
    if each not in second:
        diff_res.append(each)

print(diff_res)
