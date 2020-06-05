"""Write a Python program to accept a filename from the user and print the extension of that"""




file = input("Enter file name:").split(".")
print("extension:" + file[-1])
