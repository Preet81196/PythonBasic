"""
Write a Python program to test whether a passed letter is a vowel or not.
"""
vowel_list = ['a', 'e', 'i', 'o', 'u']


def is_vowel(ch):
    if ch.lower() in vowel_list:
        return True
    return False


print(is_vowel('u'))
