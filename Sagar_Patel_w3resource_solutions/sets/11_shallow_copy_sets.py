"""Write a Python program to create a shallow copy of sets.

Note : Shallow copy is a bit-wise copy of an object.
A new object is created that has an exact copy of the values in the original object. """

numbers = {1, 2, 3, 4}
new_numbers = numbers

new_numbers.add(5)
new_numbers1 = numbers.copy()
new_numbers1.add(6)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)

print('new_numbers1: ', new_numbers1)