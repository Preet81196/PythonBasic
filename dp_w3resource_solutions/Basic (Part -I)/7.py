"""
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
"""

filename = input("Sample filename : ")

print("Output :", filename.split(".")[-1])