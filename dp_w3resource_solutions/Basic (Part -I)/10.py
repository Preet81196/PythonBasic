"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
Sample value of n is 5
Expected Result : 615
"""

given_number = input("Sample value of n is ")

try: 
    given_number = int(given_number)
    print("Expected Result :", given_number + (11 * given_number) + (111 * given_number))
except:
    print('not a number provided')