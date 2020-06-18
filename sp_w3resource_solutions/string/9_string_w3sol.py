""" Write a Python program to remove the nth index character from a nonempty string"""


txt = input("Enter string: ")
n = int(input("enter index: "))
def remove_char(txt,n):
    str1 = txt[:n]
    str2 = txt[n + 1:]
    return str1 + str2


print(remove_char(txt,n))

