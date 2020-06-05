"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 05/06/20
* @decription: Write a Python program to create a dictionary from a string.
"""

# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

sample = 'w3resource'
word_counts = dict()

for each in sample:
    word_counts[each] = word_counts.get(each, 0) + 1

print(word_counts)
