"""  Write a Python program to calculate the length of a string."""

input = input("enter text")
count = 0
for char in input:
    count +=1
    print(count,end="")