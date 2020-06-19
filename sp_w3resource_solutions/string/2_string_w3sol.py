"""   Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}"""

# Python3 code to demonstrate
# each occurrence frequency using
# collections.Counter()
from collections import Counter

# initializing string
test_str = input("enter string: ")

# using collections.Counter() to get
# count of each element in string
res = Counter(test_str)

# printing result
print("Count of all characters :\n "
      + str(res))
