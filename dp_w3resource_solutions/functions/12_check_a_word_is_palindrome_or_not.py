"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function that checks whether a passed string is palindrome or not
"""
# A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


# def reverse_str(text):
#     if not isinstance(text, str) or len(text) == 0:
#         return None
#     reversed_str = ''
#     for each in text:
#         reversed_str = each + reversed_str
#     return reversed_str


def is_palindrome(text):
    text = text.replace(' ', '')
    return text == text[::-1]
    # return text == reverse_str(text)  # Another method, to reverse a string in python using for loop


print(is_palindrome('madam'))
print(is_palindrome('nurses run'))
print(is_palindrome('divyesh'))
