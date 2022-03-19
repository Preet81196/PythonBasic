"""Write a Python program that accepts a word from the user and reverse it"""

wo = input("Input a word to reverse: ")

for char in range(len(wo) - 1, -1, -1):
    print(wo[char],end="")
print("\n")