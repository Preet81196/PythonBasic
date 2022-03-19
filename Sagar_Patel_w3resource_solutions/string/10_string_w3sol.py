""" Write a Python program to change a given string to a new string where the first and last chars have been exchanged"""

txt1 = input("Enter string 1:")

str1 = txt1[-1:] + txt1[1:-1] + txt1[:1]

print(str1)