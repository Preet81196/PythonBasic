"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 27/05/20
* @decription: Write a Python program to append a list to the second list.
"""

first = ['divyesh', 'patel', 'rushabh', 'dave']
second = ['preet', 'patel']

first.extend(second)
print(first)

# Other ways
# list1 + list2
# list1[len(list1):] = list2
