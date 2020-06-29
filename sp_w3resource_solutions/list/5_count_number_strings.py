""" Write a Python program to count the number of strings where the string length is 2 or more and
the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

list = ['abc', 'xyz', 'aba', '1221']
cnt = 0
for each in list:
    if len(each) >= 1 and each [0] == each[-1]:
        cnt += 1

print(cnt)

