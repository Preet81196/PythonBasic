"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 26/05/20
* @decription: Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
"""
import string
alphas = string.ascii_uppercase

for each in alphas:
    filename = each + '.txt'
    with open(filename, 'w') as handle:
        handle.write('Hello World')
