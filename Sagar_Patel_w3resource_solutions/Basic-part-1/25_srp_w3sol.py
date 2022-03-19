""" Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""

list = [1,5,8,3]
inp = int(input("enter number: "))

print(inp in list)
