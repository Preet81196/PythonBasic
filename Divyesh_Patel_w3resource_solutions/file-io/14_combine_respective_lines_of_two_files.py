"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/05/20
* @decription: Write a Python program to combine each line from first file with the corresponding line in second file
"""

source_content = None
with open('data.txt') as source_one_handle:
    source_one_content = list(source_one_handle)

with open('target.txt') as source_two_handle:
    source_two_content = list(source_two_handle)


max_length = max(len(source_one_content), len(source_two_content))

counter = 0
while counter < max_length:
    # if counter >= len(source_one_content):
    #     first = ''
    # else:
    #     first = source_one_content[counter]
    #
    # if counter >= len(source_two_content):
    #     second = ''
    # else:
    #     second = source_two_content[counter]

    first = source_one_content[counter] if counter < len(source_one_content) else None
    second = source_two_content[counter] if counter < len(source_two_content) else None
    print(first, second)
    counter += 1
