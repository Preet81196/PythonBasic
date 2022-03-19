""" Write a Python program to get a string which is n (non-negative integer) copies of a given string """

text = input("Enter string:")
copy = int(input("Number of copies:"))

for i in range(copy):
    print(text)
