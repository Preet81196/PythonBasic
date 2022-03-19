"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 09/06/20
* @decription: Write a Python program to count the number of characters (character frequency) in a string.
"""

statement = 'Hello world This is Elon Musk from SpaceX'
frequency = dict()

for each in statement:
    frequency[each] = frequency.get(each, 0) + 1

print(frequency)
