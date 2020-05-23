"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 23/05/20
* @decription: Write a Python function that accepts a string and calculate
            the number of upper case letters and lower case letters.
"""


def get_case_counts(text):
    if len(text) == 0 or not isinstance(text, str):
        return None, None

    upper_count = 0
    lower_count = 0
    for each in text:
        if each.isupper():
            upper_count += 1
        if each.islower():
            lower_count += 1
    return upper_count, lower_count


total_upper, total_lower = get_case_counts('Hello World this is Divyesh Patel')
print('total upper:', total_upper)
print('total, lower:', total_lower)
