str1 = input("enter string :")
length = len(str1)

if length > 2:
    if str1[-3:] == "ing":
       str1 = str1 + 'ly'
       print(str1)
    else:
        str1 = str1 + "ing"
        print(str1)    