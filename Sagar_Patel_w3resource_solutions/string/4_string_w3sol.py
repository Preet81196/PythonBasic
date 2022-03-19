"""  Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'"""

text = input("Enter string:")
str1 = text[0]
str2 = text[1:].replace(str1,"$")


print(str1 + str2)