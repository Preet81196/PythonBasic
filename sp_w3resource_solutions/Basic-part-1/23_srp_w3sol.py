""" Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2.   """


text = input("Enter string:")
copy = int(input("Number of copies:"))

length = len(text)

if length > 2 :
    for i in range(copy):
        print(text[0],text[1])
elif length < 2:
    for i in range(copy):
        print(text)
else:
        print("error")
