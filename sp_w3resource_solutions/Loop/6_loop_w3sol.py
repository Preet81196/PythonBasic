""" Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in numbers:
    if i % 2:
        even += 1
    else:
        odd += 1

print("even numbers are:",even)
print("odd numbers are:",odd)



