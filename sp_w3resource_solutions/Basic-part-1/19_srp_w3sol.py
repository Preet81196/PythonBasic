"""Write a Python program to get a new string from a given string where "Is" has been added to the front.
   If the given string already begins with "Is" then return the string unchanged.   """

str = str(input("Enter string:"))
if str[0]=='l' and str[1]=='s':
     print(str)
else:
     print("ls"+str)
