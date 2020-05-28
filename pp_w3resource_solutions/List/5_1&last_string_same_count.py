"""5. Write a Python program to count the number of strings where the string length
 is 2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']"""


def str1(list):
    count = 0
    for i in list:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
    return count
print(str1(['abc', 'xyz', 'aba', '1221']))