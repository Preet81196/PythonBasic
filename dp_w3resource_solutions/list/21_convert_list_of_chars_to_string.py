"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to convert a list of characters into a string.
"""

alist = ['a', 'e', 'i', 'o', 'u']
final_str = ''

for each in alist:
    final_str += each

print(final_str)

# Another method
# final_str = ''.join(alist)
