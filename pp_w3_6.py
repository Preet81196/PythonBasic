"""Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

Sample data: 3, 5, 7, 23"""

val = input("enter number ")

list = val.split(",")
tuple = tuple(list)

#print(list)
#print(tuple)
print("this is list value {0} and this is tupal {1}".format(list,tuple))