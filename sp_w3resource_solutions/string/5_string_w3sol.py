"""  Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'"""

text = input("Enter 1st string")
text2 = input("Enter 2nd string")

new1 = text2[:2] + text[2:]
new2 = text[:2] + text2[2:]

print(new1 + ' ' + new2)