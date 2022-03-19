"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to create a file where all letters of English alphabet are listed
        by specified number of letters on each line.
"""
import string
alphas = list(string.ascii_uppercase)
alphas_with_nl = ''
line_length = 2
alphas_length = len(alphas) + int(len(alphas)/line_length)
# Added number of length of alphas after addition of newlines so loop can go to future length

with open('alphamoghuls.txt', 'w') as handle:
    for each in range(line_length, alphas_length, line_length+1):
        alphas.insert(each, '\n')  # adds newline char to the desired point
    for each in alphas:
        alphas_with_nl += each
    handle.write(alphas_with_nl)
