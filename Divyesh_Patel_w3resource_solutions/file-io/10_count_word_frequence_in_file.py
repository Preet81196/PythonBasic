"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to count the frequency of words in a file.
"""

words_frequency = dict()
with open('data.txt') as handle:
    for line in handle:
        for each_word in line.strip().split():
            words_frequency[each_word] = words_frequency.get(each_word, 0) + 1

for key, value in words_frequency.items():
    print(key, value)
