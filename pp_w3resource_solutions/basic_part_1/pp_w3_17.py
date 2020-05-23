"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
num = int(input('enter number :'))
print((1000-num) <= 100) or ((2000-num)<=100)
