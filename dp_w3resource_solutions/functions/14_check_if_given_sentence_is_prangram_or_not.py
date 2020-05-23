"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function to check whether a string is a pangram or not.
"""

# Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"


def is_pangram(sequence):
    sequence = sequence.lower()
    alphabets = 'qwertyuiopasdfghjklzxcvbnm'
    for each in alphabets:
        if each not in sequence:
            return False
    return True


print(is_pangram('divyesh'))
print(is_pangram('The quick brown fox jumps over the lazy dog'))
