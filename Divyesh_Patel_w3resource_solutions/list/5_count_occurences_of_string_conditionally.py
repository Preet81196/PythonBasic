"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to count the number of strings where the string length is 2 or more
        and the first and last character are same from a given list of strings.
"""

alist = ['abc', 'xyz', 'aba', '1221']

counts = 0
for each in alist:
    if len(each) >= 2 and each[0] == each[len(each)-1]:
        counts += 1

print(counts)
