"""
Write a Python program to test whether a passed letter is a vowel or not.
"""
vowel_list = ['a', 'e', 'i', 'o', 'u']

def isVowel(ch):
    if ch in vowel_list:
        return True
    return False

print(isVowel('u'))