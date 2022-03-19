"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to extract characters from various text files and puts them into a list.
"""

with open('data.txt') as dhandle, open('target.txt') as thandle:
    dhandle_data = dhandle.read()
    thandle_data = thandle.read()

with open('combination.txt', 'w') as chandle:
    final_str = dhandle_data + '\n' + thandle_data
    chandle.write(final_str)
    print('written, done')


